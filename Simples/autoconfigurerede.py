from pywinauto.application import Application
from pywinauto.keyboard import send_keys


class NetworkAutomation:
    def __init__(self):
        self.app = None
        self.window = None

    def run(self):
        self.open_network_connections()
        self.open_adapter_properties()
        self.remove_network_sharing()

    def open_network_connections(self):
        """
        Abre o painel 'Conexões de Rede' (ncpa.cpl)
        """
        self.app = Application(backend="uia").start("control.exe ncpa.cpl")
        self.window = self.app.window(title_re=".*Conexões de Rede.*")
        self.window.wait("visible ready")
        self.window.set_focus()

    def open_adapter_properties(self):
        """
        Abre as propriedades do adaptador selecionado
        (assume que existe apenas um adaptador principal)
        """
        adapter = self.window.child_window(
            control_type="ListItem"
        )

        adapter.wait("visible enabled")
        adapter.click_input(double=True)

    def remove_network_sharing(self):
        """
        Desmarca o compartilhamento de rede
        """
        properties = self.app.window(title_re=".*Propriedades.*")
        properties.wait("visible ready")
        properties.set_focus()

        # Abre a aba "Compartilhamento"
        tab = properties.child_window(title="Compartilhamento", control_type="TabItem")
        tab.select()

        # Desmarca a checkbox
        checkbox = properties.child_window(
            title_re=".*Permitir que outros usuários.*",
            control_type="CheckBox"
        )

        if checkbox.get_toggle_state():
            checkbox.toggle()

        # Confirma
        ok_button = properties.child_window(title="OK", control_type="Button")
        ok_button.click_input()


if __name__ == "__main__":
    NetworkAutomation().run()
