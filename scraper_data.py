#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import os
from openpyxl import Workbook

def trim (des):
	desc = des.encode('utf-8')
	toremove = ['•','\n–\n','\n–','\n1.','\n2.','\n3.','\n4.','\n5.','\n6.','\n7.','\n8.','\n9.','\n10.','\n11.','\n12.', '\n13.', '\n14.', '\n15', '\n\n']
	for symbol in toremove:
		if symbol in desc:
			desc = desc.replace(symbol,' ') 
	return desc

wb = Workbook()
ws = wb.active

len_users = len(os.listdir('/home/sameer/NEST'))
for userno in range(1,len_users+1):
	profile = open('/home/sameer/NEST/'+ str(userno) + '.html', 'r')
	soup = bs(profile)
	try:
		name = trim(soup.find("span","full-name").string)
	except:
		name = 'No Name'
	try:
		title = trim(soup.find("p","title").text)
	except:
		title = 'No Title'
	try:
		pub_profile = soup.find("dl","public-profile").dd.string
		if pub_profile == '':
			pub_profile = soup.find("div","full-top-card-unsaved-public-profile").text
	except:
		pub_profile = 'No Public Profile'
	try:
		summary = trim(soup.find("div","summary").text)
	except:
		summary = 'No Summary'
	try:
		experience = ''
		exp = soup.find(id="background-experience")
		explist = exp.find_all('div','editable-item section-item')
		for expno in range(len(explist)):
			for string in explist[expno].stripped_strings:
				experience = experience + string + '\n'
		experience = trim(experience)
	except:
		experience = 'No Experience'
	try:
		skillset = ''
		skills = soup.find_all("span","endorse-item-name")
		for skill in skills:
			skillset = skillset + trim(skill.text) + '\n'
		skillset = trim(skillset)
	except:
		skillset = 'No Skills'
	try:
		education = ''
		edu = soup.find(id="background-education")
		edulist = edu.find_all('div','editable-item section-item')
		for eduno in range(len(edulist)):
			for string in edulist[eduno].stripped_strings:
				education = education + string + '\n'
		education = trim(education)
		education = education.replace('\n,\n',',')
	except:
		education = 'No education'
	try:
		interests = trim(soup.find("ul","interests-listing").text)
	except:
		interests = 'No interests'
	ws.cell(row = userno, column = 1).value = name.decode('utf-8','ignore')
	ws.cell(row = userno, column = 2).value = title.decode('utf-8','ignore')
	ws.cell(row = userno, column = 3).value = pub_profile.decode('utf-8','ignore')
	ws.cell(row = userno, column = 4).value = summary.decode('utf-8','ignore')
	ws.cell(row = userno, column = 5).value = experience.decode('utf-8','ignore')
	ws.cell(row = userno, column = 6).value = skillset.decode('utf-8','ignore')
	ws.cell(row = userno, column = 7).value = education.decode('utf-8','ignore')
	ws.cell(row = userno, column = 8).value = interests.decode('utf-8','ignore')
	print str(userno) + ' ' + name + ' done'

wb.save('NEST_raw.xlsx')
