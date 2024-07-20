from browser import Browser

class HeaderPageRegister(Browser):

    def preenche_input_name(self, texto):
        self.navegador.find_element('xpath', '//*[@id="name"]').send_keys(texto)

    def preenche_input_date_birth(self, texto):
        self.navegador.find_element('xpath', '//*[@id="birthDate"]').send_keys(texto)

    def preenche_input_email(self, texto):
        self.navegador.find_element('xpath', '//*[@id="email"]').send_keys(texto)

    def preenche_input_password(self, texto):
        self.navegador.find_element('xpath', '//*[@id="password"]').send_keys(texto)

    def preenche_input_confirm_password(self, texto):
        self.navegador.find_element('xpath', '//*[@id="confirm_password"]').send_keys(texto)

    def preenche_input_type_account(self, texto):
        self.navegador.find_element('xpath', '//*[@id="accont_type"]').send_keys(texto)

    def clica_button_dont_registed(self):
        self.navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[4]/button[2]').click()

    def clica_button_new_account(self):
        self.navegador.find_element('xpath', '//*[@id="root"]/div/div/div/div[7]/button').click()
