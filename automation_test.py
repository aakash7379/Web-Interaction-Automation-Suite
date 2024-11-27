from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
driver_path = r"C:\Windows\chromedriver.exe" # Replace with your actual ChromeDriver path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Navigate to the FitPeo Homepage
    driver.get("https://www.fitpeo.com")  # Replace with actual homepage URL
    driver.maximize_window()
    print("Navigated to FitPeo Homepage.")

    # Step 2: Navigate to Revenue Calculator Page
    revenue_calculator_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator"))  # Replace with actual link text
    )
    revenue_calculator_link.click()
    print("Navigated to Revenue Calculator Page.")

    # Step 3: Scroll Down to the Slider Section
    slider_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "slider_section"))  # Replace with actual slider section ID
    )
    driver.execute_script("arguments[0].scrollIntoView();", slider_section)
    print("Scrolled to Slider Section.")

    # Step 4: Adjust the Slider to 820
    slider = driver.find_element(By.ID, "slider_id")  # Replace with actual slider ID
    ActionChains(driver).click_and_hold(slider).move_by_offset(820, 0).release().perform()
    time.sleep(1)  # Allow slider movement
    slider_value = driver.find_element(By.ID, "slider_value_id").text  # Replace with actual ID for slider value
    assert slider_value == "820", "Slider value did not update to 820."
    print("Slider adjusted to 820.")

    # Step 5: Update the Text Field to 560
    text_field = driver.find_element(By.ID, "text_field_id")  # Replace with actual text field ID
    text_field.clear()
    text_field.send_keys("560")
    time.sleep(1)  # Allow time for the change to take effect
    updated_slider_value = slider.get_attribute("value")  # Replace with the correct attribute or method
    assert updated_slider_value == "560", "Slider does not reflect updated text field value."
    print("Text field updated to 560 and slider synchronized.")

    # Step 6: Select CPT Codes
    cpt_codes = ["CPT-99091", "CPT-99453", "CPT-99454", "CPT-99474"]
    for code in cpt_codes:
        checkbox = driver.find_element(By.ID, f"checkbox_{code}")  # Replace with actual checkbox IDs
        if not checkbox.is_selected():
            checkbox.click()
    print("CPT codes selected.")

    # Step 7: Validate Total Recurring Reimbursement
    total_reimbursement = driver.find_element(By.ID, "total_reimbursement_id")  # Replace with correct ID
    assert total_reimbursement.text == "$110700", "Total reimbursement value mismatch."
    print("Total Recurring Reimbursement validated successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()  # Ensure the browser is closed properly
    print("Driver quit successfully.")
