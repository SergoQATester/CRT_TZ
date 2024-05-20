from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# Условие: для успешного прохождения тестов аккаунты должны быть зарегистрированы.

class TestSingup(unittest.TestCase):
    def test_notextandcheckbox(self): # ввод пустого логина, пароля, чекбокса
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/login")
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            text = browser.find_element(By.CSS_SELECTOR, ".container.has-text-centered")
            assert "Welcome, !" == text.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_notext(self): # ввод пустого логина, пароля
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/login")
            checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
            checkbox.click()
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            text = browser.find_element(By.CSS_SELECTOR, ".container.has-text-centered")
            assert "Welcome, !" == text.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_email(self): # ввод логина и чекбокса
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/login")
            Email = browser.find_element(By.NAME, "email")
            Email.send_keys("Python@mail.com")
            checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
            checkbox.click()
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            text = browser.find_element(By.CSS_SELECTOR, ".notification.is-danger")
            assert "Please check your login details and try again." == text.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_password(self): # ввод пароля и чекбокса
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/login")
            password = browser.find_element(By.NAME, "password")
            password.send_keys("Python")
            checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
            checkbox.click()
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            text = browser.find_element(By.CSS_SELECTOR, ".notification.is-danger")
            assert "Please check your login details and try again." == text.text
        finally:
            time.sleep(2)
            browser.quit()
    def test_all(self): # ввод корректного логина, пароля, чекбокса
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.get("http://localhost:5000/login")
            Email = browser.find_element(By.NAME, "email")
            Email.send_keys("Python@mail.com")
            password = browser.find_element(By.NAME, "password")
            password.send_keys("Python")
            checkbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
            checkbox.click()
            Button = browser.find_element(By.CSS_SELECTOR, ".button.is-block.is-info.is-large.is-fullwidth")
            Button.click()
            text = browser.find_element(By.CSS_SELECTOR, ".container.has-text-centered")
            assert "Welcome, Python!" == text.text
        finally:
            time.sleep(2)
            browser.quit()

if __name__ == "__main__":
    unittest.main()