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
  
def memberTwo():
    pass
  
def Enoch_task_3(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # 讀取文件中的每一行
        reversed_lines = [line.rstrip()[::-1] for line in lines]  # 反轉每一行的字符順序
        reversed_paragraph = '\n'.join(reversed_lines)  # 將反轉後的行重新組合成段落
        return reversed_paragraph
  
def memberFour():
    pass


if __name__ == "__main__":
    print(hammer_task_0())
    print('call memberOne() ')
    print('call memberTwo() ')
    print('Task3:',Enoch_task_3(text))
    print('call memberFour() ')
   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
