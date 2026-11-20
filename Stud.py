import pandas as pd
data={"Name":["Aman","Rohit"],"Age":[20,24]}
temp=pd.DataFrame(data)
temp.to_json("data.json")
print(temp)