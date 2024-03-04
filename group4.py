import random

text = './news.txt'
f = open(text, "r")
print(f.read())
txt = f.read().replace('\n',' ')

def hammer_task_0():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result
  
def memberOne():
    #Task 1
    count=0
    for i in txt:
        if i in ('a','e','i','o','u'):
        # if the word in the news match with any word in the turple, add the number of count by one.
            count+=1
    return(count)

def memberTwo(n):
    #Task 2
    ans = ""
    for i in range(len(txt)):
        ch = txt[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            # use ASCii code to find the word is encrypt to [A:65-Z:90]
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            # use ASCii code to find the word is encrypt to [a:97-z:122]
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans
  
def memberThree():
    #Task 3
    #slice the word backward 
    result = txt[::-1]
    return(result)
  
def memberFour():
    #Task 4
    #separate the word by space
    result = txt.split(' ')
    temp =[]
    for i in result:
        #slice the word backward
        temp.append(i[::-1])
    #combine the list in to a single line
    return(' '.join(temp))


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
