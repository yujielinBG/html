import random
question = ['a','b','c','d']
answer = ['a','b','c','d']
howManyA = 0
howManyB = 0
howManyTimes = 0


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

def reply(time):
    answer_str = input(f"你猜(第{time}次)")
    if answer_str =="stop" :
        return False
    if len(answer_str) != 4 :
        print("錯誤")
        reply(time)
    for i in range(4):
        answer[i] = int(answer_str[i])
    #print("answer:",answer)
    return True

def check():
    global howManyA,howManyB
    for i in range(4):
        for j in range(4):
            if(answer[i] == question[j]):
                if(i==j):
                    howManyA +=1
                else:
                    howManyB +=1
    print(howManyA,"A",howManyB,"B")
    if(howManyA == 4):
        return False
    return True


created()
i = True
while i==True:
    howManyTimes +=1
    if(reply(howManyTimes) == False):
        print("停止")
        break
    if(check() == False):
        print("猜對了")
        print("共花了",howManyTimes,"次")
        break
    howManyA = 0
    howManyB = 0