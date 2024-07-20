from browser import Browser

class HeaderPageLogin(Browser):
    def preenche_input_email(self, texto):
        self.navegador.find_element('xpath', '//*[@id="email"]').send_keys(texto)

    def preenche_input_password(self, texto):
        self.navegador.find_element('xpath', '//*[@id="fieldPassword"]').send_keys(texto)

    def clica_botao_entrar(self):
        self.navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[4]/button[1]').click()
