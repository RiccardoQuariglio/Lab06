from asyncio.windows_events import NULL

import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_top_vendite(self, e):
        self._view.txtResult.controls.clear()
        self._view.txtResult.controls.append(ft.Text("Di seguito le migliori 5 vendite per i parametri selezionati: \n"))
        anno = self._view.ddAnno.value
        brand = self._view.ddBrand.value
        retailer = self._view.ddRetailer.value
        if anno == "0" :
            anno = None
        if brand == "0" :
            brand = None
        if retailer == "0" :
            retailer = None

        topVendite = self._model.get_top_vendite(anno, brand, retailer)
        if len(topVendite) < 5:
            self._view.txtResult.controls.append(ft.Text(
                f"Ci sono meno di 5 vendite per questa ricerca {len(topVendite)}""."
            ))
        for vendita in topVendite:
            self._view.txtResult.controls.append(ft.Text(vendita.__str__()))

        self._view.update_page()

    def handle_analizza_vendite(self, e):
        self._view.txtResult.controls.clear()
        anno = self._view.ddAnno.value
        brand = self._view.ddBrand.value
        retailer = self._view.ddRetailer.value
        if anno == "0" :
            anno = None
        if brand == "0" :
            brand = None
        if retailer == "0" :
            retailer = None

        giroAffari, numeroVendite, numeroRetailers, numeroProdotti = self._model.get_analizza_vendite(anno, brand, retailer)
        self._view.txtResult.controls.append(ft.Text(
            f"Statistiche vendite: \n"
            f"Giro d'Affari: {giroAffari} \n"
            f"Numero vendite: {numeroVendite} \n"
            f"Numero retailers coinvolti: {numeroRetailers} \n"
            f"Numero prodotti coinvolti: {numeroProdotti}"
        ))
        self._view.update_page()




    def fill_ddAnno(self):
        self._view.ddAnno.options.append(ft.dropdown.Option(
            key= "0",
            text= "Nessun filtro"
        ))
        for anno in self._model.get_all_anni():
            self._view.ddAnno.options.append(ft.dropdown.Option(
                key= anno,
                text= anno
            ))

    def fill_ddBrand(self):
        self._view.ddBrand.options.append(ft.dropdown.Option(
            key="0",
            text="Nessun filtro"
        ))
        for brand in self._model.get_all_brands():
            self._view.ddBrand.options.append(ft.dropdown.Option(
                key= brand,
                text= brand
            ))

    def fill_ddRetailer(self):
        self._view.ddRetailer.options.append(ft.dropdown.Option(
            key="0",
            text="Nessun filtro"
        ))
        for retailer in self._model.get_all_retailers():
            self._view.ddRetailer.options.append(ft.dropdown.Option(
                key= retailer.codice,
                text= retailer.nome,
                data= retailer,
                on_click= self.read_retailer
            ))

    def read_retailer(self, e):
        self._retailer = e.control.data








