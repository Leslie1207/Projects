from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

dob = ""
passportnumber = ("")
email = ""

#Storing path location of Opera browser driver in variable to pass through as argument below:
chromedriver = "C:\\Users\\lesli\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chromedriver)
#Telling Chrome to open Immi website.
driver.get("https://online.immi.gov.au/evo/firstParty?actionType=query")

#Use Select to open drop-down to choose document type
documenttype = Select(driver.find_element_by_id("_2a0a2a0a2a0a1a_input"))
time.sleep(2)
#Select Passport
documenttype.select_by_visible_text("Passport")
time.sleep(2)

#Use Select to open drop-down too choose reference type
referencetype = Select(driver.find_element_by_id("_2a0a2a0a2c1a0b_input"))
time.sleep(2)
#Select Visa Grant Number
referencetype.select_by_visible_text("Visa Grant Number")

#Wait for 5 secs, gives next dropdown chance to open
time.sleep(2)

#Find Visa Grant Number box
referencetypenumber = driver.find_element_by_id("_2a0a2a0a2c1b1b0_input")
#Insert Visa Grant Number
referencetypenumber.send_keys(visagrantnumber)

#Find DOB entry box
dobinsert = driver.find_element_by_id("_2a0a2a0a2e0a1a_input")
#Insert DOB into box
dobinsert.send_keys(dob)

#Find passport number entry box
passportinsert = driver.find_element_by_id("_2a0a2a0a2e0b1a_input")
#Insert passport number
passportinsert.send_keys(passportnumber)

#Find country drop-down box
country = Select(driver.find_element_by_id("_2a0a2a0a2e0c1a_input"))
#Select country
country.select_by_visible_text("UNITED KINGDOM - BRITISH CITIZEN")

#Find checkbox that agrees to terms and conditions
checkbox = driver.find_element_by_id("_2a0a2a0a2f1b0_input").click()

#Find 'Submit' button and click
submit = driver.find_element_by_id("_2a0a2a0a3b0a").click()
time.sleep(2)

#Send VEVO check as PDF
sendemail = driver.find_element_by_id("_2a3a2a0a2c1b0").click()

#Enter email first time
inputemail1 = driver.find_element_by_id("_2a5a2a0a2a0b0_input")
inputemail1.send_keys(email)

#Repeat email for verification
inputemail2 = driver.find_element_by_id("_2a5a2a0a2a1b0_input")
inputemail2.send_keys(email)

#Press send button
sendvevo = driver.find_element_by_id("_2a5a2a0a3b0a").click()
