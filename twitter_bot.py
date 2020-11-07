from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SendTweets:
    def __init__(self, tweetNo, tweet, timeIn, passIn, userIn):
        self.tweetNo = tweetNo
        self.tweet = tweet
        self.timeIn = timeIn
        self.passIn = passIn
        self.userIn = userIn

        self.PATH = "chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)

    def login(self):
        self.driver.get("https://www.twitter.com/login")

        time.sleep(5)
        user_field = self.driver.find_element_by_name("session[username_or_email]")
        pass_field = self.driver.find_element_by_name("session[password]")

        user_field.send_keys(f"{self.userIn}")
        pass_field.send_keys(f"{self.passIn}")
        pass_field.send_keys(Keys.RETURN)

        time.sleep(3)

        if "Home" in self.driver.title:
            print("it's running")
            self.tweetMessage()

    
    def tweetMessage(self):
        SpamBarrier = "."
        for a in range(0, self.tweetNo)
            time.sleep(self.timeIn)
            tweet = self.driver.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                        /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                        /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                        /div/div/div''')
            tweet.send_keys(f"""{self.tweet}""" + SpamBarrier)
            tweet.send_keys(Keys.CONTROL, Keys.ENTER)
            SpamBarrier += "."


if __name__ == "__main__":
    tweetNo = int(input("Enter the Number of tweets (integer) you want to send: "))
    tweet = input("Enter the tweet(sentence): ")
    timeIn = int(input("Enter the buffer time (integer) between each tweet"))
    passIn = input("Enter your account Password: ")
    userIn = input("Enter your account Username: ")
    Obj = SendTweets(tweetNo, tweet, timeIn, passIn, userIn)
    Obj.login()




