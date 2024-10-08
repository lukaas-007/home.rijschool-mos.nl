from selenium.webdriver.common.by import By
import time

def change_week(driver, weeks=1):
    """Clicks the next week button the specified number of times."""
    for _ in range(weeks):
        driver.find_element(By.CLASS_NAME, 'fc-next-button').click()
        
        time.sleep(5)  # Wait for the page to load
