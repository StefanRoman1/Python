def cmmdc(a, b) :
    while(a!=b) :
        if(a > b) :
            a -= b
        else :
            b -= a
    return a

def exercise1() :
    print("Execise 1 : ")
    n = int(input("How many numbers ? "))
    list = []
    print("Write the numbers : ")
    for i in range(0,n) :
        aux = int(input())
        list.append(aux)
    a = list[0]
    b = list[1]
    c = cmmdc(a,b)
    for i in range(2,n) :
        aux = list[i]
        c = cmmdc(c,aux)
    print("Cmmd is : %d" %c)

def exercise2(a) :
    count = 0
    for i in a :
        if i.lower() in ('a', 'e', 'i', 'o', 'u') :
            count += 1
    print("Number of vowels is : %d" %count)

def exercise3(a,b) :
    count = 0
    for i in range(0, len(b)-len(a)) :
        if b[i : i + len(a)] == a :
            count += 1 
    print(count)

def exercise4(a) :
    result = a[0].lower()
    for i in range(1,len(a)) :
        if a[i].isupper() == True : 
            result += '_' + a[i].lower()
        else :
            result += a[i]
    print(result)

#def exercise5(a) :
    




#exercise1()
#exercise2("abcda")
#exercise3("text","ttextastextsstexts")
#exercise4("ThisIsCamelCaseLOL")
#exercise5([['f','i','r','s'],['n','_','l','t'], ['o','b','a','_'],['h','t','y','p']])