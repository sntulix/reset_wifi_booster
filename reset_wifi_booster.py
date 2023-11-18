import base64
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

username = "admin"
password = "admin"
url = "192.168.3.2/wizard_setup.html"
auth_url = f"http://{username}:{password}@{url}"

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

driver.get(auth_url)

# 接続確認
driver.switch_to.default_content()
frame = driver.find_element_by_css_selector('iframe#wizard_iframe')
driver.switch_to.frame(frame)
button = driver.find_element_by_id('connect')
button.click()

driver.implicitly_wait(70)

# 再起動
driver.switch_to.default_content()
frame = driver.find_element_by_css_selector('iframe#wizard_iframe')
driver.switch_to.frame(frame)
form = driver.find_element_by_css_selector('td#connection_success_apply input')
form.click()

# 再起動待ち
driver.implicitly_wait(200)
driver.quit()
