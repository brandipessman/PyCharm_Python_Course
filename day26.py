# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)
#
# name = "Brandi"
# letters_list = [letter for letter in name]
# print(letters_list)
#
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
# student_scores = {
#     student:random.randint(1,100) for student in names
# }
# print(student_scores)
# passed_students = {
#     student:score for (student, score) in student_scores.items() if score > 60
# }
# print(passed_students)

# numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)
# result = [num for num in numbers if num%2 == 0]
# print(result)


# import pandas
# with open("file1.txt") as file1:
#     file1 = file1.readlines()
#     file1_strip = [num.strip() for num in file1]
#
# with open("file2.txt") as file2:
#     file2 = file2.readlines()
#     file2_strip = [num.strip() for num in file2]
#
# result = [int(item) for item in file1_strip if item in file2_strip]
#
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sent_list = sentence.split()
# result = {
#     word:len(word) for word in sent_list
# }
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {
#     day: temp*1.8 + 32 for (day, temp) in weather_c.items()
# }
# print(weather_f)

