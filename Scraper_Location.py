import logging
import time

from copy import copy
from openpyxl import Workbook
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('/home/sameer/bin/chromedriver')

driver.get('http://www.linkedin.com/');

