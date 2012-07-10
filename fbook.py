import selenium_browser
from selenium_browser import browser
from selenium.webdriver.common.keys import Keys

from secret import FACEBOOK_USERNAME
from secret import FACEBOOK_PASSWORD
from secret import FACEBOOK_PAGE
from secret import FACEBOOK_SELECTOR

def fbook_get(url, selector):
    browser.get(url)
    e = browser.find_element_by_name('email')
    e.send_keys(FACEBOOK_USERNAME)
    p = browser.find_element_by_name('pass')
    p.send_keys(FACEBOOK_PASSWORD)
    p.send_keys(Keys.RETURN)
    results = []
    results = browser.find_elements_by_css_selector(selector)
    return results

results = fbook_get(FACEBOOK_PAGE, FACEBOOK_SELECTOR)

for result in results:
    print(result.text)
    print(8 * '-')
