
minuscules = 'abcdefghijklmnopqrstuvwxyz'
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chiffres = '0123456789'
special = '()[]:;!'
characters = f'{minuscules}{majuscules}{chiffres}{special}'


print('Le calcul du nombre de combinaisons possibles pour un mot de passe est le suivant :')
print('Nombre de caractères possibles à la puissance de la longueur du mot de passe.\n')
print('Dans notre cas, on a 26 lettres en minuscule, 26 lettres en majuscule, 10 chiffres (de 0 à 9)')
print(f'Et 7 caractères spéciaux. Ce qui nous fait un total de {len(characters)} caractères\n')
print(f'Pour un mot de passe de 6 caractères, il y aura donc {len(characters)}^6 soit {len(characters)**6} combinaisons possibles')

