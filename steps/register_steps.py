from behave import given, when, then
#definindo uma classe pra reaproveitar codigo
from utils import Utils
from time import sleep
from pages.header_page_register import HeaderPageRegister

browser = Utils()
header_page = HeaderPageRegister()


@given(u'que acesse a pagina web para um novo registro')
def step_impl(context):
    browser.navegar('https://meajudaae.onrender.com')
    sleep(7)

@when(u'clico no botão de Não é Cadastrado')
def step_impl(context):
    header_page.clica_button_dont_registed()
    sleep(1)

@then(u'navego para outra pagina')
def step_impl(context):
    expected_url = 'https://meajudaae.onrender.com/register'  # URL esperada da página home após o login
    current_url = browser.current_url()  # Obtém a URL atual do navegador
    print(f"URL atual: {current_url}")
    print(f"URL esperada: {expected_url}")
    assert current_url == expected_url, f"A URL atual '{current_url}' é diferente da esperada '{expected_url}'"
    sleep(1)

@then(u'preencho o input nome')
def step_impl(context):
    header_page.preenche_input_name('Giovanni')
    sleep(1)

@then(u'preencho o input data de aniversario')
def step_impl(context):
    header_page.preenche_input_date_birth('20/07/2000')
    sleep(1)

@then(u'preencho o input email')
def step_impl(context):
    header_page.preenche_input_email('giovanni.santos9@fatec.sp.gov.br')
    sleep(1)

@then(u'preencho o input senha')
def step_impl(context):
    header_page.preenche_input_password('12345678')
    sleep(1)

@then(u'preencho o input confirmação de senha')
def step_impl(context):
    header_page.preenche_input_confirm_password('12345678')
    sleep(1)

@then(u'preencho o input tipo de conta')
def step_impl(context):
    header_page.preenche_input_type_account('Estudante')
    sleep(1)

@when(u'clico no botão criar conta')
def step_impl(context):
    header_page.clica_button_new_account()
    sleep(3)

@then(u'devo visualizar a pagina login')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then devo visualizar a pagina home')
    expected_url = 'https://meajudaae.onrender.com'  # URL esperada da página home após o login
    current_url = browser.current_url()  # Obtém a URL atual do navegador
    print(f"URL atual: {current_url}")
    print(f"URL esperada: {expected_url}")
    assert current_url == expected_url, f"A URL atual '{current_url}' é diferente da esperada '{expected_url}'"

