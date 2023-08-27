import random
import math
from statistics import mean


def inverse(x, alpha):
    return -(alpha * math.log(1-x))

def loop(TA, TS, Q, c, alpha, beta, Q_total, count):
        Q_total += Q
        count += 1
        if TA < TS:
            TS = TS-TA
            c += TA
            Q += 1
            x = random.random()
            TA = inverse(x, alpha)
            #print(f"Running the arrival loop and TA is {TA:.4f}, TS is {TS:.4f}")
        else:
            TA -= TS
            c += TS
            Q -= 1
            y = random.random()
            TS = inverse(y, beta)
            #print(f"Running the service loop and TA is {TA:.4f}, TS is {TS:.4f}")
        return Q, TA, TS, c, Q_total, count

def block(TA, c, Q, alpha, Q_total, count):
    Q_total += Q
    count += 1
    c += TA
    Q += 1
    x = random.random()
    TA = inverse(x, alpha)
    #print(f"Running block, TA is {TA}")
    return Q, TA, TS, c, Q_total, count

def accuracy_fn(alpha, beta, average):
    p = beta / alpha
    estimate = p/(1-p)
    acc = abs(((average-estimate)/estimate) * 100)
    print(f"Deviation is: {acc:.4f}% | estimate is:{estimate}\nAverage is {average}\n")
    return acc


accuracy_accumulator = []
for l in range(10):
    TA, TS = 0, 0
    Q = 1
    c = 0
    alpha = random.randint(2,30)
    beta = random.randint(1,alpha - 1)
    print(f"===== Alpha is: {alpha}, beta is: {beta} =====")

    results = []
    service = 0
    arrival = 0

    Q_total = 1
    count = 0

    epochs = 100

    for x in range(epochs):
        for i in range(epochs):
            while Q != 0:
                Q, TA, TS, c, Q_total, count = loop(TA, TS, Q, c, alpha, beta, Q_total, count)
            Q, TA, TS, c, Q_total, count= block(TA, c, Q, alpha, Q_total, count)

        results.append(Q_total/count)

    average = mean(results)
    acc = accuracy_fn(alpha,beta,average)
    
    accuracy_accumulator.append(acc)
print(f"Mean accuracy is {mean(accuracy_accumulator):.4f}%")




    





