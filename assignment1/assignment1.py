def hello():
    print("Hello!")
    return "Hello!"

def greet(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

def calc (x, y, op="multiply"):
    try:
        if op == "add":
            return x + y
        elif op == "subtract":
            return x - y
        elif op == "multiply":
            return x * y
        elif op == "divide":
            return x / y
        elif op == "modulo":
            return x % y
        elif op == "int_divide":
            return x // y
        elif op == "power":
            return x ** y
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

def data_type_conversion(x, type="int"):
    try:
        if type == "int":
            return int(x)
        elif type == "float":
            return float(x)
        elif type == "str":
            return str(x)
    except ValueError:
        return "You can't convert {} into a {}.".format(x, type)
    
def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
def repeat(x, times=1):
    try:
        s = ""
        for i in range(times):
           s += x
        return s
    except TypeError:
        return "You can't repeat {} {} times.".format(x, times) 
    
def student_scores(mode,**kwargs):
    try:
        if mode == "best":
            best_student = None
            best_score = 0

            for key, value in kwargs.items():
                if value >= best_score:  
                    best_score = value
                    best_student = key              
            return best_student
        
        elif mode == "mean":
            return sum(kwargs.values()) / len(kwargs)  
        else:
            return "Invalid mode"
    except TypeError:
        return "Invalid data was provided."

def titleize(string): 
    words = string.split(" ")
    words[0]=words[0].capitalize()
    words[-1]=words[-1].capitalize()
    for i in range(1,len(words)-1):
        if words[i] not in ("a", "on", "an", "the", "of", "and", "is", "in"):
            words[i]=words[i].capitalize()

    return " ".join(words)

def  hangman(word,guessed_letters):
    s = ""
    for i in word:
        if i in guessed_letters:
            s += i
        else:
            s += "_"
    return s

def pig_latin  (string):
    result = []
    for word in string.split(" "):
        s = ""
        if word[0] in ("a", "e", "i", "o", "u"):
            s += word
        else:
            cons = ""
            was_q = False
            for i, char in enumerate(word):
                if char not in ("a", "e", "i", "o", "u"):
                    cons += char
                if char == "q":
                    was_q = True
                if was_q and char == "u":
                    cons += char
                    was_q = False
                    continue
                if char in ("a", "e", "i", "o", "u"):
                    break
            s += word[i:] + cons
        s += "ay"
        result.append(s)
    return " ".join(result)