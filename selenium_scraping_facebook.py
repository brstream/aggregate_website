import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os

# Username and password info
from secret import FACEBOOK_USERNAME, FACEBOOK_PASSWORD

chromedriver = '/Users/brstream/Downloads/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
display = Display(visible=0, size=(800, 600))
display.start()
br = webdriver.Chrome(chromedriver)
br.get('http://www.facebook.com/thichnhathanh/events')
e = br.find_element_by_name('email')
e.send_keys(FACEBOOK_USERNAME)
p = br.find_element_by_name('pass')
p.send_keys(FACEBOOK_PASSWORD)
p.send_keys(Keys.RETURN)
results = []
results = br.find_elements_by_css_selector('li.uiListItem.uiListMedium')
for result in results:
    print result.text
    print 8 * '-'
