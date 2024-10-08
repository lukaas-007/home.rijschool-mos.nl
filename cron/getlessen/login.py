from selenium.webdriver.common.by import By
import time

def login_to_autofox(driver, email, password, login_url):
    """Logs in to the AutoFox website."""
    driver.get(login_url)

    # Log in
    driver.find_element(By.ID, 'm1_Cln1_txtUsername').send_keys(email)
    driver.find_element(By.ID, 'm1_Cln1_txtPassword').send_keys(password)
    driver.find_element(By.ID, 'm1_Cln1_cmdLogin').click()

    # Wait for the page to load
    time.sleep(5)
