from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


try:
    class Bot:
        """docstring for Bot"""

        def __init__(self):
            self.bot = webdriver.Chrome()
            self.bot.set_window_size(900, 800)
            self.bot.set_window_position(600, 20)

        def login(self, username, password):
            self.username = username
            self.password = password
            bot = self.bot

            bot.get('https://instagram.com')
            time.sleep(3)
            username = bot.find_element(By.NAME, 'username')
            password = bot.find_element(By.NAME, 'password')
            username.clear()
            password.clear()
            username.send_keys(self.username)
            time.sleep(3)
            password.send_keys(self.password + Keys.RETURN)
            time.sleep(3)

        def likePost(self):
            bot = self.bot
            wait = WebDriverWait(bot, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/explore/"]'))).click()
            time.sleep(5)
            div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'K6yM_')))
            time.sleep(5)
            for i in range(3):
                bot.execute_script(
                    'window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(10)
            posts = div.find_elements(By.TAG_NAME, 'a')
            links = []
            for post in posts:
                link = post.get_attribute('href')
                links.append(link)
                print(link)
                print(len(links))
            for link in links:
                bot.get(link)
                time.sleep(3)
                div = bot.find_element(By.CLASS_NAME, 'eo2As')
                like = div.find_elements(By.TAG_NAME, 'button')
                like[0].click()
                time.sleep(3)

    ovi = Bot()
    ovi.login('ovaixe', '')
    ovi.likePost()
finally:
    ovi.bot.quit()
