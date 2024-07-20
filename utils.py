from browser import Browser

class Utils(Browser):
    def navegar(self, url):
        self.navegador.get(url)

    def current_url(self):
        return self.navegador.current_url