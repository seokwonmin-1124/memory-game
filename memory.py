import random
import os

class memory:
    def __init__(self, lev):
        self.lev = lev
        self.numList = []
    
    def getNum(self, min=0, max=10):
        num = random.randint(min, max-1)
        
        self.numList.append(str(num))
        return num

    def answerCheck(self, count, answer):
        if "".join(self.numList[:count]) == answer:
            return True
        return False

    def run(self):
        count = 0
        while True if count == 0 else self.answerCheck(count, answer):
            os.system("clear")
            if count > 0:
                print("정답입니다!")
            count += 1
            num = self.getNum()
            print(num)
            answer = input()

            
            if count == self.lev:
                print("전부 맞추셨습니다!")
                break
        print("답 : ", "".join(self.numList))

mm = memory(10)
mm.run()