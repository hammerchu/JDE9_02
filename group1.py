import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def memberOne():
    pass
  
def memberTwo(string,position:int):
    unicode_string_list= []
    unicode_string_list_switch = []
    # Iterate through each character in the string and print its Unicode code point
    for char in string:
        unicode_string_list.append(ord(char))
        if char == " ":
            unicode_string_list_switch.append(ord(char)) 
        else:
            unicode_string_list_switch.append(ord(char)+position)

    
    
    print(unicode_string_list)
    print(unicode_string_list_switch)

    decoded_string = ''.join(chr(code_point) for code_point in unicode_string_list_switch)

    # Print the decoded string
    print(decoded_string)
    return decoded_string
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer())
    print('call memberOne() ')
    print(memberTwo('I am a boy',1))
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
