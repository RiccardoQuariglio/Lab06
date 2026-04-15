import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddAnno = None
        self.ddBrand = None
        self.ddRetailer = None
        self.btnTopVendite = None
        self.btnAnalizzaVendite = None
        self.txtResult = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self.ddAnno = ft.Dropdown(label= "anno")
        self._controller.fill_ddAnno()
        self.ddBrand = ft.Dropdown(label="brand")
        self._controller.fill_ddBrand()
        self.ddRetailer = ft.Dropdown(label="retailer")
        self._controller.fill_ddRetailer()
        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer],
                      alignment=ft.MainAxisAlignment.CENTER)

        # button for the "hello" reply
        self.btnTopVendite = ft.ElevatedButton(text= "Top vendite",
                                               on_click= self._controller.handle_top_vendite)
        self.btnAnalizzaVendite = ft.ElevatedButton(text= "Analizza vendite",
                                                    on_click= self._controller.handle_analizza_vendite)


        row2 = ft.Row([self.btnTopVendite, self.btnAnalizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2)

        # List View where the reply is printed
        self.txtResult = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtResult)
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
