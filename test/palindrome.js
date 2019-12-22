console.log('Please input a string:')
str=prompt()
l=str.length
flag=0
for(i = 0; i < l; i++){
    if(str[i]!==str[l - 1 - i]){
        flag=1
        break
    }
}
if(flag){
    console.log('False')
}
else{
    console.log('True')
}
