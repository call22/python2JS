while(1):
    print("Please input a string:\n")
    str = input()
    l = len(str)
    flag  = 0
    for i in range(0,l):
        if(str[i] != str[l-1-i]):
            flag = 1
            break
    if(flag):
        print("This is not a palindrome string.\n")
    else:
        print("This is a palindrome string.\n")
