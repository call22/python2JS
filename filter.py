def spaceFilter(filename_in, filename_out):
    fi = open(filename_in,mode = 'r')
    fo = open(filename_out,mode = 'w')
    data = fi.readlines()
    for i in data:
        flag = True
        l_len = len(i)
        for j in range(0,l_len):
            tmp_c = i[j]
            if(tmp_c != '\n' and tmp_c != '\r' and tmp_c != ' ' and tmp_c != '\t'):
                flag = False
                break
        if(not flag):
            fo.write(i)
    fi.close()
    fo.close()
