import csv

# data = [
#     ["first_name", "last_name"],
#     ["sachin","tendulkar"],
#     ["virat","kohli"],
#     ["rohit","sharma"],
#     ["ms","dhoni"]
# ]
#
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for row in data:
#         writer.writerow(row)

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
