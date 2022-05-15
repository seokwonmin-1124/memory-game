# LESH
import random

def mix(lev):
    count = 1
    num = random.randint(0, 9)
    print(num)
    num = int(num)
    list = []
    list.append(num)
    print(list[0])
    answer = input("숫자 입력 : ")
    if int(answer) == list[0]:
        print("정답입니다.")
        while count <= lev:
            num = random.randint(0, 9)
            num = int(num)
            print(num)
            list.append(num)
            dap = ''.join(map(str, list))
            answer = input("숫자 입력 : ")
            if answer != dap:
                print(f"정답은 {dap} 입니다")
                print(f"{count} 단계까지 성공했습니다.")
                print("오답")
                break
            else:
                None
            count += 1
    else:
        print("오답입니다. 처음부터 다시 시작합니다.")
mix(10)