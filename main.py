from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver') # replace with the actual path to chromedriver
driver.get('https://docs.google.com/forms/d/1FAIpQLSeZswQ7YW5mX0n_EZ8WDpxSdh7U1RVMSntmdpgd_3N47-UKrA/edit')
choice2 = driver.find_element_by_xpath('//*[@id="i38"]/div[3]/div')

choice2.click()
submit_button = driver.find_element_by_css_selector('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/spa')
submit_button.click()
