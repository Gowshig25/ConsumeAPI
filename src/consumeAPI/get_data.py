import requests

from src.fileHandling.insert_product import write_to_csv
from src.fileHandling.insert_to_excel import write_in_excel


def get_data_from_API():
    getURL="http://localhost:8080/OnlineShoppingUsingREST/api/products/getProduct"
    response=requests.get(getURL)
    if response.status_code ==200:
        products=response.json()
        write_to_csv(products)
        write_in_excel(products)
        return products
    else:
        print("The Server is not working Properly")

