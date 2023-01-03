from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from fake_useragent import UserAgent
import time
import os

useragent = UserAgent()
options = webdriver.FirefoxOptions()

#options.set_preference('general.useragent.override', 'Hiiii')


url = 'https://br.pinterest.com/Revain_Brazil/'
install_dir = "/snap/firefox/current/usr/lib/firefox"
driver_loc = os.path.join(install_dir, "geckodriver")
binary_loc = os.path.join(install_dir, "firefox")

service = FirefoxService(driver_loc)
opts = webdriver.FirefoxOptions()
opts.binary_location = binary_loc
opts.set_preference('general.useragent.override', useragent.random)

driver = webdriver.Firefox(service=service, options=opts)


try:
    driver.get(url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
