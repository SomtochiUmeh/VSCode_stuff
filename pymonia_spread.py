# TODO: You can put your code here:
import random
import matplotlib.pyplot as plt

def simulate_pandemic(healthy: int) -> None:
    n_infected = 2  # number of infected people
    n_immune = 0  # number of immune people
    n_healthy = healthy  # number of healthy people

    lhealthy = [healthy]  # These 3 lists are initialized with values from day 0
    infected = [2]
    immune = [0]
    fluctuation = random.uniform  # function to add random fluctuations/deviations in the data, without which our graphs will be perfectly smooth
    l = (-2, 2)
    n_days = 500
    for i in range(n_days):
        newly_infected = (n_infected / (5 * healthy)) * n_healthy + fluctuation(*l)  # the immune come from the infected
        n_infected += newly_infected
        n_healthy -= newly_infected  # values are updated

        newly_immune = 0.01 * n_infected + fluctuation(*l)  # the immune come from the infected
        n_immune += newly_immune
        n_infected -= newly_immune  # values are updated

        newly_healthy = 0.04 * n_infected + fluctuation(*l)  # the healthy come from the infected
        n_healthy += newly_healthy
        n_infected -= newly_healthy  # values are updated

        lhealthy.append(n_healthy)
        infected.append(n_infected)
        immune.append(n_immune)  # we append the values for that day to the correponding list

    for y in (lhealthy, infected, immune):
        plt.plot(range(n_days + 1), y)  # after getting all values, we plot each with one extra day, day 0
    plt.legend(["Healthy", "Infected", "Immune"])
    plt.xlabel("Time(Days)")
    plt.ylabel("Number of people")
    plt.title("Spread of Pymonia over time")
    plt.show()


simulate_pandemic(1000)