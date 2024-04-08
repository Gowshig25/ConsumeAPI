import csv
def write_to_csv(data):
    csv_file = "C:/JavaProgramming/ConsumingAPI/resources/csv/product_data.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product ID", "Product Name", "Product Quantity", "Product Price"])
        for product in data:
            writer.writerow([product['p_id'], product['p_name'], product['p_quantity'], product['p_price']])
    print(f"Data written to '{csv_file}'")