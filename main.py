fruit = "banana"
letter = fruit[0]
print(letter)
print(fruit[1])
i = 0
print(fruit[i-2])
print(len(fruit))
print(fruit[len(fruit)-1])

prefixes = 'JKLMNOPQ'
suffixes = 'ack'

for letter in prefixes:
    print(letter+suffixes)

name = "westminister"

#def absolute_is_valid(test):
#    if (isinstance(test, int)) and (1 <= test <=3 ):
#        return True
#    else:
#        return False

#print(test_is_valid("3"))
#print(test_is_valid("3"))
#print(test_is_valid("0"))


def myname():
    name = "Dinora"
    print(name)

def myname2():
    name = "Dinora2"
    print(myname2)

def fancy_string():
    fancy_string = """
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█

    """
    return fancy_string

print(fancy_string())