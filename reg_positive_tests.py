
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

#Регистрация с корректными данными
def test_reg_page_correct_data(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
#Вводим имя
    enter_first_name.send_keys('Анастасия')
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
#Вводим фамилию
    enter_last_name.send_keys('Баканёва')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Mari_El = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
#Вводим email
    enter_email.send_keys('test129@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
#Вводим пароль
    enter_password.send_keys('123456789Nj')
    time.sleep(6)
#Подтверждение пароля
    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(7)


    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


#2 символа в имени
def test_reg_page_two_symbols_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Вводим данные в поле ввода "Имя"
    enter_first_name.send_keys('Ан')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

#Вводим данные в поле ввода "Фамилия"
    enter_last_name.send_keys('Баканёва')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test-test@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# 30 символов в имени
def test_reg_page_thirty_symbols_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,  'section#page-right > div > div > div > form > div > div > div > input')

# Вводим данные в поле ввода "Имя"
    enter_first_name.send_keys('АнастасияАнастасияАнастасияАна')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

# Вводим данные в поле ввода "Фамилия"
    enter_last_name.send_keys('Баканёва')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)

    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test.te@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


#Спецсимволы в имени
def test_reg_page_hyphen_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

# Вводим имя со спецсимволами
    enter_first_name.send_keys('Анастасия-София')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Баканёва')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test-et@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('12345678Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('12345678Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# 2 символа в фамилии
def test_reg_page_two_symbols_last_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    # Вводим данные в поле ввода "Имя"
    enter_first_name.send_keys('Анастасия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    # Вводим данные в поле ввода "Фамилия"
    enter_last_name.send_keys('Ба')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test-ana@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


#30 символов в фамилии
def test_reg_page_thirty_symbols_last_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    # Вводим данные в поле ввода "Имя"
    enter_first_name.send_keys('Анастасия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    # Вводим данные в поле ввода "Фамилия"
    enter_last_name.send_keys('БаканёваБаканёваБаканёваБаканё')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test-Anast@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"

#Спецсимволы в фамилии
def test_reg_page_hyphen_last_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Анастасия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

#Вводим фамилию со спецсимволами
    enter_last_name.send_keys('Санта-Барбора')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('anas-test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('12345678Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('12345678Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"

#Спецсимволы в именной части email
def test_reg_page_hyphen_email_name_part(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Анастасия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Санта-Барбора')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('te2-2st@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('12345678Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('12345678Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"

#Цифры в именной части email
def test_reg_page_numbers_email_name_part(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Анастасия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Санта-Барбора')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')

 #Вводим цифры в именную часть email
    enter_email.send_keys('te377st@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('12345678Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('12345678Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"


# Цифры в доменной части email
def test_reg_page_numbers_email_domen_part(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Анастасия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Санта-Барбора')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')

    # Вводим цифры в доменную часть email
    enter_email.send_keys('anastasia87-test@mail456.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('12345678Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('12345678Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(9)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text == "Подтверждение email"
