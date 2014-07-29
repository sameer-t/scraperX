#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import csv

from copy import copy
from openpyxl import Workbook
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

def dur_mon (totdur):
	if 'year' in totdur:
		ny = int(totdur[totdur.find('(')+1:totdur.find('year')-1])
	else:
		ny = 0
	if 'month' in totdur and not 'year' in totdur:
		nm = int(totdur[totdur.find('(')+1:totdur.find('month')-1])
	elif 'month' in totdur and 'year' in totdur:
		nm = int(totdur[totdur.find('month')-3:totdur.find('month')-1])
	else:
		nm = 0
	tm = ny*12 + nm
	return tm

def trim (des):
	desc = des.encode('utf8')
	toremove = ['•', '-','\n1.','\n2.','\n3.','\n4.','\n5.','\n6.','\n7.','\n8.','\n9.','\n10.','\n11.','\n12.', '\n13.', '\n14.', '\n15', '\n\n']
	for symbol in toremove:
		if symbol in desc:
			desc = desc.replace(symbol,'') 
	return desc

def maploc (dop, place):
	for k in dop:
		for v in dop[k]:
			if place in v:
				return k
	return place

ctm = {}
maplocs = load_workbook(filename='/home/sameer/cities to map.xlsx',use_iterators=True)
for area in maplocs.get_sheet_names():
	ctm[area] = []
	ts = maplocs[area]
	for row in ts.iter_rows():
		for cell in row:
			ctm[area].append(cell.value)

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

# Go to Uber page.
driver.get('https://www.linkedin.com/company/1815218')

# Find number of users.
#user_count = (driver.find_elements_by_class_name('density')[2].text)
#user_count = int(user_count.replace(',', ''))
#print user_count

# Get to list page.
driver.find_element_by_link_text('See all').click()
driver.find_element_by_id('us:84-G-ffs').click()

time.sleep(3)

# Start scraping.

try:
    users = []
    while len(users) < users:
        users += [element.get_attribute('href') for element in driver.find_elements_by_class_name('title')]
        print len(users)
        driver.get(driver.find_element_by_link_text('Next >').get_attribute('href'))
except Exception:
    #print users
    links = open('links', 'w')
    links.write(str(users))
    print 'Acquired links to user profiles.'

links = open('./links', 'r')
users = eval(links.read())
print len(users)

alluserdat = []
userno = 1 
i = 1

try:
	for link in users:
		if str(type(link)) == "<type 'unicode'>":
			driver.get(str(link))
			print userno
			userdat = []
			data = ''
			try:
				#Name
				try:
					userdat.append(str(userno) + '. ' + driver.find_element_by_class_name('full-name').text + '\n')
					print 'Name Done'
				except:
					userdat.append('No Name')
					print 'No Name'			
				#Title
				try:
					data = data + trim(driver.find_element_by_class_name('title').text) + '\n'
					print 'Title Done'
				except:
					print 'No Title' 
				#Summary						
				try:
					wrapper1 = driver.find_element_by_class_name('summary')
					data = data + trim(wrapper1.find_element_by_class_name('description').text) + '\n'
				except NoSuchElementException:
					print 'No Summary'
				print 'Summary Done'
				#Skills
				try:
					wrapper3 = driver.find_elements_by_class_name('endorse-item-name')
					for v in range(len(wrapper3)):
						ski = wrapper3[v].text.replace('...','')
						if ski != '':
							data = data + trim(ski) + '\n'
					print 'Skills Done'
				except:
					print 'No Skills'
				#Education
				try:
					wrapper4 = driver.find_element_by_id('background-education')
					er = wrapper4.find_elements_by_class_name('editable-item')
					for i in range(len(er)):
						data = data + trim(er[i].text) + '\n'
					print 'Edu Done'
				except:
					print 'No Education'
				#Additional Info - Interests
				try:
					wrapper5 = driver.find_element_by_class_name('interests-listing')
					data = data + trim(wrapper5.text) + '\n'
				except NoSuchElementException:
					print 'No interests'
				print 'Int Done'
				#Experience
				try:
					wrapper2 = driver.find_element_by_id('background-experience')
					qw = wrapper2.find_elements_by_class_name('editable-item')
					for k in range(len(qw)):
						data = data + trim(qw[k].text) + '\n'
					print 'Exp Done'
				except:
					print 'No Exp'
				data = data.decode('utf-8')
				data = trim(data)
				userdat.append(data)
				alluserdat.append(userdat)
			except NoSuchElementException:
				print 'element not found'
			print 'Done saving.'
			userno += 1
		else:
			print 'Not a link :('
except:
    print 'Some exception'

with open('alluserdat', 'wt') as fout:
	csvout = csv.writer(fout)
	csvout.writerows(alluserdat)

#driver.quit()
