#language: pt

Funcionalidade: Fluxo de login

@busca
Cenário: realiza login no site
    Dado que acesse a pagina web
    E preencho o imput de email
    E preencho o imput de senha
    Quando clico no botão de entrar
    Então devo visualizar a pagina home
    