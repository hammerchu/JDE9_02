import random

# text = './news.txt'
# f = open(text, "r")
# print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    print('hello JDE')
    result = random.sample(teamJDE, 1)
    return result


def hammer_task_1():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    print('hello JDE task 1')
    result = random.sample(teamJDE, 1)
    return result
  
def chinny_task_1(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str_list = string.split(' ')
    count = 0 

    for word in str_list:
        for vowel in vowels:
            if vowel in word:
                print(f'vowel: {vowel} in word : {word}')
                count += 1
                break
    return count 
  
def chinny_task_2(string,position:int=1):
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

    return decoded_string
  
def chinny_task_3(string):
    reverse_list = []
    
    for char in string:
        reverse_list = [char] + reverse_list

    # printing resultant list 
    print("Reverse list: " + str(reverse_list))

    combine_str = ''.join(char for char in reverse_list)
    return combine_str
  
def chinny_task_4(str):
    reversed_words = str[::-1].split(" ")
    reversed_words.reverse()
    combined_str = ' '.join(word for word in reversed_words)
    return combined_str


if __name__ == "__main__":
    # print(hammer())
    print('call memberOne() ')
    # print(chinny_task_1('I am a boy'))
    # print(chinny_task_2('I am a boy'))
    # print(chinny_task_3('I am a boy'))
    print(chinny_task_4('I am a boy'))
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
