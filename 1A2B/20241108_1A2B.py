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

def reply():
    answer_str = str(input("你猜"))
    for i in range(4):
        answer[i] = int(answer_str[i])
    print("answer:",answer)

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


created()
i = True
while i==True:
    howManyTimes +=1
    reply()
    check()
    if(howManyA == 4):
        break
    howManyA = 0
    howManyB = 0
print("猜對了")
print("共花了",howManyTimes,"次")