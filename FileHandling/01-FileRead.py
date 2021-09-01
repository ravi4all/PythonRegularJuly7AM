file = open('file_1.txt', mode='r')
# data = file.read()

# data = file.read(10)

# data = file.readlines()

# data = file.readline()

file.seek(20)
data = file.read(20)
print(data)
file.close()