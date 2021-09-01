file = open('img.jpg', mode='rb')
data = file.read()
# print(data)
file.close()

file = open('img_2.jpg', mode='wb')
file.write(data)
file.close()