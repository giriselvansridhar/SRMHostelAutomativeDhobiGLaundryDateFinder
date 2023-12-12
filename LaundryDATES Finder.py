from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import pywhatkit
import datetime

# Set the path to your Microsoft Edge WebDriver executable
edge_driver_path = r"C:\edgedriver_win64\msedgedriver.exe"




# Create an Edge WebDriver instance
driver = webdriver.Edge(executable_path=edge_driver_path)


# Navigate to the default URL
driver.get("https://dhobig.com/campus/")

try:
    # Find the input field with id "regNumber" on the first webpage and enter some text
    reg_number_input = driver.find_element(By.TAG_NAME, "input")  # Assuming it's an input element
    reg_number_input.send_keys("RA2311003020337")
    
    time.sleep(5)

    # Find the submit button and click it to submit the form
    submit_button = driver.find_element(By.ID, "submit1")  # Assuming it's a button element
    submit_button.click()
    
    time.sleep(5)

    # Wait for the second webpage to load (implicitly_wait)

    # Find the input field with id "mobile" on the second webpage and enter some text
    mobile_input = driver.find_element(By.ID, "mobile")  # Assuming it's an input element
    mobile_input.send_keys("9363604476")
    
    time.sleep(5)

    button = driver.find_element(By.CSS_SELECTOR, "button[onclick='checkMobile()'].btn.btn-primary")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

    time.sleep(10)
    

    # Wait for the third webpage to load (implicitly_wait)
    
    third_webpage_text = driver.find_element(By.TAG_NAME, "ul").text
    print(third_webpage_text)
    
   
    
    pywhatkit.sendwhatmsg_instantly("+919629794476",third_webpage_text,15)
    
    
    

  
finally:
    # Close the Edge browser window
    driver.quit()
    
    
    
