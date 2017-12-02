'''
Author: Tom Rafter
Description: Uses selenium to automate new user build
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time, csv, numpy as np
import pyautogui as py
import sys
import test
driver = webdriver.Chrome()
un=test.un
pw=test.pw

fname=('testfn')
lname=('testln')
email=(fname+'.'+lname+'@bch.org')
testclinic='//*[@id="div_id_username"]/div/div/a[4]'


def login():
	driver.get("https://dashboard.seamlessmedical.com/login#")
	time.sleep(2)
	username = driver.find_element_by_xpath('//*[@id="id_username"]')
	username.send_keys(un)
	passw = driver.find_element_by_xpath('//*[@id="id_password"]')
	passw.send_keys(pw)
	button = driver.find_element_by_xpath('//*[@id="submit-id-submit"]').click()

def clinic():
	driver.find_element_by_xpath(testclinic).click()
def userbuild():
	settings=driver.find_element_by_xpath('//*[@id="main-tabs"]/li[2]/a').click()
	users=driver.find_element_by_xpath('//*[@id="sub-nav"]/li[5]/a').click()
	newusers=driver.find_element_by_xpath('//*[@id="sidebar"]/div/a').click()
	firstname=driver.find_element_by_xpath('//*[@id="id_first_name"]')
	firstname.send_keys(fname)
	lastname=driver.find_element_by_xpath('//*[@id="id_last_name"]')
	lastname.send_keys(lname)
	role=driver.find_element_by_xpath('//*[@id="id_type"]')
	role.send_keys('staff')
	emailaddress=driver.find_element_by_xpath('//*[@id="id_email"]')
	emailaddress.send_keys(email)
	submit=driver.find_element_by_xpath('//*[@id="userEdit"]/div/div[1]/a[1]').click()
	


login()
clinic()
userbuild()

