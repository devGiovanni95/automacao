from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options


# class Browser:
#     # service = FirefoxService()
#     navegador = webdriver.Firefox()

# class Browser:
#     servico = Service(ChromeDriverManager().install())
#     navegador = webdriver.Chrome(service=servico)

class Browser:
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)