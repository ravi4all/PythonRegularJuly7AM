import io

try:
    file = open('file_1.txt','w')
    file.write("Hello World")
    data = file.read()
    print(data)
except io.UnsupportedOperation:
    print("Cannot read/write file...")
finally:
    file.close()
    print("It will always executed...")