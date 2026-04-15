from database.DAO import DAO


class Model:
    def __init__(self):
        pass



    def get_all_anni(self):
        return DAO.get_all_anni()

    def get_all_brands(self):
        return DAO.get_all_brands()

    def get_all_retailers(self):
        return DAO.get_all_retailers()

    def get_top_vendite(self, anno, brand, retailer):
        topVendite = DAO.get_top_vendite(anno, brand, retailer)
        topVendite.sort(key=lambda v:v.ricavo, reverse=True)
        topCinqueVendite = topVendite[:5]
        return topCinqueVendite

    def get_analizza_vendite(self, anno, brand, retailer):
        giroAffari, numeroVendite, numeroRetailers, numeroProdotti = DAO.get_analizza_vendite(anno, brand, retailer)
        return giroAffari, numeroVendite, numeroRetailers, numeroProdotti
