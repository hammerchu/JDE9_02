import random

text = './news.txt'
f = open(text, "r")
print(f.read())


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
  
def memberOne(filename):
    with open(filename, 'r') as file:
        paragraph = file.read()

    vowels = set("aeiouAEIOU")
    words = paragraph.split()
    
    count = 0
    for word in words:
        if any(char in vowels for char in word):
            count += 1

    return count

def memberTwo(filename, shift=1):  # Kenneth task
    with open(filename, 'r') as file:
        paragraph = file.read()

    result = ""
    for char in paragraph:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result
  
def memberThree(filename):
    # Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I
    with open(filename, 'r') as file:
        paragraph = file.read()

def memberThree(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    reversed_paragraph = ""
    for line in lines:
        words = line.split()
        for word in words:
            reversed_paragraph += word[::-1] + " "
        reversed_paragraph += '\n'
    
    return reversed_paragraph.rstrip('\n')

def memberFour():
    pass


if __name__ == "__main__":
    # print(hammer())
    print('call memberOne() ')
    print(memberOne(text))
    print('call memberTwo() ')
    print(memberTwo(text))
    print('call memberThree() ')
    print(memberThree(text))
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
