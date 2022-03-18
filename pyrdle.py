# coding: UTF-8

import numpy as np
import glob
import random
import sys



class pyrdle:

    wordlist_all : list
    wordlist_hidden  : list
    libs = glob.glob("./lib/*")

    correctAnswer :str
    correctAnswer_list = np.empty((0,1))

    numOfAns : int
    word_length : int

    preHit = np.empty((0,1))
    preBit = np.empty((0,1))
    preDisplay = np.empty(0)

    clearFlag : bool = False

    def __init__(self):
        with open(self.libs[1],encoding="utf-8") as words:
            self.wordlist_all = [ i.replace("\n","") for i in words ]
        with open(self.libs[0],encoding="utf-8") as words:
            self.wordlist_hidden = [ i.replace("\n","") for i in words ]
        self.setCorrectAnswer()
        self.numOfAns = 0
        self.word_length = len(self.correctAnswer)
        self.preHit = np.empty( (0,self.correctAnswer_list.size) ,dtype=bool)
        self.preBit = np.empty( (0,self.correctAnswer_list.size) ,dtype=bool)
        self.preDisplay = np.empty(0,dtype=str)


    def init(self):
        self.__init__()
        print("the game is initialized !!")
        return 0

    def setCorrectAnswer(self):
        self.correctAnswer =  self.wordlist_hidden[random.randrange(len(self.wordlist_hidden))].upper()
        self.correctAnswer_list = np.array( list( self.correctAnswer ))
        return self.correctAnswer

    def answer(self,ans:str):
        ans = ans.upper()

        if self.numOfAns == 6 or self.clearFlag == True :
            print("this game is already end")
            return self.preHit[5],self.preBit[5],self.numOfAns,self.preDisplay

        elif len(list(ans)) != self.correctAnswer_list.size:
            print("input should be " + str(self.correctAnswer_list.size) +" characters")
            return np.array([False,False,False,False,False]),np.array([False,False,False,False,False]),self.numOfAns,self.preDisplay

        elif self.isAnswerExists(ans) != True:
            print("Not in word list")
            return np.array([False,False,False,False,False]),np.array([False,False,False,False,False]),self.numOfAns,self.preDisplay

        elif self.numOfAns < 6 :
            self.numOfAns += 1
            hit,bit = self.answerChecker(ans)
            display = self.answerDisplayer(ans,hit,bit)

            self.preHit = np.append(self.preHit,np.array([hit]),axis=0)
            self.preBit = np.append(self.preBit,np.array([bit]),axis=0)
            self.preDisplay = np.append(self.preDisplay,np.array(display))


            if np.all(hit) == True:
                print("congratulate!")
                print("the correct answer is" + self.correctAnswer)
                self.clearFlag == True

            return hit,bit,self.numOfAns,self.preDisplay

    def answerChecker(self,ans:str):
        if len( ans  ) != len( self.correctAnswer ):
            return np.array([False,False,False,False,False]),np.array([False,False,False,False,False])
        else:
            ans_list = np.array( list(ans) )
            hit = ans_list == self.correctAnswer_list

            bit = np.array( [False]*ans_list.size )
            hitCheckFlag = np.zeros(ans_list.size)

            for i in range(ans_list.size):
                if hit[i] == True:
                            bit[i] = True
                            hitCheckFlag[i] = 1

            for i in range(ans_list.size):
                if hit[i] == False:
                    for j in range(ans_list.size):
                        if ans_list[j] == self.correctAnswer_list[i] and hitCheckFlag[j] != 1:
                            bit[j] = True

            bit = hit^bit


            return hit,bit

    def answerDisplayer(self,ans:str,hit,bit):
        displayStr = ""
        listAns = list(ans)

        for i in range(len(ans)):
            if hit[i] == True :
                displayStr += self.wordColor.green(listAns[i]) + " "
            elif bit[i] == True:
                displayStr += self.wordColor.yellow(listAns[i]) + " "
            else:
                displayStr += self.wordColor.black(listAns[i]) + " "

        return displayStr

    def isAnswerExists(self,ans:str):
        return ans.lower() in self.wordlist_hidden

    class wordColor:
        BLACK     = '\033[40m'
        RED       = '\033[41m'
        GREEN     = '\033[42m'
        YELLOW    = '\033[43m'
        BLUE      = '\033[44m'
        MAGENDA    = '\033[45m'
        CYAN      = '\033[46m'
        WHITE     = '\033[47m'
        END       = '\033[0m'

        @classmethod
        def red(self,output):
            return self.RED + output + self.END

        @classmethod
        def green(self,output):
            return self.GREEN + output + self.END

        @classmethod
        def yellow(self,output):
            return self.YELLOW + output + self.END

        @classmethod
        def blue(self,output):
            return self.BLUE + output + self.END

        @classmethod
        def purple(self,output):
            return self.MAGENDA + output + self.END

        @classmethod
        def cyan(self,output):
            return self.CYAN + output + self.END

        @classmethod
        def white(self,output):
            return self.WHITE + output + self.END

        @classmethod
        def black(self,output):
            return self.BLACK + output + self.END

def  pyrdlePlay():

    def gameEnd():
        print("This game is end")
        yn = input("Do you want to play again ? [y/n] : ")
        if yn.lower() == "y" or yn.lower() == "yes" :
            wordle.init()
            if len(sys.argv) > 1 and sys.argv[1] == "-dev" or sys.argv[1] =="-d":
                print(wordle.correctAnswer)
            return True
        elif yn.lower() == "n" or yn.lower() == "no" :
            return False

    wordle = pyrdle()


    if len(sys.argv) > 1:
        if  "-dev" in sys.argv or "-d" in sys.argv:
            print(wordle.correctAnswer)

        elif "--help" in sys.argv or "-h" in sys.argv:
            print("Guess the WORDLE in 6 tries.")
            print("Each guess must be a valid 5 letter word. Hit the enter button to submit.")
            print("After each guess, the color of the tiles will change to show how close your guess was to the word.")

            print("---------------------------------------")
            print("Examples")
            print( pyrdle.wordColor.green("S") + " T A T E")
            print("The letter S is in the word and in the correct spot")
            print( "P " + pyrdle.wordColor.yellow("L") + " A N E")
            print("The letter L is in the word but the wrong spot.")
            print("U N " + pyrdle.wordColor.purple("I") + " T E")
            print("The letter I is not in the word in any spot")


            print("---------------------------------------")
            print("In-game commands")
            print("--giveup : you can give up.")
            print("--init : the game is end and a new game starts.")

            print("---------------------------------------")
            print("Commands")
            print("--dev or -d : dev mode,the correct answer is displayed first.")
            print("--help or -h : You will see how to play the game and other help.")
            return 0
        else :
            print("unrecognized option")
            print("try --help or -h for more information.")
            return 0

    while True:
        answer = input("please input your answer : ")

        if answer == "--giveup":
            print("You gave up")
            print("Correct Answer is :" + wordle.correctAnswer)
            if gameEnd():
                continue
            else:
                return 0

        elif answer == "--init":
            wordle.init()

            if len(sys.argv) > 1 and sys.argv[1] == "-dev" or sys.argv[1] =="-d":
                print(wordle.correctAnswer)
            continue


        hit,bit,count,display = wordle.answer(answer)
        for i in display:
            print(i)
        print(count)

        if count == 6 or np.all(hit) == True :
            if gameEnd():
                continue
            else:
                return 0


