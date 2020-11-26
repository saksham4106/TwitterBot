from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *

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
        for a in range(0, self.tweetNo):
            time.sleep(self.timeIn)
            tweet = self.driver.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                        /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                        /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                        /div/div/div''')
            tweet.send_keys(f"""{self.tweet}""" + SpamBarrier)
            tweet.send_keys(Keys.CONTROL, Keys.ENTER)
            
            
            SpamBarrier += "."



def startProgram(entry1, entry2, entry3, entry4, entry5):
        
    
    tweetNo = int(entry1.get())
    tweet = entry2.get()
    timeIn = int(entry3.get())
    passIn = entry5.get()
    userIn = entry4.get()
    Obj = SendTweets(tweetNo, tweet, timeIn, passIn, userIn)
    Obj.login()

if __name__ == "__main__":
    win = Tk()
    win.geometry("300x300")
    label1 = Label(win, text = "Nuber of tweets")
    label1.place(x=0,y=10)
    entry1 = Entry(win)
    entry1.place(x=90,y=10)

    label2 = Label(win, text = "Enter the Tweet")
    label2.place(x=0, y = 30)
    entry2 = Entry(win)
    entry2.place(x=90, y = 30)

    label3 = Label(win, text = "Enter the Time between Each Tweet")
    label3.place(x = 0, y = 50)
    entry3 = Entry(win)
    entry3.place(x = 25, y = 70)

    label4 = Label(win, text = "Twitter Username")
    label4.place(x=0, y = 100)
    entry4 = Entry(win)
    entry4.place(x=100, y = 100)

    label5 = Label(win, text = "Twitter Password")
    label5.place(x=0, y = 130)
    entry5 = Entry(win, show = "*")
    entry5.place(x=100, y = 130)



    button1 = Button(win, text = "Start", command = lambda:startProgram(entry1,entry2,entry3,entry4,entry5))
    button1.place(x = 150, y = 200)


    win.mainloop()







