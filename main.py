# Native Python library
import sys
import time
import random
# Third party library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# Other archives
from messages import msgList

# Target name, as saved on WhatsApp
contact_name = "Ue"

# Delay between sendo two messages
delay = 100 # In seconds

# How many messages until delay
count_until_interval = 20

# After send a count_until_interval, delay that time
interval = 600 # In seconds

# Quantity Control Variables
totalcount = 1
count = 0

# Elements in HTML
enter_name_element = "_2zCfw" # The area where you will enter the name to select
send_message_element = "_3u328" # The area where you will typed the message to send


# Saudation messages
print("\t======== WHATSAPP SPAM ========")
amount = int(input("How many messages do you want to send? "))

# Open the browser (Firefox) and visit the site
browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com/')
assert 'WhatsApp' in browser.title

# GarateMake sure you are logged in to your account before searchinge for the elements on the page
input("Log in using the QR Code and press enter ")

# Selecting the contact to send messages
print("Trying to select " + contact_name)
try:
    elem = browser.find_element_by_class_name(enter_name_element)
except NoSuchElementException:
    print("No such element. Impossible to select the contact, closing scrip...")
    sys.exit()
else:
    elem.send_keys(contact_name + Keys.RETURN)
    print("The selection has been sucessful")

# Try reach the area where will be typed the messages
try:
    elem = browser.find_element_by_class_name(send_message_element)
except NoSuchElementException:
    print("No such element. Impossible to select the area to type the messages, closing scrip...")
    sys.exit()

# Sending the messages
for i in range(amount):
    elem = browser.find_element_by_class_name(send_message_element)
    elem.send_keys(random.choice(msgList) + Keys.RETURN) # Choice a message in message list randomly
    print("\tSend {} messages".format(totalcount)) # Print in terminal the amount of sended messages
    if count >= count_until_interval:
        count = 0
        print("Interval")
        time.sleep(interval)
    else:
        time.sleep(delay)
    count += 1
    totalcount += 1
