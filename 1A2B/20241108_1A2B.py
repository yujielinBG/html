import random
question = ['a','b','c','d']


def created():
    num =[]
    for j in range(10):
        num.insert(j,j)
    #print(num)
    i = 0
    while i<4:
        #print(i)
        r = random.randint(0,9-i)
        question[i] = num[r]
        del num[r]
        #num.remove(r)
        #print(num)
        i+=1
    print(question)

def check(answer_str):
    global question
    answer = ['a','b','c','d']
    howManyA = 0
    howManyB = 0
    for i in range(4):
        answer[i] = int(answer_str[i])
    for i in range(4):
        for j in range(4):
            if(answer[i] == question[j]):
                if(i==j):
                    howManyA +=1
                else:
                    howManyB +=1
    return f"{howManyA}A{howManyB}B"

created()
howManyTimes = 1
while True:
    answer_str = input(f"你猜(第{howManyTimes}次)")
    if answer_str =="stop" :
        print("停止")
        break
    if len(answer_str) != 4 :
        print("錯誤")
        continue
    howManyTimes +=1
    result = check(answer_str)
    print(result)
    if(result == "4A0B" ):
        print("猜對了")
        print("共花了",howManyTimes,"次")
        break
