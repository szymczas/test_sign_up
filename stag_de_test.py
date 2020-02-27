import mail_generator
from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_path = r"C:\Users\szymon.hubicki\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
wait = WebDriverWait(driver, 10, 0.5)

maile = (mail_generator.generate_random_emails(1, 3))
print(maile[0])


driver.get("https://stag.dazn.com")
driver.maximize_window()
driver.find_element_by_css_selector('[data-testid="PROMO_CTA_BUTTON"]').click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="plan-details__wrapper_Annual"]')))
driver.find_element_by_css_selector('[data-test-id="plan-details__wrapper_Annual"]').click()
driver.find_element_by_css_selector('[data-test-id="FIRST_NAME"]').send_keys("Mojeimie")
driver.find_element_by_css_selector('[data-test-id="LAST_NAME"]').send_keys("Twojenazwisko")
driver.find_element_by_css_selector('[data-test-id="EMAIL"]').send_keys(maile)
driver.find_element_by_css_selector('[data-test-id="CONFIRM_EMAIL"]').send_keys(maile)
driver.find_element_by_css_selector('[data-test-id="PASSWORD"]').send_keys("11111a")
driver.save_screenshot("screenshots/" + maile[0] + ".png")
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="cookie-disclaimer-button"]')))
driver.find_element_by_css_selector('[data-test-id="cookie-disclaimer-button"]').click()
driver.find_element_by_css_selector('[data-test-id="button__icon"]').click()
free_trial = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="DIALOG_BUTTON-0"]')))
##if free_trial:
driver.find_element_by_css_selector('[data-test-id="DIALOG_BUTTON-0"]').click()
#else:
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="select-payment__option__CreditCard_Button"]')))
driver.find_element_by_css_selector('[data-test-id="select-payment__option__CreditCard_Button"]').click()
driver.find_element_by_css_selector('[data-test-id="CREDIT_CARD_NUMBER"]').click()
driver.find_element_by_css_selector('[data-test-id="CREDIT_CARD_NUMBER"]').send_keys('4111111111111111')
driver.find_element_by_css_selector('[data-test-id="EXPIRY_DATE-0"]').click()
driver.find_element_by_css_selector('[data-test-id="EXPIRY_DATE-0"]').send_keys('10 2020')
driver.find_element_by_css_selector('[data-test-id="SECURITY_CODE"]').click()
driver.find_element_by_css_selector('[data-test-id="SECURITY_CODE"]').send_keys('737')
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="CREDITCARD_PAYMENT_BUTTON"]')))
driver.find_element_by_css_selector('[data-test-id="CREDITCARD_PAYMENT_BUTTON"]').click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '[data-test-id="signUpConfirmation__BUTTON"]')))
driver.save_screenshot("screenshots/"  + maile[0] + "CP" + ".png")
driver.find_element_by_css_selector('[data-test-id="signUpConfirmation__BUTTON"]').click()


print(driver.title)
driver.quit()

