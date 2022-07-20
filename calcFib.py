



def fib(n1):
    #n1 = int(input("Termo do fibonnati desejado: "))
    un=1
    penun=1

    if (n1==1) or (n1==2):
        n1=1
    else:
        for count in range(2,n1):
            f1 = un + penun
            penun = un
            un = f1

            count += 1
        n1=un
        return n1
    return n1


#n1 = int(input("Termo do fibonnati desejado: "))
#n1= fib(n1)
#print(n1)