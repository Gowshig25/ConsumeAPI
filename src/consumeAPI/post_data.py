import requests
def post_data(data):
    postURL='http://localhost:8080/OnlineShoppingUsingREST/api/products/postProduct'
    response=requests.post(postURL,json=data)
    if response.status_code==201:
        print('The data is uploaded successfully')
    else:
        print("The data is not uploaded")
def user_input():
    data={
        "p_id":int(input("Enter the Product ID")),
        "p_name":input("Enter the name of the product"),
        "p_price":float(input("Enter the price")),
        "p_quantity":int(input("Enter the quantity of the product"))
    }
    post_data(data)