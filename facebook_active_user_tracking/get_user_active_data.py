from selenium import webdriver
import time
import os
from datetime import datetime, timedelta
from selenium.webdriver.firefox.options import Options
from pymongo import MongoClient

uri = "mongodb://toe:toe@localhost/test_data?authSource=facebook"
client = MongoClient(uri)
db = client.get_database('facebook')

opts = Options()
opts.add_argument('-private')

# os.environ['MOZ_HEADLESS'] = '1'
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
firefox_profile.set_preference("browser.cache.disk.enable", False)
firefox_profile.set_preference("browser.cache.memory.enable", False)
firefox_profile.set_preference("browser.cache.offline.enable", False)
firefox_profile.set_preference("network.http.use-cache", False) 

firefox_binary = '/usr/bin/firefox'
driver = webdriver.Firefox(firefox_profile=firefox_profile, firefox_options=opts, firefox_binary=firefox_binary)
driver.get("https://www.facebook.com")
driver.maximize_window()
email = driver.find_element_by_id("email")
# email.send_keys("abcdefeb389@gmail.com")
password = driver.find_element_by_id("pass")
# password.send_keys("@bcd3feb@fb")
login = driver.find_element_by_id("loginbutton")
# login.click()
time.sleep(15)

messenger = driver.find_element_by_xpath("//*[@id='navItem_217974574879787']/a/div")
messenger.click()

time.sleep(3)
#setting = driver.find_element_by_xpath("//*[@id='u_0_r']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a")
#setting.click()

#active_contacts = driver.find_element_by_link_text("Active Contacts")
#active_contacts.click()

time.sleep(15)

pre_active = 0
while True:
    driver.refresh()
    time.sleep(5)
    total_active = driver.find_element_by_xpath("//*[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div").text
    #total_active = total_active.replace("Active Contacts (", "")
    total_active = int("".join(list(filter(str.isdigit, total_active))))
    print(str(total_active))
    if pre_active!=total_active:
        print(str(total_active)+" users active at +" + str(datetime.now()-timedelta(minutes=20)))
        db.active_users.insert({"no_of_users":total_active, "active_time": datetime.now()-timedelta(minutes=20)})
        pre_active = total_active
    time.sleep(10)
#print("Url = " + driver.current_url)
time.sleep(5)
driver.quit()

