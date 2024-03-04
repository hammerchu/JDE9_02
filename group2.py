import random
text = './news.txt'
f = open(text, "r")
# print(f.read())


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

def memberFive(text):
    print('----------------')
    f=open(text,'r')

    lines=f.readlines()
    #task 3 
    new_p=[]
    for line in lines:
        for l in reversed(line):
            new_p.append(l)
        print('----')
    print(''.join(new_p))

    
    # print(words)
    pass

if __name__ == "__main__":
    # print(hammer())
    text = './news.txt'
    print('call memberOne() ')
    print('call memberTwo() ')  
    print('call memberThree() ')
    print('call memberFour() ')
    memberFive(text)

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
