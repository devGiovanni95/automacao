from behave import given, when, then
#definindo uma classe pra reaproveitar codigo
from utils import Utils
from time import sleep
from pages.header_page_login import HeaderPageLogin

browser = Utils()
header_page = HeaderPageLogin()

@given(u'que acesse a pagina web')
def step_impl(context):
    browser.navegar('https://meajudaae.onrender.com')
    sleep(7)


@given(u'preencho o input de email')
def step_impl(context):
    header_page.preenche_input_email('giovanni.santos9@fatec.sp.gov.br')
    sleep(2)

@given(u'preencho o input de senha')
def step_impl(context):
    header_page.preenche_input_password('12345678')
    sleep(2)

@when(u'clico no botão de entrar')
def step_impl(context):
    header_page.clica_botao_entrar()
    sleep(10)

@then(u'devo visualizar a pagina home')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then devo visualizar a pagina home')
    expected_url = 'https://meajudaae.onrender.com/home'  # URL esperada da página home após o login
    current_url = browser.current_url()  # Obtém a URL atual do navegador

    print(f"URL atual: {current_url}")
    print(f"URL esperada: {expected_url}")

    assert current_url == expected_url, f"A URL atual '{current_url}' é diferente da esperada '{expected_url}'"
