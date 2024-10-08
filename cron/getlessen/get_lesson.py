import json
import gzip
from io import BytesIO
from seleniumwire import webdriver  # Use seleniumwire instead of selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_lessen():
    _agenda_item_array = []
    
    # Locate the agenda items
    _agenda_items = driver.find_elements(By.CLASS_NAME, 'fc-time-grid-event')
    
    for item in _agenda_items:
        # Extract relevant information from each item
        _agenda_item_body = item.find_element(By.CLASS_NAME, 'fc-item-body').text
        _agenda_item_start = item.find_element(By.CLASS_NAME, 'fc-timespan').text.split(' - ')[0]
        _agenda_item_end = item.find_element(By.CLASS_NAME, 'fc-timespan').text.split(' - ')[1]
        _agenda_item_style = item.get_attribute('style')
        
        # Create a dictionary for each agenda item
        _agenda_data = {
            'agenda_item_body': _agenda_item_body,
            'agenda_item_start': _agenda_item_start,
            'agenda_item_end': _agenda_item_end,
            'agenda_item_style': _agenda_item_style
        }
        
        # Append the dictionary to the list
        _agenda_item_array.append(_agenda_data)
    
    # Return the list of agenda items
    return _agenda_item_array

def intercept_last_request():
    # Loop through all requests intercepted by Selenium Wire
    last_request = None
    for request in driver.requests:
        if request.response and 'getresponse/isvsession/filters/planning/' in request.url:
            last_request = request
    
    if last_request is not None:
        print(f"URL: {last_request.url}")
        print(f"Response Status Code: {last_request.response.status_code}")
        
        # Check for gzip encoding in response headers
        if 'gzip' in last_request.response.headers.get('Content-Encoding', ''):
            print("Gzip encoding detected, decompressing...")
            # Decompress the gzipped response body
            compressed_data = BytesIO(last_request.response.body)
            with gzip.GzipFile(fileobj=compressed_data) as f:
                decompressed_data = f.read().decode('utf-8')
                
            # Replace the last character with ,
            decompressed_data = decompressed_data[:-1] + ','
            
            # Remove the first character
            decompressed_data = decompressed_data[1:]
            
            return decompressed_data
        else:
            # If no gzip, return the body directly
            return last_request.response.body.decode('utf-8')
    
    return None

def change_week_to_next():
    driver.find_element(By.CLASS_NAME, 'fc-next-button').click()
    time.sleep(5)
    # Wait for the page to load using webdriver wait

# Define the link and credentials
_EMAIL = 'rijschoolmos@gmail.com'
_PASSWORD = '@Moss2022!'
_LINK = 'https://app.autofox.nl/rijschool/clarien/login'

# Set up Chrome options to run in headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Open the headless browser using Selenium Wire
driver = webdriver.Chrome(seleniumwire_options={}, options=chrome_options)
driver.get(_LINK)

# Log in
driver.find_element(By.ID, 'm1_Cln1_txtUsername').send_keys(_EMAIL)
driver.find_element(By.ID, 'm1_Cln1_txtPassword').send_keys(_PASSWORD)

driver.find_element(By.ID, 'm1_Cln1_cmdLogin').click()

# Current weeks
time.sleep(5)
_agenda_items = intercept_last_request()
change_week_to_next()

# Next weeks
time.sleep(5)
_agenda_items += intercept_last_request()
change_week_to_next()

# 2 weeks ahead
time.sleep(5)
_agenda_items += intercept_last_request()

# Intercept and get the last network request to the specific URL
last_request_response = _agenda_items

# Save the last request response to a JSON file
if last_request_response:
    
    # Remove the last character from the response body
    last_request_response = last_request_response[:-1]
    
    last_request_response = '[' + last_request_response + ']'
    
    # Turn it into JSON
    getLessonJSON = json.loads(last_request_response)
    storedLessonJSON = json.loads(open('clarien_lessons.json').read())
    
    # Loop trough the stored lessons and if the lesson is also in getLessonJSON, remove it from the storedLessonJSON
    for storedLesson in storedLessonJSON:
        for getLesson in getLessonJSON:
            if storedLesson['id'] == getLesson['id']:
                storedLessonJSON.remove(storedLesson)
                print("Removed lesson with id: " + str(storedLesson['id']))
    
    with open('clarien_lessons.json', 'w') as f:
        #Clear the file 
        f.flush()
        
        f.write(json.dumps(getLessonJSON + storedLessonJSON, indent=4))
        f.close()

# Take a screenshot
driver.get_screenshot_as_file('screenshot.png')

# Print the title of the page and path to the screenshot we made
print('Screenshot saved as screenshot.png')

# Close the browser
driver.quit()
