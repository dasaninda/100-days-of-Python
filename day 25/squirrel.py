#WITHOUT PANDAS (code) not really organized
#  import csv

# with open ("weather.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

# print(data["temp"].mean()) #mean of the data
# print(data["temp"].max())#max of the data


import pandas

data = pandas.read_csv("Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count  = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count  = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"], 
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")