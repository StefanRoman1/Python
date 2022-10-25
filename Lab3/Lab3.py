def exercise1(listA, listB) :
    intersection = set(listA) & set(listB)
    reunion = set(listA) | set(listB)
    difference = set(listA) - set(listB)
    difference2 = set(listB) - set(listA)
    returnList = []
    returnList.append(intersection)
    returnList.append(reunion)
    returnList.append(difference)
    returnList.append(difference2)
    return returnList

def exercise2(word) : 
    occurances = {}
    for i in word :
        if i in occurances :
            occurances[i] += 1
        else :
            occurances[i] = 1
    return occurances

def exercise3(dict1, dict2) :
    dict3 = {}
    for i in dict1 :
        if i not in dict2 :
            dict3[i] = dict1[i]
    for i in dict2 :
        if i not in dict1 :
            dict3[i] = dict2[i]
    return dict3

def build_xml_element(tag, content, **kwargs) :
    xml = "<" + tag + " "
    for i in kwargs :
        xml += i + " =\" " + kwargs[i] + "\""
    xml += ">" + content + "</" + tag + ">"
    return xml

def validate_dict(rules, dictionary) :
    for i in dictionary :
        has_rule = False
        for j in rules :
            if i == j[0] :
                has_rule = True
                if(dictionary[i][:len(j[1])] != j[1] and dictionary[i][len(j[1]):dictionary[i]-len(j[3])].find(j[2]) == -1 and dictionary[i][dictionary[i]-len(j[3]):] != j[3]) :
                    return False
                break
        if not has_rule :
            return False
    return True

def exercise6(list) :
    unique = {}
    unice = 0
    duplicate = 0
    for i in list : 
        if i not in unique :
            unique[i] = 1
        else :
            unique[i] += 1
    for i in unique :
        if unique[i] == 1 :
            unice += 1
        else :
            duplicate += 1
    return unice, duplicate

def exercise7(*args) :
    result = {}
    for i in range(len(args)) :
        for j in range(i+1, len(args)) :
            result[str(args[i]) + " & " + str(args[j])] = args[i] & args[j]
            result[str(args[i]) + " | " + str(args[j])] = args[i] | args[j]
            result[str(args[i]) + " - " + str(args[j])] = args[i] - args[j]
            result[str(args[j]) + " - " + str(args[i])] = args[j] - args[i]
    return result

def exercise8(mapping) :
    list = []
    list.append(mapping["start"])
    while mapping[list[-1]] not in list :
        list.append(mapping[list[-1]])
    return list

def exercise9(*args, **kwargs) :
    count = 0
    for i in args :
        if i in kwargs.values() :
            count += 1
    return count


#print(exercise1([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
#print(exercise2("Ana has apples."))
#print(exercise3({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "d": 4}))
#print(build_xml_element("a", "Hello world!", href =" http://python.org ", _class =" my-link ", id= "someid "))
#print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},{"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
#print(exercise6("mmammbc"))
#print(exercise7({3,6}, {5, 6}))
#print(exercise9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
#print(exercise8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))