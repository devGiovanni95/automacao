# from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service as FirefoxService
# geckodriver_path = '/usr/local/bin/geckodriver'
#
# # Configuração do serviço do Firefox
# firefox_service = FirefoxService(executable_path=geckodriver_path)
#
# navegador = webdriver.Firefox(service=firefox_service)
# # browser.get('http://selenium.dev/')
# from time import sleep
#
# # servico = Service(ChromeDriverManager().install())
# # navegador = webdriver.Firefox()
#
# #abrindo o navegador
# # navegador.maximize_window()
#
# # #acessando url

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import logging

logging.basicConfig(level=logging.DEBUG)

# Especifique o caminho para o GeckoDriver
geckodriver_path = '/usr/local/bin/geckodriver'
firefox_options = FirefoxOptions()
firefox_options.headless = False  # Altere para True se desejar executar sem abrir a janela do navegador

# Configuração do serviço do Firefox
firefox_service = FirefoxService(executable_path=geckodriver_path)

# Inicializando o navegador Firefox
navegador = webdriver.Firefox(service=firefox_service,options=firefox_options)

# Agora você pode continuar com seu código Selenium normalmente
navegador.get('https://meajudaae.onrender.com/')

# Fechando o navegador ao finalizar
# navegador.quit()

def login():
    sleep(10)
    # procurando e passando dados
    navegador.find_element('xpath','//*[@id="email"]').send_keys('giovanni.santos9@fatec.sp.gov.br')
    sleep(1)
    navegador.find_element('xpath','//*[@id="fieldPassword"]').send_keys('12345678')
    sleep(1)
    navegador.find_element('xpath','//*[@id="root"]/div/div/div/div[4]/button[1]').click()
    sleep(1)

def register_student():
    sleep(2)
    # procurando e passando dados
    navegador.find_element('xpath','//*[@id="root"]/div/div/div/div[4]/button[2]').click()
    sleep(1)
    navegador.find_element('xpath','//*[@id="name"]').send_keys('Giovanni Santos')
    sleep(1)
    navegador.find_element('xpath','//*[@id="birthDate"]').send_keys('01/01/2000')
    sleep(1)
    navegador.find_element('xpath','//*[@id="email"]').send_keys('giovanni.santos9@fatec.sp.gov.br')
    sleep(1)
    navegador.find_element('xpath','//*[@id="password"]').send_keys('12345678')
    sleep(1)
    navegador.find_element('xpath','//*[@id="confirm_password"]').send_keys('12345678')
    sleep(1)
    navegador.find_element('xpath','//*[@id="accont_type"]').send_keys('Estudante')
    sleep(2)
    navegador.find_element('xpath','//*[@id="root"]/div/div/div/div[7]/button').click()
    sleep(1)

# navegador.get('https://meajudaae.onrender.com/')



register_student()
sleep(200)