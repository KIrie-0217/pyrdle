import numpy as np
import glob 
import random


class wordle:

    wordlist_all = []
    wordlist_hidden = []
    correctAnswer :str 
    libs = glob.glob("./lib/*")
    numOfAns = 0


    def __init__(self):
        with open(self.libs[1],encoding="utf-8") as words:
            self.wordlist_all = [ i.replace("\n","") for i in words ]
            print(len(self.wordlist_all))
        with open(self.libs[0],encoding="utf-8") as words:
            self.wordlist_hidden = [ i.replace("\n","") for i in words ]
            print(len(self.wordlist_hidden))
        self.setCorrectAnswer()

    def setCorrectAnswer(self):
        self.correctAnswer =  self.wordlist_hidden[random.randrange(len(self.wordlist_hidden))] 

    def answer(self,ans:str):
        if len(list(ans)) != 5:
            print("input should be 5 characters")
            return [0,0,0,0,0],0
        else :
            print("a")

    def answerChecker(self,ans:str):
        if len( list( ans ) ) != len( list(self.correctAnswer) ):
            return np.array([False,False,False,False,False]),np.array([False,False,False,False,False])
        else:
            ans_list = np.array( list(ans) )
            hit = ans_list == np.array( list(self.setCorrectAnswer ) )
            for i in np.array( list( self.setCorrectAnswer ) ):
                print(ans_list == i)




        

a = "aaaaa"
correctAnswer = "happy"

a_list = np.array(list(a))
correctAnswer_list = np.array(list(correctAnswer))

for i in correctAnswer_list:
    print( a_list == i )
print(a_list)
print(correctAnswer_list)

aaa =  correctAnswer_list == "h"
print(aaa)