def check(fil, key):
    ans = hash(key)
    f = open("password.txt", 'r')
    passws = f.read().strip()
    passws = passws.split('\n')
    f.close()
    
    try:
        exist = passws.index(str(ans))
    except:
        exist = -1
    
    if exist == -1:
        return 0
    else:
        del passws[exist]
        pswd =''
        for i in passws:
            pswd += i + '\n' 
            
        f = open('password.txt', 'w')
        f.writelines(pswd)
        f.close()
        return 1
    