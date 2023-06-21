import random

with open('text', 'r') as file:
    data = file.read()
with open('initialSequence', 'r') as file:
    init_sequence = file.read()

length = int(input("now write length the genereted text shall has::\n"))
n = len(init_sequence)
text = data

training_set = list(text)
generated_set = []

n_set = list(init_sequence)
for x in n_set:
    generated_set.append(x)

numOfChar = {}

for x in text:
    if x not in numOfChar:
        numOfChar[x] = 0


def fun1(keyList):  # zwraca znak z listy znaków bazując na akt numOfChar
    if generated_set[len(generated_set) - 1] in keyList:
        keyList.remove(generated_set[len(generated_set) - 1])
    if len(keyList) == 0:  # TODO WYWALIĆ TO
        print("returning @ errrrrror")
        return '@'

    max = []
    maxVal = 0

    for x in keyList:
        if numOfChar[x] > maxVal:
            max.clear()
            max.append(x)
        elif numOfChar[x] == maxVal:
            max.append(x)

    tmpKeyList = keyList
    for x in max:
        tmpKeyList.remove(x)

    if len(max) == 0:
        fun1(tmpKeyList)

    elif len(max) > 0:
        result = random.choice(max)
        return result


def funForN0():
    for x in training_set:
        if x not in numOfChar:
            numOfChar[x] = 1
        else:
            numOfChar[x] = numOfChar[x] + 1

    tmp = []
    for x in numOfChar:
        if numOfChar[x] > 0:
            tmp.append(x)

    generated_set.append(fun1(tmp))


def fun2(n, init):
    numOfChar = {}

    for i in range(0, len(training_set) - n):

        notTheSameFlag = False
        for x in range(0, len(init)):
            if init[x] != training_set[x + i]:
                notTheSameFlag = True

        if notTheSameFlag == False:

            if training_set[n + i] not in numOfChar:
                numOfChar[training_set[n + i]] = 1
            else:
                numOfChar[training_set[n + i]] = numOfChar[training_set[n + i]] + 1

    tmpList = []

    for x in numOfChar:
        if numOfChar[x] > 0 and x not in tmpList:
            tmpList.append(x)

    if len(tmpList) == 0 or len(tmpList) == 1 and generated_set[len(generated_set) - 1] in tmpList:
        if len(init) == 0:
            print("appended @ ERRRROR")
            generated_set.append('@')
        elif len(init) == 1:
            funForN0()
        elif len(init) > 1:

            init.remove(init[0])
            fun2(n - 1, init)

    else:

        generated_set.append(fun1(tmpList))


while len(generated_set) < length:

    if n == 0:
        funForN0()

    else:
        fun2(n, n_set)

result = "".join(generated_set)
print(result)

with open('result', 'w') as file:
    file.write(result)