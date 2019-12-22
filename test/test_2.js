console.log('Please input a pattern string:')
pattern_istr=prompt()
console.log('Please input a main string:')
main_str=prompt()
m_len=main_str.length
p_ilen=pattern_istr.length
if(p_ilen===0){
    if(m_len===0){
        console.log(0)
    }
    else{
        console.log('Error: Pattern string cannot be an empty string.')
    }
}
else{
    pattern_str=[]
    pattern_str.push('$')
    for(i = 0; i < p_ilen; i++){
        pattern_str.push(pattern_istr[i])
    }
    p_len=p_ilen + 1
    next=[]
    next.push( - 1)
    for(i = 1; i < p_len; i++){
        x=next[i - 1]
        while(x >= 0 && pattern_str[i]!==pattern_str[x + 1]){
            x=next[x]
        }
        next.push(x + 1)
    }
    j=0
    ans=[]
    for(i = 0; i < m_len; i++){
        while(j >= 0 && main_str[i]!==pattern_str[j + 1]){
            j=next[j]
        }
        j=j + 1
        if(j===p_len - 1){
            ans.push(i - j + 1)
            j=next[j]
        }
    }
    a_len=ans.length
    if(a_len===0){
        console.log('False')
    }
    else{
        for(i = 0; i < a_len; i++){
            console.log(ans[i])
        }
    }
}
