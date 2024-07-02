import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # button for the "hello" reply
        self._title = ft.Text("Genes Small", color="blue", size=24)
        self._page.controls.append(self._title)


        # row1
        self._btn_grafo = ft.ElevatedButton(text="Grafo", on_click=self._controller.handleGrafo)
        row1 = ft.Row([ft.Container(self._btn_grafo, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self.txt_result1 = ft.ListView(expand=1, spacing=10, padding=20)
        self._page.controls.append(self.txt_result1)

        # row2
        self._txtInSoglia = ft.TextField(label="Soglia", disabled=True)
        self._btn_conta_archi = ft.ElevatedButton(text="Cerca itinerario", on_click=self._controller.handleContaArchi, disabled=True)
        row2 = ft.Row([ft.Container(self._txtInSoglia, width=300), ft.Container(self._btn_conta_archi, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20)
        self._page.controls.append(self.txt_result2)

        # row3
        self._btn_cammino = ft.ElevatedButton(text="Cerca cammino", on_click=self._controller.handleCammino, disabled=True)
        row3 = ft.Row([ft.Container(self._btn_cammino, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self.txt_result3 = ft.ListView(expand=1, spacing=10, padding=20)
        self._page.controls.append(self.txt_result3)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
