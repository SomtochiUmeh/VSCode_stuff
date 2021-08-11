import matplotlib.pyplot as plt
import random

def simulate_news(n):
    day = 1
    heard = 1
    not_heard = n-1

    lheard = [heard]
    lnot_heard = [not_heard]

    while lnot_heard[-1] > 0:
        new_heard = 0.03*not_heard +random.uniform(-2,2)
        heard += new_heard
        not_heard -= new_heard

        lheard.append(heard)
        lnot_heard.append(not_heard)
        day += 1

    plt.plot(range(1, day+1), lheard)
    plt.plot(range(1, day+1), lnot_heard)

    plt.xlabel('Days')
    plt.ylabel('Number of people')
    plt.title('Minervapolis News Spread')
    plt.legend(['Knows the news', 'Do not know the news'], loc='center right')
    plt.show()

    return day

simulate_news(1000)