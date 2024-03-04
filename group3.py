import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def wordswithvowel():
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    # Split the text into words
    words = text.split()
    
    # Iterate through each word
    for word in words:
        # Convert the word to lowercase for case-insensitive matching
        word = word.lower()
        
        # Check if the word contains any vowel characters
        if any(vowel in word for vowel in vowels):
            count += 1
    
    return count
    pass
  
def caesar_cipher_encode(text, shift):
    encoded_text = ""
    
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the shift value based on the character's case
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            
            # Apply the shift and wrap around the alphabet
            encoded_char = chr((ord(char) - base + shift) % 26 + base)
        else:
            # Keep non-alphabetic characters unchanged
            encoded_char = char
        
        encoded_text += encoded_char
    
    return encoded_text
  
def memberThree():
    pass
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('call memberThree() ')
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
