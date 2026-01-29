from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time

class NetworkAutomation:
    def run(self):
        self.open_network_connections()
        self.open_properties()
        self.disabling_network_sharing()

    def open_network_connections(self):
        Application(backend="uia").start("control.exe ncpa.cpl")
        time.sleep(2)

        self.window = Desktop(backend="uia").window(title="Conexões de Rede")
        self.window.wait("visible", timeout=15)
        self.window.set_focus()

    def open_properties(self):
        # o container real dos adaptadores
        listview = self.window.child_window(control_type="List")
        listview.wait("visible", timeout=10)

        # pega o PRIMEIRO adaptador
        item = listview.children()[3]
        item.select()
        time.sleep(0.5)

        # menu de contexto
        item.right_click_input()
        time.sleep(0.5)

        # Propriedades
        context_menu = Desktop(backend="uia").window(control_type="Menu")
        context_menu.wait("visible", timeout=5)

        context_menu.child_window(
            title="Propriedades",
            control_type="MenuItem"
        ).click_input()

    def disabling_network_sharing(self):
        props = Desktop(backend="uia").window(title_re="Propriedades")
        props.wait("visible", timeout=10)
        props.set_focus()

        # ir para aba Compartilhamento
        for _ in range(2):
            send_keys("^{TAB}")
            time.sleep(0.3)

        # marcar/desmarcar checkbox
        send_keys("{SPACE}")
        time.sleep(0.3)

        # confirmar
        send_keys("{ENTER}")

if __name__ == "__main__":
    NetworkAutomation().run()
