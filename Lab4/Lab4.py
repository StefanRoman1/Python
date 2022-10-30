import os, operator

def exercise1(director) :
    result = {}
    for file in os.listdir(director) :
        if file[file.rfind(".") + 1:] not in result :
            result[file[file.rfind(".") + 1:]]= 1
        else:
            result[file[file.rfind(".") + 1:]] += 1
    unique_extensions = []
    for i in result :
        if result[i] == 1 :
            unique_extensions.append(i)
    unique_extensions.sort()
    return unique_extensions
    
def exercise2(director, fisier) :    
    with open(fisier, "w") as f :
        for file in os.listdir(director) :
            if file[0] == "A" :
                f.write(os.path.abspath(file) + "\n")

def exercise3(my_path) :
    if os.path.isfile(my_path) :
        with open(my_path, "r") as f :
            return f.read()[-20:]
    elif os.path.isdir(my_path) :
        result = {}
        for file in os.listdir(my_path) :
            if file[file.rfind("."):] not in result :
                result[file[file.rfind(".") + 1:]] = 1
            else :
                result[file[file.rfind(".") + 1:]] += 1
        #return a list of tuples sorted by the number of files
        return [(k,v) for k,v in sorted(result.items(), key = operator.itemgetter(1), reverse = True)]

def exercise4() :
    director = input("Introduceti directorul: ")
    result = {}
    for file in os.listdir(director) :
        if file[file.rfind(".") + 1:] not in result :
            result[file[file.rfind(".") + 1:]]= 1
        else:
            result[file[file.rfind(".") + 1:]] += 1
    unique_extensions = []
    for i in result :
        if result[i] == 1 :
            unique_extensions.append(i)
    unique_extensions.sort()
    return unique_extensions

def exercise5(target, to_search) :
    if os.path.isfile(target) :
        with open(target, "r", encoding="utf8") as f :
            if to_search in f.read() :
                return [target]
            else :
                return []
    elif os.path.isdir(target) :
        result = []
        for file in os.listdir(target) :
            result += exercise5(os.path.join(target, file), to_search)
        return result
    else :
        raise ValueError("Nu este nici director, nici fisier")

def callback(e) :
    print(e)
    return True

def exercise6(target, to_search, callback) :
    try :
        return exercise5(target, to_search)
    except ValueError as e :
        callback(e)

def exercise7(target) :
    result = {}
    result["full_path"] = os.path.abspath(target)
    result["file_size"] = os.path.getsize(target)
    result["file_extension"] = target[target.rfind(".") + 1:]
    result["can_read"] = os.access(target, os.R_OK)
    result["can_write"] = os.access(target, os.W_OK)
    return result

def exercise8(dir_path) :
    result = []
    for file in os.listdir(dir_path) :
        result.append(os.path.join(dir_path, file))
    return result

#print(exercise1('C:\GOG Games\Terraria'))
#exercise2(r"C:\Users\stefa\Python\Python\Lab4\New folder", r"C:\Users\stefa\Python\Python\Lab4\Fisier.txt")
#print(exercise3(r"C:\Users\stefa\Python\Python\Lab4\Fisier.txt"), exercise3(r"C:\Users\stefa\Python\Python\Lab4\New folder"))
#print(exercise4())
#print(exercise5(r"C:\Users\stefa\Python\Python\Lab4\New_folder_with_txts", "a"), exercise5(r"C:\Users\stefa\Python\Python\Lab4\Fisier.txt", "a"))
#print(exercise6(r"C:\Users\stefa\Python\Python\Lab4\New_folder", "a", callback))
#print(exercise7(r"C:\Users\stefa\Python\Python\Lab4\Fisier.txt"))
#print(exercise8(r"C:\Users\stefa\Python\Python\Lab4\New folder"))