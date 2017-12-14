from random import*

# le paquet de carte
paquet = list(range(1, 109))

# le pile de jeu
pile = ['test']

# distribuer une couleur et le contenu à chacun
couleur = ['rouge'] * 25 + ['bleu'] * 25 + \
    ['vert'] * 25 + ['jaune'] * 25 + ['noir'] * 8
contenu = (list(range(10)) + list(range(1, 10)) +
           ['+2', 'passer tour', 'change sens'] * 2) * 4 + \
    ['+2'] * 4 + ['+4'] * 4
dict_couleur = dict(zip(paquet, couleur))
dict_contenu = dict(zip(paquet, contenu))

joueur_nom = {}
joueur_main = {}

pioche = 0

sens = 1

nombre_joueur = 0
nombre_carte = 0


def afficher_carte(indice):
    return dict_contenu[indice], dict_couleur[indice]


def piocher(main_du_joueur, nombre):
    for i in range(1, nombre + 1):
        main_du_joueur.append(paquet.pop(-1))


def afficher_main(main_du_joueur):
    for i in range(len(main_du_joueur)):
        print('Carte', i + 1, ':')
        print(afficher_carte(main_du_joueur[i]))


def pioche_vide(nombre_a_pioche):
    if len(paquet) < nombre_a_pioche:
        paquet = list(paquet) + list[shuffle(pile[0:-1])]


def verfication(indice):
    if pile[-1] == 'test':
        return True
    elif dict_couleur[indice] == dict_couleur[pile[-1]]:
        return True
    elif isinstance(dict_contenu[indice], int) and \
            dict_contenu[indice] == dict_contenu[pile[-1]]:
        return True
    elif dict_couleur[indice] == 'noir':
        if dict_contenu[indice] == '+4':
            return True
        elif dict_contenu[pile[-1]] != '+4':
            return True
    else:
        return False


def nombre_pioche(centrale_contenu):
    if centrale_contenu == '+2':
        pioche += 2
    elif centrale_contenu == '+4':
        pioche += 4


def jouer(indice, main_du_joueur):
    if indice == 0:
        piocher(main_du_joueur, 1)
    else:
        while indice > len(main_du_joueur) or \
                not verfication(main_du_joueur[indice - 1]):
            print('Carte invalide, ressayez.')
            indice = int(
                input('Quelle carte voulez-vous jouer? Ou tapez 0 pour piocher une carte. '))
        if indice == 0:
            piocher(main_du_joueur, 1)
        else:
            pile.append(main_du_joueur.pop(indice - 1))
            
def gestion_init(nombre_joueur, nombre_carte):
    for i in range(1, nombre_joueur + 1):
        joueur_main[i] = []
        joueur_nom[i] = input('Le nom de joueur est ')
        for j in range(nombre_carte):
            joueur_main[i].append(paquet.pop(-1))


def victoire(joueur_main):
    return len(joueur_main) == 0


def tour(numero_joueur):
    global pioche
    global sens
    global joueur
    afficher_main(joueur_main[numero_joueur])
    if pioche != 0:
        i = True
        for j in joueur_main[numero_joueur]:
            if dict_contenu[joueur_main[numero_joueur][j]] == '+4':
                i = i and True
            elif dict_contenu[joueur_main[numero_joueur][j]] == '+2':
                i = i and verfication(joueur_main[numero_joueur][j])
            else:
                i = i and False
        if not i:
            piocher(joueur_main[numero_joueur], pioche)
            pioche = 0
        joueur = joueur + sens
    else:
        carte_a_jouer = int(
            input('Quelle carte voulez-vous jouer? Ou tapez 0 pour piocher une carte. '))
        jouer(carte_a_jouer, joueur_main[numero_joueur])
        if dict_contenu[pile[-1]] == '+4':
            pioche = pioche + 4
            joueur = joueur + sens
        elif dict_contenu[pile[-1]] == '+2':
            pioche = pioche + 4
            joueur = joueur + sens
        elif dict_contenu[pile[-1]] == 'passer tour':
            joueur = joueur + sens * 2
        elif dict_contenu[pile[-1]] == 'changer sens':
            sens = -sens
            joueur = joueur + sens
        else:
            joueur = joueur + sens
    if joueur > nombre_joueur:
        joueur = joueur - nombre_joueur
    elif joueur <= 0:
        joueur = joueur + nombre_joueur
    if pile[-1] != 'test':
        print('La carte jouee est ', afficher_carte(pile[-1]))
    print('Le prochain joueur est: ', joueur_nom[joueur])

# mélanger le paquet
shuffle(paquet)

nombre_joueur = int(input('Combien de joueur? '))
nombre_carte = int(input('Combien de carte pour chacun? '))

joueur = 1

gestion_init(nombre_joueur, nombre_carte)

while joueur in range(1, 6):
    tour(joueur)
