import json

players = [
    {
        "id": 1,
        "first_name": "Hans",
        "last_name": "Niemann",
        "elo_points": 1882
    },
    {
        "id": 2,
        "first_name": "Anish",
        "last_name": "Giri",
        "elo_points": 2547
    },
    {
        "id": 3,
        "first_name": "Anna",
        "last_name": "Cramling",
        "elo_points": 2235
    },
    {
        "id": 4,
        "first_name": "Magnus",
        "last_name": "Carlsen",
        "elo_points": 2878
    },
    {
        "id": 5,
        "first_name": "Hikaru",
        "last_name": "Nakamura",
        "elo_points": 2659
    },
    {
        "id": 6,
        "first_name": "Dina",
        "last_name": "Belenkaya",
        "elo_points": 2456
    }
]

n_players = len(players)

def tri_classement(players:list()) -> list():

    # Algorithme de tri à bulle classique
    for i in range(n_players):
        for j in range(n_players-i-1):
            if(players[j]['elo_points'] < players[j+1]['elo_points']):
                players[j], players[j+1] = players[j+1], players[j]

def build_tree(players:list()) -> list():

    group_1 = []
    group_2 = []

    # Séparation des joueurs dans les 2 groupes
    for i in range(n_players//2):
        group_1.append(players[i])
    for j in range((n_players//2), n_players):
        group_2.append(players[j])

    matches = []


    # Construction des matchs
    for k in range(n_players//2):

        # Construction des affrontements pour garder toutes les données des joueurs et ajout d'un champ affrontement_id
        affrontement = {
            'affrontement_id' : k+1,
            'player_1' : group_1[k],
            'player_2' : group_2[k]
        }
        matches.append(affrontement)
    
    # En sortie : une liste de dictionnaire, chaque dictionnaire comporte un champ affrontement_id, et un dictionnaire par joueur, chaque dictionnaire de joueur comporte ses données
    return matches

def build_tree_json(players:list()) -> None:

    matches = build_tree(players)
    
    # Dump de la liste des affrontements dans le json
    json_data = json.dumps(matches, indent=4)
    with open('matches.json','w') as outfile:
        outfile.write(json_data)

    print('\nJSON file created\n')

def affichage_matches(matches:list()) -> None:

    print('----------------------------------------------------------------')

    for i in range(len(matches)):
        print(f"Affrontement {matches[i]['affrontement_id']}")
        print(f"{matches[i]['player_1']['first_name']} {matches[i]['player_1']['last_name']} ({matches[i]['player_1']['elo_points']}) vs {matches[i]['player_2']['first_name']} {matches[i]['player_2']['last_name']} ({matches[i]['player_2']['elo_points']})")
        print('----------------------------------------------------------------')

if __name__ == '__main__':

    # Tri des joueurs selon leur elo
    tri_classement(players) 

    # Méthode 1 : création du json
    build_tree_json(players) 
    # Méthode 2 : retour de la structure de donnée
    matches = build_tree(players) 
    affichage_matches(matches)