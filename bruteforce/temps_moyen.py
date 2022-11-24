from bruteforce import bruteforce
from password_generator import generate
import time

def avg_time(length:int) -> float:

    total_time = 0

    # Generation aléatoire et bruteforce de 10 mdp
    for i in range(10):
        password = generate(length)

        start = time.time()
        bruteforce(password)
        end = time.time()
        
        total_time += end - start

    return total_time/10

if __name__ == '__main__':
    print('Pour quelle longueur de mot de passe voulez vous connaître le temps moyen')
    print('3 : 3 caractères\n4 : 4 caractères')

    length = 0

    while(length != 3 and length != 4):
        length = int(input('> '))

    print('Bruteforce en cours...')

    average = avg_time(length)

    print(f'Pour un mot de passe de {length} caractères, cet ordinateur mettra en moyenne {round(average,3)}s à le craquer')
