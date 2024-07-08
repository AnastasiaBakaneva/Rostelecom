import time
from selenium.webdriver.common.by import By

#Пустой email
def test_unsuccessful_auth_page_no_email(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
#Оставить поле ввода email пустым
    enter_email.send_keys('')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

#Ввести неверный email
def test_unsuccessful_auth_page_invalid_email(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
#Ввести неверный email
    enter_email.send_keys('bakaneva.test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

#1 символ в пароле
def test_one_symbol_in_password(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('1')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

#21 символ в пароле
def test_twenty_one_symbol_in_password(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('1234567890123456789Nj')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')

#Поле ввода пароль пустое
def test_unsuccessful_auth_page_no_password(driver):
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    time.sleep(5)


    enter_email = driver.find_element(By.XPATH,'//*[@id="username"]')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')

#Оставить поле ввода "пароль" пустым
    enter_password.send_keys('')
    time.sleep(6)

    auth = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@id="app"]/main[1]')
