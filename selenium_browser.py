from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

import os

# Get the path for the working directory
here = os.path.dirname(os.path.abspath(__file__))
# Use the above to determine the path to the chromedriver binary
chromedriver = here + '/bin/chromedriver'
# Put the chromedriver binary in the path
os.environ['webdriver.chrome.driver'] = chromedriver
# Initialize the chromedriver instance
display = Display(visible=0, size=(800, 600))
display.start()
browser = webdriver.Chrome(chromedriver)
