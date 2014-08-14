#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from openpyxl import Workbook
import time

# Load driver.
driver = webdriver.Chrome('/home/sameer/bin/chromedriver')

# Go to LinkedIn.
driver.get('http://www.linkedin.com/');

# Login
login_box = driver.find_element_by_name('session_key')
password_box = driver.find_element_by_name('session_password')
login_box.send_keys('pvora2@gmail.com')
password_box.send_keys('Opensilo1')
password_box.submit()

links = open('./links_nest', 'r')
users = eval(links.read())
print len(users)

wb = Workbook()
ws = wb.active

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
            ws.cell(row = userno, column = 1).value = name.decode('utf-8','ignore')
            ws.cell(row = userno, column = 2).value = str(ulink)
            userno +=1
        else:
            print 'Not a link :('
except:
    errorlinks.append(ulink)
    print 'Some exception'
    
fails = open('failed_links', 'w')
fails.write(str(errorlinks))
fails.close()

wb.save('NEST_lookup.xlsx')

driver.quit()
