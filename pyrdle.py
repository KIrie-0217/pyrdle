import numpy as np
import fabric
import glob
import random


class pyrdle:

    wordlist_all : list
    wordlist_hidden  : list
    libs = glob.glob("./lib/*")

    correctAnswer :str
    correctAnswer_list = np.empty((0,1))

    numOfAns : int

    preHit = np.empty((0,1))
    preBit = np.empty((0,1))

    clearFlag : bool = False

    def __init__(self):
        with open(self.libs[1],encoding="utf-8") as words:
            self.wordlist_all = [ i.replace("\n","") for i in words ]
        with open(self.libs[0],encoding="utf-8") as words:
            self.wordlist_hidden = [ i.replace("\n","") for i in words ]
        self.setCorrectAnswer()
        self.numOfAns = 0
        self.preHit = np.empty( (0,self.correctAnswer_list.size) ,dtype=bool)
        self.preBit = np.empty( (0,self.correctAnswer_list.size) ,dtype=bool)


    def init(self):
        self.__init__()
        return 0

    def setCorrectAnswer(self):
        self.correctAnswer =  self.wordlist_hidden[random.randrange(len(self.wordlist_hidden))]
        self.correctAnswer_list = np.array( list( self.correctAnswer ))
        return self.correctAnswer

    def answer(self,ans:str):
        if self.numOfAns == 6 or self.clearFlag == True :
            print("this game is already end")
            return self.preHit[5],self.preBit[5],self.numOfAns

        elif len(list(ans)) != 5:
            print("input should be 5 characters")
            return np.array([False,False,False,False,False]),np.array([False,False,False,False,False]),self.numOfAns

        elif self.numOfAns < 6 :
            self.numOfAns += 1
            hit,bit = self.answerChecker(ans)


            self.preHit = np.append(self.preHit,np.array([hit]),axis=0)
            self.preBit = np.append(self.preBit,np.array([bit]),axis=0)


            if np.all(hit) == True:
                print("congratulate!")
                print("the correct answer is" + self.correctAnswer)
                self.clearFlag == True

            return hit,bit,self.numOfAns

    def answerChecker(self,ans:str):
        if len( list( ans ) ) != len( list(self.correctAnswer) ):
            return np.array([False,False,False,False,False]),np.array([False,False,False,False,False])
        else:
            ans_list = np.array( list(ans) )
            print(ans_list)
            print(self.correctAnswer_list)
            hit = ans_list == self.correctAnswer_list
            bit = np.array( [False]*ans_list.size )
            for i in range(self.correctAnswer_list.size):
                flag = 0
                for j in range(ans_list.size):
                    if flag == 0 and ans_list[j] == self.correctAnswer_list[i]:
                        bit[j] = True
            return hit,bit


def main():

    wordle = pyrdle()

    correct = wordle.setCorrectAnswer()
    correct_list = np.array( list(correct) )
    print(correct)

    ans = [ "happy", "lucky" , "humor","intel",correct ,"rabit","aaaaa"]
    print( fabric.green("a"))
    for i in ans:
        print( " your ans is " + i)
        hit,bit,count = wordle.answer(i)
        print("hit is" + str(hit))
        print("bit is" + str(bit) )
        print("count is" + str(count) )


    return 0

if __name__ == "__main__":
    main()