import pandas as pd
temp = pd.read_csv("Stud.csv")
print(temp)
data = {
    "Name": ["Rahul", "Amit"],
    "Age": [20, 21]
}
df = pd.DataFrame(data)
print(df)
