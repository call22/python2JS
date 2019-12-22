function parse (expr,queue,queueType){
    e_len=expr.length
    if(e_len===0){
        return false
    }
    x=0
    num_flag=0
    last=''
    for(i = 0; i < e_len; i++){
        if(expr[i] >= '0' && expr <= '9'){
            if(num_flag===0){
                num_flag=1
                x=parseInt(expr[i])
            }
            else{
                x=x * 10 + parseInt(expr[i])
            }
            if(i===e_len - 1){
                if(num_flag===1){
                    queue.push(x)
                    queueType.push('n')
                }
            }
        }
        else{
            if(num_flag===1){
                queue.push(x)
                queueType.push('n')
                num_flag=0
                if(last==='rb' || last==='n'){
                    console.log('Illegal input!')
                    return false
                }
                else{
                    last='n'
                }
            }
            if(expr[i]==='+' || expr[i]==='-' || expr[i]==='*' || expr[i]==='/'){
                queue.push(expr[i])
                queueType.push('t')
                if(last==='t' || last==='lb'){
                    console.log('Illegal input!')
                    return false
                }
                else{
                    last='t'
                }
            }
            else if(expr[i]==='('){
                queue.push(expr[i])
                queueType.push('lb')
                if(last==='n' || last==='rb'){
                    console.log('Illegal input!')
                    return false
                }
                else{
                    last='lb'
                }
            }
            else if(expr[i]===')'){
                queue.push(expr[i])
                queueType.push('rb')
                if(last==='t' || last==='lb'){
                    console.log('Illegal input!')
                    return false
                }
                else{
                    last='rb'
                }
            }
            else if(expr[i]!==' ' && expr[i]!=='\n'){
                console.log('Illegal input!')
                return false
            }
        }
    }
    return true
}
function priority (x){
    return ((x==='(') ? (0) : ((x==='+' || x==='-') ? (1) : ((x==='*' || x==='/') ? (2) : undefined)))
}
function calculate (queue,queueType){
    q_len=queue.length
    opStack=[]
    proStack=[]
    proTopNum=0
    for(i = 0; i < q_len; i++){
        if(queueType[i]==='n'){
            proStack.push(queue[i])
        }
        else if(queueType[i]==='lb'){
            opStack.push(queue[i])
        }
        else if(queueType[i]==='rb'){
            while(opStack.length!==0 && opStack[opStack.length - 1]!=='('){
                proStack.push(opStack.pop())
            }
            if(opStack.length===0){
                return undefined
            }
            else{
                opStack.pop()
            }
        }
        else if(queueType[i]==='t'){
            while(opStack.length!==0 && priority(opStack[opStack.length - 1]) >= priority(queue[i])){
                proStack.push(opStack.pop())
            }
            opStack.push(queue[i])
        }
    }
    while(opStack.length!==0){
         y=opStack.pop()
         if(y!=='+' && y!=='-' && y!=='*' && y!=='/'){
             return undefined
         }
         proStack.push(y)
    }
    pro_len=proStack.length
    calStack=[]
    for(i = 0; i < pro_len; i++){
        if(proStack[i]==='+'){
            if(calStack.length < 2){
                return undefined
            }
            else{
                z=calStack.pop() + calStack.pop()
                calStack.push(z)
            }
        }
        else if(proStack[i]==='-'){
            if(calStack.length < 2){
                return undefined
            }
            else{
                c1=calStack.pop()
                c2=calStack.pop()
                z=c2 - c1
                calStack.push(z)
            }
        }
        else if(proStack[i]==='*'){
            if(calStack.length < 2){
                return undefined
            }
            else{
                z=calStack.pop() * calStack.pop()
                calStack.push(z)
            }
        }
        else if(proStack[i]==='/'){
            if(calStack.length < 2){
                return undefined
            }
            else{
                c1=calStack.pop()
                c2=calStack.pop()
                if(c1===0){
                    return undefined
                }
                z=c2 / c1
                calStack.push(z)
            }
        }
        else{
            calStack.push(proStack[i])
        }
    }
    return calStack[0]
}
expr=prompt()
queue=[]
queueType=[]
if(parse(expr,queue,queueType)){
    tmp=calculate(queue,queueType)
    if(tmp!==undefined){
        console.log(tmp)
    }
    else{
        console.log('Error in calculating the formula.')
    }
}
else{
    console.log('Error in parsing the formula.Maybe an empty string or illegal one.')
}
