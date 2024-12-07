import random
question = ['a','b','c','d','e']

def created():
    num =[]
    #s=""    (字串方法)
    for j in range(10):
        num.insert(j,j)
    #print(num)    (字串方法)
    i = 0
    while i<digit:
        #print(i)
        r = random.randint(0,9-i)
        question[i] = num[r]
        #s = s + num[r]    (字串方法)
        del num[r]    #=num.remove(r)
        #print(num)
        i+=1
    print(question)

def check(answer_str):
    global question
    answer = ['a','b','c','d','e']
    howManyA = 0
    howManyB = 0
    for i in range(digit):
        answer[i] = int(answer_str[i])
    for i in range(digit):
        for j in range(digit):
            if(answer[i] == question[j]):
                if(i==j):
                    howManyA +=1
                else:
                    howManyB +=1
    return f"{howManyA}A{howManyB}B"

digit=0
def main():
    global digit
    while True:
        digitAsk = input("要猜幾位數(2~5):")
        if digitAsk.isdigit() :
            digit = int(digitAsk)
            if 2<=digit<=5 :
                break

    created()
    howManyTimes = 1
    while True:
        answer_str = input(f"你猜(第{howManyTimes}次):")
        if answer_str =="stop" :
            print("停止")
            print("答案:",question)
            break
        elif len(answer_str) != digit or answer_str.isdigit() is False :
            print("錯誤")
            continue
        howManyTimes +=1
        result = check(answer_str)
        print(result)
        if(int(result[0]) == digit ):
            print("猜對了")
            print("共花了",howManyTimes,"次")
            break

main()