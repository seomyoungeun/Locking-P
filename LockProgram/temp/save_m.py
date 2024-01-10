def save(fil, key):
    
    pasw = hash(key)
    
    f = open("password.txt", 'a')
    f.write("{0} \n".format(pasw))
    f.close()