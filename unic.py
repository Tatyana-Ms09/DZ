
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def auth_test(driver, url, email, password):
    try:
        driver.get(url)

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        
        email_input.send_keys(email)

        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        return True

    except Exception as e:
        print(f"Error during authorization: {e}")
        return False

if __name__ == "__main__":
    driver = webdriver.Chrome()

    url = 'http://prestashop.qatestlab.com.ua/ru/authentication?back=my-account'
    email = 'your_email@example.com'
    password = 'your_password'

    auth_test(driver, url, email, password)

    driver.quit()
