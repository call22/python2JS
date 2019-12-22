print('Please input a pattern string:')
pattern_istr = input()
print('Please input a main string:')
main_str = input()
m_len = len(main_str)
p_ilen = len(pattern_istr)

if(p_ilen == 0):
    if(m_len == 0):
        print(0)
    else:
        print('Error: Pattern string cannot be an empty string.')
else:
    pattern_str = []
    pattern_str.append('$')
    for i in range(0, p_ilen):
        pattern_str.append(pattern_istr[i])
    p_len = p_ilen + 1
    next = []
    next.append(-1)
    for i in range(1, p_len):
        x = next[i - 1]
        while (x >= 0 and pattern_str[i] != pattern_str[x + 1]):
            x = next[x]
        next.append(x + 1)
    j = 0
    ans = []
    for i in range(0, m_len):
        while (j >= 0 and main_str[i] != pattern_str[j + 1]):
            j = next[j]
        j = j + 1
        if (j == p_len - 1):
            ans.append(i)
            j = next[j]
    a_len = len(ans)
    if (a_len == 0):
        print('False')
    else:
        for i in range(0, a_len):
            print(ans[i])
