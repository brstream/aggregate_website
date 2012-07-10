import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os
chromedriver = '/Users/brstream/Downloads/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
display = Display(visible=0, size=(800, 600))
display.start()
br = webdriver.Chrome(chromedriver)
br.get('http://www.google.com/ncr')
q = br.find_element_by_name('q')
q.send_keys('Thich Nhat Hanh')
q.send_keys(Keys.RETURN)
results = br.find_elements_by_class_name('g')
blah = ['one thing', 'another']
print blah
print results
for result in results:
    print result.text
    import pdb; pdb.settrace()
    print 8 * '-'
