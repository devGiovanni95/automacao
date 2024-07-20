#language: pt

Funcionalidade: Fluxo de registro

@busca
Cenário: realiza cadastro no site
    Dado que acesse a pagina web para um novo registro
    Quando clico no botão de Não é Cadastrado
    Entao navego para outra pagina
    E preencho o input nome
    E preencho o input data de aniversario
    E preencho o input email
    E preencho o input senha
    E preencho o input confirmação de senha
    E preencho o input tipo de conta
    Quando clico no botão criar conta
    Então devo visualizar a pagina login