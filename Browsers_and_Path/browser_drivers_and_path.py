from selenium import webdriver

# Option 1: NOT recommended because code not portable
driver = webdriver.Chrome(executable_path="/Users/yanichik/Downloads/chromedriver")

# opens window to google.com
driver.get("https://google.com")
