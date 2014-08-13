#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs

with open('/home/sameer/2.html', 'r') as profile:
	soup = bs(profile)
	name = soup.find("span","full-name").string
	title = soup.find("p","title").text
	summary = soup.find("div","summary").text
	experience = ''
	exp = soup.find(id="background-experience")
	for string in exp.stripped_strings:
		experience = experience + string + '\n'
	#exp2 = experience.encode('utf-8')
	#exp2.replace('\n–\n',' - ')
	skillset = ''
	skills = soup.find_all("span","endorse-item-name")
	for skill in skills:
		skillset = skillset + skill.text + '\n'
	education = ''
	edu = soup.find(id="background-education")
	for string in edu.stripped_strings:
		education = education + string + '\n'
	interests = soup.find("ul","interests-listing").text

