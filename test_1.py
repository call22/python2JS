def parse(expr,queue,queueType):
    e_len = len(expr)
    x = 0
    num_flag = 0
    last = ''
    for i in range(0,e_len):
        if(expr[i] >= '0' and expr <= '9'):
            if(num_flag == 0):
                num_flag = 1
                x = int(expr[i])
            else:
                x = x * 10 + int(expr[i])
            if(i == e_len-1):
                if(num_flag == 1):
                    queue.append(x)
                    queueType.append('n')
        else:
            if(num_flag == 1):
                queue.append(x)
                queueType.append('n')
                num_flag = 0
                if(last == 'rb' or last == 'n'):
                    print('Illegal input!')
                    return False
                else:
                    last = 'n'
            if(expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/'):
                queue.append(expr[i])
                queueType.append('t')
                if(last == 't' or last == 'lb'):
                    print('Illegal input!')
                    return False
                else:
                    last = 't'
            elif(expr[i] == '('):
                queue.append(expr[i])
                queueType.append('lb')
                if (last == 'n' or last == 'rb'):
                    print('Illegal input!')
                    return False
                else:
                    last = 'lb'
            elif(expr[i] == ')'):
                queue.append(expr[i])
                queueType.append('rb')
                if (last == 't' or last == 'lb'):
                    print('Illegal input!')
                    return False
                else:
                    last = 'rb'
            elif(expr[i] != ' ' and expr[i] != '\n'):
                print('Illegal input!')
                return False
    return True

def priority(x):
    if(x == '('):
        return 0
    elif(x == '+' or x == '-'):
        return 1
    elif(x == '*' or x == '/'):
        return 2
    else:
        return None

def calculate(queue,queueType):
    q_len = len(queue)
    opStack = []
    proStack = []
    proTopNum = 0
    for i in range(0,q_len):
        if(queueType[i] == 'n'):
            proStack.append(queue[i])
        elif(queueType[i] == 'lb'):
            opStack.append(queue[i])
        elif (queueType[i] == 'rb'):
            while(len(opStack) != 0 and opStack[len(opStack)-1] != '('):
                proStack.append(opStack.pop())
            if(len(opStack) == 0):
                return None
            else:
                opStack.pop()
        elif(queueType[i] == 't'):
            while(len(opStack) != 0 and priority(opStack[len(opStack)-1]) >= priority(queue[i])):
                proStack.append(opStack.pop())
            opStack.append(queue[i])
    while(len(opStack) != 0):
         y = opStack.pop()
         if(y != '+' and y != '-' and y != '*' and y != '/'):
             return None
         proStack.append(y)
    pro_len = len(proStack)
    calStack = []
    for i in range(0,pro_len):
        if(proStack[i] == '+'):
            if(len(calStack) < 2):
                return None
            else:
                z = calStack.pop() + calStack.pop()
                calStack.append(z)
        elif (proStack[i] == '-'):
            if (len(calStack) < 2):
                return None
            else:
                c1 = calStack.pop()
                c2 = calStack.pop()
                z = c2 - c1
                calStack.append(z)
        elif (proStack[i] == '*'):
            if (len(calStack) < 2):
                return None
            else:
                z = calStack.pop() * calStack.pop()
                calStack.append(z)
        elif (proStack[i] == '/'):
            if (len(calStack) < 2):
                return None
            else:
                c1 = calStack.pop()
                c2 = calStack.pop()
                if(c1 == 0):
                    return None
                z = c2 / c1
                calStack.append(z)
        else:
            calStack.append(proStack[i])
    return calStack[0]

expr = input()
queue = []
queueType = []
if(parse(expr,queue,queueType)):
    tmp = calculate(queue,queueType)
    if(tmp != None):
        print(tmp)
    else:
        print('Error in calculate the formula.')
else:
    print('Error in parse the formula.')
