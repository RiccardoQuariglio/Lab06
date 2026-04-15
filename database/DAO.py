from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendita import Vendita


class DAO():

    @staticmethod
    def get_all_anni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """ select year(Date) as anno
                    from go_daily_sales
                    group by year(Date)"""

        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_all_brands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select Product_brand as brand
                    from go_products
                    group by Product_brand"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row["brand"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_all_retailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select Retailer_code as codice, Retailer_name as nome, type as tipo, Country as nazione
                    from go_retailers"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_top_vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select Retailers.Retailer_code as codiceRetailer, Prodotti.Product_number as numeroProdotto,
	                Vendite.Date as data, (Vendite.Quantity * Vendite.Unit_sale_price)  as ricavo
                    from go_products as Prodotti, go_retailers as Retailers, go_daily_sales as Vendite
                    where Prodotti.Product_number = Vendite.Product_number 
                  and Retailers.Retailer_code = Vendite.Retailer_code
                  and year(Vendite.Date) = COALESCE(%s, year(Vendite.Date))
                  and Prodotti.Product_brand = COALESCE(%s, Prodotti.Product_brand)
                  and Retailers.Retailer_code = COALESCE(%s, Retailers.Retailer_code)"""
        res = []
        cursor.execute(query, (anno, brand, retailer))
        for row in cursor:
            res.append(Vendita(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def get_analizza_vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = """ select sum(Quantity * Unit_sale_price) as giroAffari,
                   count(*) as numeroVendite,
                   count(distinct Retailer_code) as numeroRetailers,
                   count(distinct Prodotti.Product_number) as numeroProdotti
	   
                    from go_products as Prodotti, go_daily_sales as Vendite
                    where Prodotti.Product_number = Vendite.Product_number 
                    and year(Vendite.Date) = COALESCE(%s, year(Vendite.Date))
                    and Prodotti.Product_brand = COALESCE(%s, Prodotti.Product_brand)
                    and Retailer_code = COALESCE(%s, Retailer_code)"""
        cursor.execute(query, (anno, brand, retailer))
        row = cursor.fetchone()
        giroAffari = row["giroAffari"]
        numeroVendite = row["numeroVendite"]
        numeroRetailers = row["numeroRetailers"]
        numeroProdotti = row["numeroProdotti"]
        return giroAffari, numeroVendite, numeroRetailers, numeroProdotti



