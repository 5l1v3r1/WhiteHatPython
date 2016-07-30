#PYTHON note
##########################List Slicing: list[start:end:step]######################################
    user_args = sys.argv[1:] #sys.argv[1],sys.argv[2],....
    #note that sys.argv is a collection or list of stringsT and then with above operation , user_args will be too
    user_args = sys.argv[2:4]#sys.argv[2],sys.argv[3],sys.argv[4] 
    #Suppose you want the last argument (last argument is always -1,second last argument is -2 ,....
    #so what is happening here is we start the count from back. So start is last, no end, no step) :
    user_args = sys.argv[-1]
    #Suppose you want the last two arguments :
    user_args = sys.argv[-2:]    
    #Suppose you want the arguments in reverse order :
    user_args = sys.argv[::-1]
    #server.accept() output is a collection of {[socket object],[socket(ip,port)]}: (<socket._socketobject object at 0x02E3C998>, ('127.0.0.1', 25129))
    #item1,item2,....=collection
    client, addr=server.accept()# now we can use client as a socket object, and use addr[0] for ip, and addr[1] is port
    
#######################################################################
    str = "doesn't or dosn\'t" * 10
    1j + 3j
    list_kharid[1:3]
    #['sibzamini', 'mast']    
    list_kharid[1:3]=["sir"]
    list_kharid[:]=[]
    list_kharid
    #[]    
    list_kharid.append("goje")
    
    
    
    