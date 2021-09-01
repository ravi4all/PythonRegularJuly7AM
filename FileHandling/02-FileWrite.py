# file = open('file_2.txt', mode='w')
# # data = "Hello this is python"
# data = "This is File Handling demo..."
# file.write(data)
# file.close()

# file = open('file_2.txt', mode='a')
# data = "\nPython Programming is easy to learn"
# file.write(data)
# file.close()

file = open('file_2.txt', mode='x')
data = "\nPython Programming is easy to learn"
file.write(data)
file.close()