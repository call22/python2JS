print('Please input a string:')
str = input()
l = len(str)
flag  = 0
for i in range(0,l):
    if(str[i] != str[l-1-i]):
        flag = 1
        break
if(flag):
    print('False')
else:
    print('True')
