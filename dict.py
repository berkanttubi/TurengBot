#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:41:56 2021

@author: berkanttubi
"""

from selenium import webdriver 
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions


options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

url = "https://tureng.com/en/turkish-english"
driver.get(url)

while True:
    word = input("Enter the word: ")
    if word == "exit":
        break
    searchBar= driver.find_element_by_xpath("//*[@id='searchTerm']")
    searchBar.send_keys(word)

    ara= driver.find_element_by_css_selector('input.btn:nth-child(5)')

    ara.click()

    elements= driver.find_element_by_xpath("//*[@id='englishResultsTable']")

    print(elements.text)

driver.quit()
