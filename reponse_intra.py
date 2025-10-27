##########################################
# Brisebois, Charlotte, <6304598>
##########################################

import random
import mathplotlib.pyplot as plt
import numpy as np



def temperature_journaliere():

    jour= 0
    temperature_froide= 24
    temperature_chaude=30

    temperature= round(random.uniform(20,35),1)
    for temperature in range(10):
        if temperature < temperature_froide:
            print('Trop froid')
        elif temperature > temperature_chaude:
             print('Trop chaud')
        else:
             print('OK')
             jour=+1

        print('Jour', jour, ':', temperature, end='')

temperature_journaliere()





def population_bacterie(taux_initial):

    taux= np.pi/1.5

    population= taux
    heure= [1,2,3,4,5,6,7,8,9,10]


    plt.figure(figsize=(10,10))
    plt.plot(population,heure, '*b')
    plt.plot([0,50000],[10,50000],'-r')
    plt.xlim(0,11)
    plt.ylim(0, 160000)
    plt.title('Croissance bactérienne')
    plt.xlabel('Heure')
    plt.ylabel('Population')
    plt.grid()
    plt.show()

population_bacterie(100)