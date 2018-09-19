import matplotlib.pyplot as plt
import  random
stake  = 100
lose = 0
win = 200
trial = 100
step=[stake];
steps= [[]]
for i in range(100):
    for t in range(trial):
        if stake < win and stake > lose:
            random.seed(random.random())
            randomNum = random.random()
            if(randomNum>0.3):
                stake = stake +1
            else:
                stake = stake - 1
            step.append(stake)
        elif not(stake < win and stake > lose):
            break
    steps.append(step)


plt.plot(steps[0],color = 'blue')
plt.plot(steps[1],color = 'red')
plt.plot(steps[2],color = 'green')
plt.show()


