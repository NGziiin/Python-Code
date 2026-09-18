from playwright.sync_api import sync_playwright

class system:
    def __init__(self):
        self.WebInfo()
        self.manipulandoWeb()


    def WebInfo(self):
        self.link = "https://cinenetcb.sgp.net.br/accounts/central/login"
        #self.user = input("digite seu nome para login: ")

    def manipulandoWeb(self):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(channel="msedge")
            self.page = self.browser.new_page()
            self.page.goto(self.link)
            print(self.page.title())
            self.browser.close()


if __name__ == "__main__":
    system()