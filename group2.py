import random

#text = 'C:\Users\GenHK\JDE9_02\news.txt'
#f = open(text, "r")
#print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def memberOne():
    pass
  
def memberTwo():
    pass
  
def memberThree():
    pass
  
def memberFour():
    pass


#if __name__ == "__main__":
    #print(hammer())
    #print('call memberOne() ')
    #print('call memberTwo() ')
    #print('call memberThree() ')
    #print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob




#Task 2 
#def shift (txt,shift):
    #encoded_text = ''
        #for char in txt:
            #if 

text1 = r'C:\Users\GenHK\JDE9_02\news.txt'
f = open(text1,'r',encoding="utf-8")
v = f.read()

def sunny_shifting(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded_char = char
        encoded_text += encoded_char
    return encoded_text

paragraph = v
shift_value = 1
encoded_paragraph = sunny_shifting(paragraph, shift_value)

print("Original: ", paragraph)
print("Encoded_replace: ", encoded_paragraph)

#print(shift(r'C:\Users\GenHK\JDE9_02\news.txt',1))



