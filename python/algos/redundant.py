def stringdup (str):
    # const alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newstr=''
    for i in range(len(str)):
        check=True
        for j in range (len(newstr)):
            if str[i]==newstr[j]:
                check=False
                break
        if check :
            newstr=newstr+str[i]
    print(newstr)
    return newstr

stringdup("aabccc")    
        




