import os
import subprocess
import sys

try:
    import selenium
    from selenium import webdriver
except ImportError:
    subprocess.call([sys.executable, '-m', 'pip', 'install', selenium])

from functions import main

download_path = os.getcwd()

try:
    options = webdriver.ChromeOptions()
    options.headless = True
    prefs = {'download.default_directory': download_path}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service_log_path='nul')

except:
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", download_path)
    options.set_preference('devtools.jsonview.enabled', False)
    driver = webdriver.Firefox(options=options, service_log_path='nul')

if __name__ == '__main__':
    main(driver)
    driver.close()
    driver.quit()
    os.system('pause')
