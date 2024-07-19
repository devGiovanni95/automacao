from behave import given, when, then
#definindo uma classe pra reaproveitar codigo
from utils import Utils
from time import sleep
navegar = Utils().navegar()

@given(u'que acesse a pagina web')
def step_impl(context):
    navegar('https://meajudaae.onrender.com/')
    raise NotImplementedError(u'STEP: Given que acesse a pagina web')


@given(u'preencho o imput de email')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given preencho o imput de email')


@given(u'preencho o imput de senha')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given preencho o imput de senha')


@when(u'clico no botão de entrar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico no botão de entrar')


@then(u'devo visualizar a pagina home')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo visualizar a pagina home')
