#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from openpyxl import load_workbook
import time

pnplinks = load_workbook('/home/sameer/linkedin-scraper/pnp_links.xlsx')
ws = pnplinks.active

users = []
for pl in range(1,31):
	users.append(ws.cell(row = pl, column = 2).value)

print len(users)

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

errorlinks = []

userno = 1
try:
    for ulink in users:
        if str(type(ulink)) == "<type 'unicode'>":
            driver.get(str(ulink))
            time.sleep(5)
            name = driver.find_element_by_class_name('full-name').text
            print str(userno) + ' ' + name
            page_html = driver.page_source.encode('utf-8')
            user = open(str(userno)+'.html','w')
            user.write(page_html)
            user.close()
            userno +=1
        else:
            print 'Not a link :('
except:
    errorlinks.append(ulink)
    print 'Some exception'
    
fails = open('failed_links', 'w')
fails.write(str(errorlinks))
fails.close()

driver.quit()
