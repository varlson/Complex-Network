import matplotlib.pyplot as plt
from random import randint as rand

all =[]

def gen(n):
    return [rand(3, 17) for x in range(n)]

fig, ax = plt.subplots(3,3)


def man():
    global all

    for i in range(9):
        all.append(plt.plot(gen(4), gen(4)))
    count=0
    for i in range(3):
        for k in range(3):
            ax[i][k] = all[count]
            count+=1

man()
fig.savefig('t.png')
