from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
import time


# from selenium.webdriver.common.keys import Keys

#setting environment for Automation
options = Options()
options._binary_location = ('C:\\Program Files (x86)\Google\Chrome Beta\Application\\chrome.exe')
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:/Users/TUKE-ANONYMOUS/Downloads/chromedriver_win32/chromedriver.exe')

# Accessing Facebook 
driver.get('https://facebook.com')
driver.maximize_window() # Maximizing window
print('Already accessing Facebook waiting for signing in')

# Login to the Facebook account

# Prompting the User for his username and password
time.sleep(5)
user_email = input('Username  or email Please: ')
user_password = input('Password please: ')

# getting email and password 
email = driver.find_element_by_xpath('//*[@id="email"]').send_keys(user_email)
password = driver.find_element_by_id('pass').send_keys(user_password)

# Submitting Credentials
login = driver.find_element_by_xpath("//*[@id='u_0_b']").click()
time.sleep(5)
print('Username and email submitted successfully, if the credentials are valid, you will be logged in')

# Finding friends
print("If notification permision pops up? please select your choice to continue")
time.sleep(60)
friends_page = driver.find_element_by_id("findFriendsNav").click()
print('Redirecting to Friends page')
driver.execute_script("window.scrollBy(0,500)","")