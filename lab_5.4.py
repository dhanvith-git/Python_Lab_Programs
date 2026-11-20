import pandas as pd
import matplotlib.pyplot as plt
# Read data from CSV file
data = pd.read_csv("sales.csv")
# Display the data
print(data)

# Line graph
plt.plot(data[data["Product"] == "Pen"]["Date"],
         data[data["Product"] == "Pen"]["Sales"],
         marker='o', label="Pen")

plt.plot(data[data["Product"] == "Book"]["Date"],
         data[data["Product"] == "Book"]["Sales"],
         marker='o', label="Book")

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Retail Sales Dashboard")
plt.legend()
plt.show()

# Bar chart
plt.bar(data["Product"], data["Sales"])
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.show()