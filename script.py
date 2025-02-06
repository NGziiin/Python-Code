from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time


#configuração selenium
driver_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
login_url = 'https://cinenetcb.sgp.net.br/accounts/central/login'
cnpj_cpf = '05.906.273/0001-13'

data = datetime.now().strftime('%d')

limite = 28

if int(data) <= limite:

    options = webdriver.EdgeOptions()
    options.binary_location = driver_path
    driver = webdriver.Edge(options = options)
    driver.get(login_url)
    driver.find_element(By.ID, "cpfcnpj").send_keys(cnpj_cpf)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(86400)
    if driver in None:
        driver.quit()
else:
    print('Data excedida')