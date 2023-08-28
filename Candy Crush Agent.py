from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


url = "https://www.cooljuegos.com/juego-en-linea/candy-crush/"

driver = webdriver.Chrome()
driver.get(url)


driver.maximize_window()


input("In order to shut down the browser press enter...")

driver.quit() 