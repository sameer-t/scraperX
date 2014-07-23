#!/usr/bin/env python

import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# Load driver.
driver = webdriver.Firefox()


# Go to LinkedIn.
driver.get('http://www.linkedin.com/');

# Login
login_box = driver.find_element_by_name('session_key')
password_box = driver.find_element_by_name('session_password')
login_box.send_keys('saisameer.t@gmail.com')
password_box.send_keys('santhishyam')
password_box.submit()


# Go to Uber page.
driver.get('https://www.linkedin.com/company/3032773')

# Find number of users.
user_count = int(driver.find_elements_by_class_name('density')[2].text)
print user_count

# Get to list page.
driver.find_element_by_link_text('See all').click()

# Start scraping.

try:
    users = []
    while len(users) < users:
        users += [element.get_attribute('href') for element in driver.find_elements_by_class_name('title')]
        print len(users)
        driver.get(driver.find_element_by_link_text('Next >').get_attribute('href'))

        
# except StandardError as e:
#     print repr(e)
#     print users
except Exception:
    print users
    links = open('links', 'w')
    links.write(str(users))
    print 'Done saving.'

links = open('./links', 'r')
users = eval(links.read())
print len(users)

alluserdat = []

try: 
        
    for link in users:
        driver.get(link)
        userdat = {}
        try:
			#Name
			userdat['Full_Name'] = driver.find_element_by_class_name('full-name').text
			
			#Summary						
			wrapper1 = driver.find_element_by_class_name('summary')
			userdat['Summary'] = wrapper1.find_element_by_class_name('description').text
			
			#Experience			
			userexp = []
			wrapper2 = driver.find_element_by_id('background-experience')
			qw = wrapper2.find_elements_by_class_name('editable-item')
			for i in range(len(qw)):
				userexp.append(qw[i].text)
			userdat['Experience'] = userexp 
			
			#Skills
			userskills = []
			wrapper3 = driver.find_element_by_class_name('skills-section')
			for wrap in wrapper3.find_elements_by_class_name('endorse-item-name'):
				userskills.append(wrap.find_element_by_class_name('endorse-item-name-text').text)
			userdat['Skills'] = userskills

			#Education
			useredu = []
			wrapper4 = driver.find_element_by_id('background-education')
			er = wrapper4.find_elements_by_class_name('editable-item')
			for i in range(len(er)):
				useredu.append(er[i].text)
			userdat['Education'] = useredu
			
			#Additional Info - Interests
			try:
				wrapper5 = driver.find_element_by_class_name('interests-listing')
				userint = wrapper5.text.split(', ')
			except NoSuchElementException:
				userint = ['Not listed']
			userdat['Interests'] = userint
			
        except NoSuchElementException:
            print 'element not found'
            
        alluserdat.append(userdat)
        print len(alluserdat)
        
    print 'Done saving.'

except Exception as e:
    logging.exception(e)
    print 'Done saving.'

#print alluserdat

userdata = open('userdata.txt', 'w')
userdata.write(str(alluserdat))
userdata.close()


'''
try: 
    profiles = []
    for link in users:
        driver.get(link)
        try:
            wrapper = driver.find_element_by_class_name('public-profile')
            profiles.append(wrapper.find_element_by_tag_name('span').text)
        except NoSuchElementException:
            print 'element not found'
        print len(profiles)
        saves = open('saves', 'w')
    saves.write(str(profiles))
    print 'Done saving.'
    print profiles

except Exception as e:
    logging.exception(e)
    print profiles
    saves = open('saves', 'w')
    saves.write(str(profiles))
    print 'Done saving.'

pros = open('pros.txt','w')
pros.write(str(profiles))
pros.close()

    # driver.quit()
'''
