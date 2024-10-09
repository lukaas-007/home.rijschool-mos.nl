import json
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector

from login import login_to_autofox
from request_interceptor import intercept_last_request
from lesson_parser import parse_lessons, save_lessons_to_database
from navigation import change_week

# Configuration variables
_EMAIL = 'rijschoolmos@gmail.com'
_PASSWORD = '@Moss2022!'
_LINK = 'https://app.autofox.nl/rijschool/clarien/login'

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment if you want to run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(seleniumwire_options={}, options=chrome_options)

try:
    # Log in to the system
    login_to_autofox(driver, _EMAIL, _PASSWORD, _LINK)

    # Collect current week lessons
    current_week_data = intercept_last_request(driver, 'getresponse/isvsession/filters/planning/')
    current_week_lessons = parse_lessons(current_week_data)

    # Move to the next week and collect lessons
    change_week(driver)
    next_week_data = intercept_last_request(driver, 'getresponse/isvsession/filters/planning/')
    next_week_lessons = parse_lessons(next_week_data)

    # Move two weeks ahead and collect lessons
    change_week(driver)
    next_two_weeks_data = intercept_last_request(driver, 'getresponse/isvsession/filters/planning/')
    next_two_weeks_lessons = parse_lessons(next_two_weeks_data)

    # Combine all lessons
    all_new_lessons = current_week_lessons #+ next_week_lessons + next_two_weeks_lessons

    # Save updated lessons to the database
    save_lessons_to_database(all_new_lessons)

finally:
    # Close the browser
    driver.quit()
