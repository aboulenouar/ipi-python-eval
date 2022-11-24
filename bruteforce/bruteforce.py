import itertools
import time

minuscules = 'abcdefghijklmnopqrstuvwxyz'
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chiffres = '0123456789'
special = '()[]:;!'
characters = f'{minuscules}{majuscules}{chiffres}{special}'

def bruteforce(password:str) -> str:
    
    # itertools.product va produire toutes les combinaisons possibles parmis les characters en paramètre
    # itertools.product permet également d'autoriser les répétitions (nombre de répétitions via le param 'repeat')
    # On utilise ''.join pour transformer le tuple en string pour le comparer au password
    for possible_password in itertools.product(characters, repeat = len(password)):
        if(''.join(possible_password) == password):
            return ''.join(possible_password)
            
def isValid(password:str) -> bool:
    
    # Vérifie que le mot de passe entré par l'utilisateur ne contient pas de lettre "illégale" (non comprise dans 'characters')
    for letter in password:
        if(letter not in characters):
            return False
    return True

if __name__ == '__main__':

    print('Mot de passe à bruteforce (1 à 6 caractères)')
    
    password = ''

    # Vérifie que l'utilisateur entre un mot de passe valide
    while(len(password) < 1 or len(password) > 6 or not isValid(password)):
        password = input('> ')

    print('Bruteforce en cours...')

    # Calcule du temps à bruteforce le password
    start = time.time()
    password_bruteforce = bruteforce(password)
    end = time.time()

    print(f'Password cracked ! ({password_bruteforce})')
    print(f"Elapsed time: {end - start}s")

