#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# Load driver.
driver = webdriver.Chrome('/home/sameer/bin/chromedriver')

# Go to LinkedIn.
driver.get('http://www.linkedin.com/');

# Login
login_box = driver.find_element_by_name('session_key')
password_box = driver.find_element_by_name('session_password')
login_box.send_keys('<INSERT LINKEDIN USERNAME HERE>')
password_box.send_keys('<INSERT LINKEDIN PASSWORD HERE>')
password_box.submit()

# Get LinkedIn profile links
users = []
for  in  :
    try:
        search_box = driver.find_element_by_name('keywords')
        search_box.send_keys('lol')
        search_box.submit()
        result1 = driver.find_element_by_class_name('idx0')
        users += result1.find_element_by_class_name('title').get_attribute('href')
    except:
        # record name for error

links = open('links_nest', 'w')
links.write(str(users))
links.close()
print 'Done saving.'

driver.quit()
