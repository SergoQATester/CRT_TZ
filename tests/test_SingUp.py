from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import unittest

# Условие: для успешного прохождения тестов аккаунты должны быть зарегистрированы.

class TestSingup(unittest.TestCase):
    def test_notext(self): # ввод пустых полей
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.LINK_TEXT, "login page")
            assert "login page" == error.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_onlyemail(self): # заполнено только поле имэйл
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Email = browser.find_element(By.NAME, "email")
            Email.send_keys("Python@mail.com")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.LINK_TEXT, "login page")
            assert "login page" == error.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_onlyname(self): # заполнено только поле нэйм
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Name = browser.find_element(By.NAME, "name")
            Name.send_keys("Python")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.LINK_TEXT, "login page")
            assert "login page" == error.text

        finally:
            time.sleep(2)
            browser.quit()
    def test_onlypassword(self): # заполнено только поле пассворд
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Password = browser.find_element(By.NAME, "password")
            Password.send_keys("Python")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.LINK_TEXT, "login page")
            assert "login page" == error.text    
        finally:
            time.sleep(2)
            browser.quit()
    def test_requiredfields(self): # заполнены обязательные поля email, password
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Email = browser.find_element(By.NAME, "email")
            Email.send_keys("Python@mail.com")
            Password = browser.find_element(By.NAME, "password")
            Password.send_keys("Python")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.LINK_TEXT, "login page")
            assert "login page" == error.text    
        finally:
            time.sleep(2)
            browser.quit()
    def test_all(self): # все поля заполнены корректно
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Email = browser.find_element(By.NAME, "email")
            Email.send_keys("Python@mail.com")
            Name = browser.find_element(By.NAME, "name")
            Name.send_keys("Python")
            Password = browser.find_element(By.NAME, "password")
            Password.send_keys("Python")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.CSS_SELECTOR, ".notification.is-danger")
            assert "Email address already exists. Go to login page." == error.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_allsymbol(self): # все поля заполнены не корректно, все поля содержат символы
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Email = browser.find_element(By.NAME, "email")
            Email.send_keys("!!!!!@mail.com")
            Name = browser.find_element(By.NAME, "name")
            Name.send_keys("!!!@@@$$$")
            Password = browser.find_element(By.NAME, "password")
            Password.send_keys("!!!@@@$$$")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.CSS_SELECTOR, ".notification.is-danger")
            assert "Email address already exists. Go to login page." == error.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_othercount(self): # все поля заполнены не корректно, большое или малое количество букв или символов
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/signup")
            Email = browser.find_element(By.NAME, "email")
            Email.send_keys("!!sfsfsfsesefgefgeseggsegsgsgsegsegsgsgsgsgsg!!!@mail.com")
            Name = browser.find_element(By.NAME, "name")
            Name.send_keys("!")
            Password = browser.find_element(By.NAME, "password")
            Password.send_keys("!")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            error = browser.find_element(By.CSS_SELECTOR, ".notification.is-danger")
            assert "Email address already exists. Go to login page." == error.text
        finally:
            time.sleep(2)
            browser.quit()
    


if __name__ == "__main__":
    unittest.main()