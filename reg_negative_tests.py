import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

# Пустое поле ввода "Имя"
def test_reg_page_empty_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Оставляем поле ввода "Имя" пустым
    enter_first_name.send_keys('')
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
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# Буквы на латинице в поле ввода "Имя"
def test_reg_page_letters_latin_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Вводим буквы на латинице в поле ввода "Имя"
    enter_first_name.send_keys('Anastasia')
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
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# 31 символ в поле ввода "Имя"
def test_reg_page_thirty_one_symbols_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Вводим в поле ввода "Имя" 31 символ
    enter_first_name.send_keys('СофияСофияСофияСофияСофияСофияя')
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
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# 1 символ в поле ввода "Имя"
def test_reg_page_one_symbol_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Вводим 1 символ в поле ввода "Имя"
    enter_first_name.send_keys('Т')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

#Вводим данные в поле ввода "Фамилия"
    enter_last_name.send_keys('Трискол')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# Пустое поле ввода "Фамилия"
def test_reg_page_empty_last_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Вводим "Имя"
    enter_first_name.send_keys('Ананас')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

#Оставить пустым поле ввода "Фамилия"
    enter_last_name.send_keys('')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# Буквы на латинице в поле ввода "Фамилия"
def test_reg_page_letters_latin_last_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Вводим в поле ввода имя
    enter_first_name.send_keys('Анастас')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

#Вводим данные в поле ввода "Фамилия" на латинице
    enter_last_name.send_keys('Sverev')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# 31 символ в поле ввода "Фамилия"
def test_reg_page_thirty_one_symbols_last_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    # Вводим имя в поле ввода
    enter_first_name.send_keys('София')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    # Вводим в поле ввода "Фамилия" 31 символ
    enter_last_name.send_keys('БерезовОсиновДупловЦветковГоршк')
    time.sleep(3)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


# 1 символ в поле ввода "Фамилия"
def test_reg_page_one_symbol_last_name(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    # Вводим имя в поле ввода
    enter_first_name.send_keys('Тая')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    # Вводим в поле ввода "Фамилия" 1 символ
    enter_last_name.send_keys('Т')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(1)
    choose_region_Mari_El = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(2)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test@mail.ru')
    time.sleep(2)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(3)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

#Регистрация с уже зарегистрированным email
def test_unsuccessful_email_already_used(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Анастас')
    time.sleep(4)


    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Ермолов')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')

#Вводим уже зарегистрированный email
    enter_email.send_keys('te-st@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# Пустое поле ввода "Email"
def test_reg_page_empty_email(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')

#Вводим "Имя"
    enter_first_name.send_keys('Ананас')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

#Вводим данные в поле ввода "Фамилия"
    enter_last_name.send_keys('Анастасов')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')

#Оставляем поле ввода "Email" пустым
    enter_email.send_keys('')
    time.sleep(4)


    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH,'//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

#Отсутствие @ в email
def test_unsuccessful_email_no_doggi(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Асия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Еловая')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')

 #Вводим email без @
    enter_email.send_keys('test.mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"


#Запятая вместо точки в доменной части email
def test_unsuccessful_email_comma_in_domain_part(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    enter_first_name.send_keys('Осия')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    enter_last_name.send_keys('Клылова')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()
    time.sleep(4)

    choose_region_Mari_El = driver.find_element(By.XPATH, "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[38]")
    choose_region_Mari_El.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')

# Вводим email с запятой вместо точки в доменной части
    enter_email.send_keys('test@mail,ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('123456789Nj')

    time.sleep(7)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# 7 символов в поле ввода "Пароль"
def test_reg_page_seven_symbols_password(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    # Вводим имя в поле ввода
    enter_first_name.send_keys('София')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    # Вводим фамилию в поле ввода
    enter_last_name.send_keys('Березов')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('12345Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('12345Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

# 21 символ в поле ввода "Пароль"
def test_reg_page_twenty_one_symbols_password(driver):
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(7)

    enter_first_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')

    # Вводим имя в поле ввода
    enter_first_name.send_keys('София')
    time.sleep(4)

    enter_last_name = driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')

    # Вводим фамилию в поле ввода
    enter_last_name.send_keys('Березов')
    time.sleep(4)

    wait = WDW(driver, 8)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'section#page-right > div > div > div > form > div:nth-of-type(2) > div > div > div:nth-of-type(2) > svg'))).click()

    time.sleep(4)
    choose_region_Altai = driver.find_element(By.XPATH,"//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div[3]")
    choose_region_Altai.click()
    time.sleep(3)

    enter_email = driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[3]/div/div/input')
    enter_email.send_keys('test@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys('1234567890123456789Nj')
    time.sleep(6)

    confirm_password = driver.find_element(By.XPATH, '//*[@id="password-confirm"]')
    confirm_password.send_keys('1234567890123456789Nj')

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@id="card-title"]').text != "Подтверждение email"

