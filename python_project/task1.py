import pandas as pd

# Create dataset
data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "Order_Date": [
        "2026-05-01", "2026-05-02", "2026-05-03", "2026-05-04", "2026-05-05",
        "2026-05-06", "2026-05-07", "2026-05-08", "2026-05-09", "2026-05-10"
    ],
    "Customer_Name": [
        "Rahul Sharma", "Priya Verma", "Amit Kumar", "Sneha Patil",
        "Rohan Das", "Kiran Rao", "Anjali Singh", "Vikram Joshi",
        "Pooja Nair", "Arjun Mehta"
    ],
    "City": [
        "Bengaluru", "Mumbai", "Delhi", "Pune", "Hyderabad",
        "Chennai", "Kolkata", "Ahmedabad", "Bengaluru", "Delhi"
    ],
    "Product_Name": [
        "Laptop", "Headphones", "Smartphone", "Keyboard", "Monitor",
        "Mouse", "Tablet", "Printer", "Webcam", "External HDD"
    ],
    "Category": [
        "Electronics", "Accessories", "Electronics", "Accessories",
        "Electronics", "Accessories", "Electronics", "Office",
        "Accessories", "Storage"
    ],
    "Quantity_Sold": [2, 5, 3, 4, 2, 10, 3, 1, 6, 4],
    "Price_Per_Unit": [55000, 2500, 22000, 1800, 15000, 700, 18000, 12000, 3200, 4500],
    "Revenue": [110000, 12500, 66000, 7200, 30000, 7000, 54000, 12000, 19200, 18000],
    "Profit": [18000, 3500, 12000, 2000, 5000, 1800, 9500, 2500, 4200, 3800],
    "Order_Status": [
        "Delivered", "Delivered", "Delivered", "Pending", "Delivered",
        "Delivered", "Returned", "Delivered", "Delivered", "Pending"
    ]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)

# Save to Excel file
df.to_excel("sales_data.xlsx", index=False)

print("Excel file 'sales_data.xlsx' created successfully.")