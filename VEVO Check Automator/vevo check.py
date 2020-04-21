from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import os

# Using os module to get sensitive data from user variable
dob = os.environ.get("VEVO_DOB")
passportnumber = os.environ.get("VEVO_PPT")
email = os.environ.get("VEVO_EMAIL")
visagrantnumber = os.environ.get("VEVO_GRANT")
chromedriver = os.environ.get("CHROME_DRIVER")

# Instantiate a chrome options object to set size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
# Set driver to run based on args added
driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)
# Telling Chrome to open Immi website.
driver.get("https://online.immi.gov.au/evo/firstParty?actionType=query")

# Use Select to open drop-down to choose document type
documenttype = Select(driver.find_element_by_id("_2a0a2a0a2a0a1a_input"))
time.sleep(2)
# Select Passport
documenttype.select_by_visible_text("Passport")
time.sleep(2)

# Use Select to open drop-down too choose reference type
referencetype = Select(driver.find_element_by_id("_2a0a2a0a2c1a0b_input"))
time.sleep(2)
# Select Visa Grant Number
referencetype.select_by_visible_text("Visa Grant Number")

# Wait for 2 secs, gives next dropdown chance to open
time.sleep(2)

# Find Visa Grant Number box
referencetypenumber = driver.find_element_by_id("_2a0a2a0a2c1b1b0_input")
# Insert Visa Grant Number
referencetypenumber.send_keys(visagrantnumber)

# Find DOB entry box
dobinsert = driver.find_element_by_id("_2a0a2a0a2e0a1a_input")
# Insert DOB into box
dobinsert.send_keys(dob)

# Find passport number entry box
passportinsert = driver.find_element_by_id("_2a0a2a0a2e0b1a_input")
# Insert passport number
passportinsert.send_keys(passportnumber)

# Find country drop-down box
country = Select(driver.find_element_by_id("_2a0a2a0a2e0c1a_input"))
# Select country
country.select_by_visible_text("UNITED KINGDOM - BRITISH CITIZEN")

# Find checkbox that agrees to terms and conditions
checkbox = driver.find_element_by_id("_2a0a2a0a2f1b0_input").click()

# Find 'Submit' button and click
submit = driver.find_element_by_id("_2a0a2a0a3b0a").click()
time.sleep(2)

# Send VEVO check as PDF
sendemail = driver.find_element_by_id("_2a3a2a0a2c1b0").click()

# Enter email first time
inputemail1 = driver.find_element_by_id("_2a5a2a0a2a0b0_input")
inputemail1.send_keys(email)

# Repeat email for verification
inputemail2 = driver.find_element_by_id("_2a5a2a0a2a1b0_input")
inputemail2.send_keys(email)

# Press send button
sendvevo = driver.find_element_by_id("_2a5a2a0a3b0a").click()
