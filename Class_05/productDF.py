import pandas

# Data for products
name = ["Laptop", "Sofa", "T-shirt", "Apple", "Novel"]
category = ["Electronics", "Furniture", "Clothing", "Groceries", "Books"]
price = [1500, 300, 250, 200, 100]
brand = ["Dell", "Ikea", "Nike", "Fuji", "Penguin"]

# Creating the DataFrame
product_data = {"Name": name, "Category": category, "Price": price, "Brand": brand}

# Converting data to DataFrame
product_table = pandas.DataFrame(product_data)
print("Display the DataFrame ....")
print(product_table)
print("\n")
print("Add Stock Column ....")
product_table["Stock"] = "Available"
print("\n")
print("These Product which price is greater tha 1000 ....")
print(product_table[product_table["Price"] >= 1000])
print("\n")
print("Print Clothing Product ....")
print(product_table[product_table["Category"] == "Clothing"])
print("\n")
print("Print Dell Brand which price is greater than 1400 ....")
print(
    product_table[(product_table["Brand"] == "Dell") & (product_table["Price"] >= 1400)]
)
# DataFrame convert to CSV file
product_table.to_csv("productData.csv", index=False)
