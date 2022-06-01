from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Option 1: NOT recommended because code not portable
# ALSO: will get WARNING:
# DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# driver = webdriver.Chrome(executable_path="/Users/yanichik/Downloads/chromedriver")

# Option 1a with selenium 4: using service object per warning from option 1 above
# service_object = Service(executable_path="/Users/yanichik/Downloads/chromedriver")

# Option 2: add executable to system path
driver = webdriver.Chrome()

# opens window to google.com
driver.get("https://google.com")
