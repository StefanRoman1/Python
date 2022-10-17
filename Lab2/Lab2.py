def isPrime(n) :
    if n < 2 : 
        return False
    if n == 2 : 
        return True
    for i in range(2, int(n/2)+1) :
        if n % i == 0 : 
            return False
    return True

def isPalindrome(number) :
    number = str(number)
    if number == number[::-1] :
        return True
    else :
        return False

def exercise1(n) :
    list = []
    a = 0
    b = 1
    if n == 1 : 
        list.append(a)
        return list
    if n == 2 : 
        list.append(a)
        list.append(b)
        return list
    if n > 2 : 
        list.append(a)
        list.append(b)
        for i in range(2,n) :
            aux = a + b
            list.append(aux)
            a = b
            b = aux
        return list

def exercise2(givenList) :
    returnList = []
    for i in givenList : 
        if isPrime(i) == True :
            returnList.append(i)
    return returnList

def exercise3(listA, listB) :
    reunite = []
    for i in listA :
        reunite.append(i)
    for i in listB :
        if i not in reunite :
            reunite.append(i)
    intersection = []
    for i in listA :
        if i in listB :
            intersection.append(i)
    differenceA = []
    for i in listA :
        if i not in listB :
            differenceA.append(i)
    differenceB = []
    for i in listB :
        if i not in listA :
            differenceB.append(i)
    return reunite, intersection, differenceA, differenceB

def exercise4(musicalNotes, pattern, start) :
    song = []
    song.append(musicalNotes[start])
    i = 0
    while(len(song) < len(pattern) + 1) :
        if start + pattern[i] < len(musicalNotes) :
            song.append(musicalNotes[start + pattern[i]])
            start = start + pattern[i]
            i = i + 1
        else :
            start = start + pattern[i] - len(musicalNotes)
            song.append(musicalNotes[start])
            i = i + 1
    return song

def exercise5(matrix) :
    for i in range(0, len(matrix)) :
        for j in range(0, len(matrix[i])) :
            if i > j :
                matrix[i][j] = 0
    return matrix

def exercise6(*lists, x) :
    total = {}
    for i in lists :
        for j in i :
            if j in total :
                total[j] = total[j] + 1
            else :
                total[j] = 1
    returnList = []
    for i in total :
        if total[i] == x :
            returnList.append(i)
    return returnList

def exercise7(list) :
    count = 0
    max = 0
    for i in list :
        if isPalindrome(i) == True :
            count += 1
            if i > max :
                max = i
    return count, max

def exercise8(words, x = 1, flag = True) :
    returnList = []
    if flag == True :
        for word in words :
            wordList = []
            for i in list(word.encode('ascii')) :
                if i%x == 0 :
                    wordList.append(chr(i))
            returnList.append(wordList)
    if flag == False :
        for word in words :
            wordList = []
            for i in list(word.encode('ascii')) :
                if i%x != 0 :
                    wordList.append(chr(i))
            returnList.append(wordList)
    return returnList

def exercise9(matrix) :
    list = []
    for i in range(0, len(matrix[1])) :
        max = 0
        for j in range(0, len(matrix)) :
            if matrix[j][i] < max :
                list.append((j,i))
            else :
                max = matrix[j][i]
    return list

def exercise10(*lists) :
    returnList = []
    for i in range(0, len(lists[0])) :
        aux = ()
        for j in range(0, len(lists)) :
            aux += (lists[j][i],)
        returnList.append(aux)
    return returnList

def takeThirdLetterOfSecondWord(elem):
    return elem[1][2]

def exercise11(list) :
    list.sort(key = takeThirdLetterOfSecondWord)
    return list 

def exercise12(words) :
    returnList = []
    for word in words :
        list_of_rhyme = [elem for elem in words if elem[-2:] == word[-2:]]
        if(list_of_rhyme not in returnList) :
            returnList.append(list_of_rhyme)
    return returnList

# print(exercise1(10))
# print(exercise2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
# print(exercise3([1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
# print(exercise4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
# print(exercise5([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]))
# print(exercise6([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], x = 2))
# print(exercise7([121,111,73,75,989,1001]))
# print(exercise8(["test", "hello", "lab002"], 2, False))
# print(exercise9([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]]))
# print(exercise10([1,2,3], [5,6,7], ["a", "b", "c"]))
# print(exercise11([('abc', 'bcd'), ('abc', 'zza')]))
# print(exercise12(['ana', 'banana', 'carte', 'arme', 'parte']))