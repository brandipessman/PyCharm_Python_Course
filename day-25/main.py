# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
import numpy

# data = pandas.read_csv("weather_data.csv")
# # print(type(data["temp"])) # series
# # print(type(data)) # dataframe
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get columns
# print(data["condition"])
# print(data.condition)
#
# # get row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # specific value
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = squirrel_data["Primary Fur Color"].unique()
squirrels = []
for color in colors:
    squirrels.append(len(squirrel_data[squirrel_data["Primary Fur Color"] == color]))
data_dict = {
    "Fur Color": colors,
    "Count": squirrels
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
