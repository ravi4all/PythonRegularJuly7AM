'''
1
12
123
1234
12345
'''
for i in range(5):
    for j in range(i+1):
        print(j+1, end='')
    print()

print('=' * 20)

'''
a
ab
abc
abcd
abcde
'''
for i in range(5):
    for j in range(i+1):
        print(chr(96+j+1), end='')
    print()

print('=' * 20)

'''
1
23
456
78910
'''
k = 0
for i in range(4):
    for j in range(i+1):
        k += 1
        print(k, end='')
    print()










