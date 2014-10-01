#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from openpyxl import load_workbook
from openpyxl import Workbook
import time

user_names = load_workbook('/home/sameer/linkedin-scraper/NEST_users.xlsx')
ws = user_names.active

NEST_check = Workbook()
nest = NEST_check.active
# Load driver.
driver = webdriver.Chrome('/usr/bin/chromedriver')

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
errs = []
for userno in range(1,242) :
    try:
        search_box = driver.find_element_by_name('keywords')
        search_box.clear()
        search_box.send_keys(ws.cell(row = userno, column = 2).value + ' ' + ws.cell(row = userno, column = 1).value)
        search_box.submit()
        time.sleep(5)
        plink = driver.find_element_by_class_name('title').get_attribute('href')
        pname = driver.find_element_by_class_name('title').text
        ptitle = driver.find_elements_by_class_name('description')[1].text
        users += driver.find_element_by_class_name('title').get_attribute('href')
        nest.cell(row = userno, column = 1).value = pname
        nest.cell(row = userno, column = 2).value = ptitle
        nest.cell(row = userno, column = 3).value = plink
        print str(userno) + ' ' + pname + ' ' + ptitle
    except:
        errs.append(ws.cell(row = userno, column = 2).value)
        # record name for error

fails = open('NEST_fails', 'w')
fails.write(str(errs))
fails.close()

links = open('links_nest', 'w')
links.write(str(users))
links.close()
print 'Done saving.'

NEST_check.save('NEST_lookup.xlsx')
driver.quit()
