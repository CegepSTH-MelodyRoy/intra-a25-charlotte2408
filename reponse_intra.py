##########################################
# Brisebois, Charlotte, <6304598>
##########################################

import random
import matplotlib.pyplot as plt
import numpy as np


#Question 1
def temperature_journaliere():

    jour= 1
    temperature_froide=24
    temperature_chaude=30
    for temperature in range(10):
        t= round(random.randint(20,35),1)
        if t > temperature_froide:
            print('Trop froid')

        elif t > temperature_chaude:
             print('Trop chaud')
        else:
            print('OK')





        jour=+1
        print('Jour', jour, ':', t)
    print('Fin')
temperature_journaliere()




#Question 2
def population_bacterie(taux_initial):

    taux= np.pi/1.5

    population= taux
    heure= [1,2,3,4,5,6,7,8,9,10]


    plt.figure(figsize=(10,10))
    plt.plot(population,heure, '*b')
    plt.plot([0,50000],[10,50000],'-r')
    plt.xlim(0,11)
    plt.ylim(0,160000)
    plt.title('Croissance bactérienne')
    plt.xlabel('Heure')
    plt.ylabel('Population')
    plt.grid()
    plt.show()

