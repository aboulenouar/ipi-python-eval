import random

minuscules = 'abcdefghijklmnopqrstuvwxyz'
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chiffres = '0123456789'
special = '()[]:;!'
characters = f'{minuscules}{majuscules}{chiffres}{special}'


def generate(longueur:int) -> str:

    password = ''

    # Prends un caractère au hasard dans la liste à chaque itération
    for i in range(longueur):
        password += random.choice(characters)
    
    return password

if __name__ == '__main__':


    print('Longueur du mot de passe (entrez un nombre)')
    longueur = ''

    # Vérifie que l'utilisateur entre bien un nombre pour la longueur
    while(not longueur.isdigit()):
        longueur = input('> ')

    longueur = int(longueur)

    print(generate(longueur))
    