import streamlit as st

image_path='images/'
st.set_page_config(page_title="FormulOfus",page_icon=image_path+"logo_InvRoxx_tab.png",layout="centered")

st.sidebar.image(image_path+"logo_nom_transp.png" )

def source(texte,lien=False):
    if lien:
        st.markdown(
            '<div style="font-size: 0.9em; color: gray;">'
            '<b>Source :</b> '
            f'<a href="{lien}" target="_blank">{texte}</a>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div style="font-size: 0.9em; color: gray;">'
            f'<b>Source : {texte}</b> '
            '</div>',
            unsafe_allow_html=True
        )


class Toc:

    def __init__(self):
        self._items = []
        self._placeholder = None
    
    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text,divider="gray"):
        # self._markdown(text, "h2", " " * 2)
        level="h2"
        space=" " * 2
        key = "-".join(filter(str.isalnum, text)).lower()

        # st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        st.header(text,divider="gray")
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=False):
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()

    def generate(self):
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)
    
    def _markdown(self, text, level, space=""):
        key = "".join(filter(str.isalnum, text)).lower()

        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


toc = Toc()

st.title("LES FORMULES DE DOFUS TOUCH")
st.header("Sommaire")
toc.placeholder()

# toc.title("1")

# for a in range(10):
#     st.write("Blabla...")

# toc.header("Header 1")

# for a in range(10):
#     st.write("Blabla...")

# toc.header("Header 2")

# for a in range(10):
#     st.write("Blabla...")

# toc.subheader("Subheader 1")

# for a in range(10):
#     st.write("Blabla...")

# toc.subheader("Subheader 2")

# for a in range(10):
#     st.write("Blabla...")
















# st.markdown("""
# ## __Sommaire :__
# """)
# st.page_link("https://calcofus.fr/formulofus#3-resistances-reductions-de-degats",label="degats")
toc.header("1. Lignes de sorts",divider="gray")
# st.divider()
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_1")

st.markdown("""
Pour déterminer les dégâts d'un Sort, sont pris en compte :
- Les dégâts de **Base** du Sort (exemple pour flamiche ce sera un nombre entre 8 et 10)
- La Caractéristique de l'élément (Neutre ou Terre = Force, Feu = Intelligence, ...)
- La puissance
- Les dommages fixes (les dommages élémentaires + dommages non élémentaires)
- Les dommages critiques lors des coups critiques
- Pour le soin c'est la même formule mais avec la stat **soin** à la place des dommages
""")

st.subheader("Formules :")
st.latex(r'''
\text{Dégâts} = \text{Base} \times \frac{100 + \text{Stats} + \text{Puissance}}{100} + \text{Dommages} \, (+\text{DoCrit si cc})
''')

st.latex(r'''
\text{Soins} = \text{Base} \times \frac{100 + \text{Intelligence}}{100} + \text{Stat soin}
''')

st.subheader("Exemple :")
st.markdown("Un joueur ayant 800 d'intelligence, 200 de puissance, 90 dommages feu et 10 dommages non élémentaires, les dégats qu'il fera à la flamiche seront :")
st.latex(r'''
\text{Dégâts minimum} = 8 \times \frac{100 + 800 + 200}{100} + \left( 90 + 10 \right) = 188 
''')
st.latex(r'''
\text{Dégâts maximum} = 11 \times \frac{100 + 800 + 200}{100} + \left( 90 + 10 \right) = 221 
''')
st.markdown("Lors des cc on a juste des lignes de dégats de base plus élevées et on ajoute les dommages critiques.")
toc.header("2. Sorts de réductions de dégats",divider="gray")
# st.header("2. Sorts de réductions de dégats",divider="gray")
# st.divider()

source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_8")
st.markdown("""
Sorts comme rempart ou armure de sel qui appliquent une réduction fixe.\n
Cette réduction s'applique après les résistances fixes et % mais avant les %dommages finaux.
""")
st.subheader("Formule :")
st.latex(r'''
\text{Réduction} = \text{Base} \times \frac{100 + 5 \times \text{Lvl lançeur}}{100}
''')
st.subheader("Exemple :")
st.latex(r'''
\text{Rempart Lvl 6 Joueur Lvl 200} : \text{Réduction} = 13 \times \frac{100 + 5 \times 200}{100} = 143
''')
toc.header("3. Résistances/Réductions de dégats",divider="gray")
# st.divider()
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_9")
st.markdown("""
Pour déterminer les dégats finaux, sont pris en compte dans l'ordre:
- Résistances Fixes (résistances élémentaires & résistances critiques)
- Résistances %
- Sorts de réduction de dommages type rempart
- % dommages subis ou occasionnés
""")
st.subheader("Formule :")
st.latex(r'''
\text{Dégats finaux} = ((\text{Dégats} - \text{Résistances fixes}) \times (1-\frac{ \text{Résistances\%} }{100}) - \text{sorts de réduction}) \times \text{\%dommages subis}
''')
st.subheader("Exemple :")
st.markdown("""
Un joueur reçoit une attaque feu faisant 1000 de dégats sur poutch, il a :
- 50 résistances fixes feu
- 30% résistances feu
- un rempart sur lui
- une vulnérabilité sur lui (x115% dommages subis)
""")
st.latex(r'''
\text{Dégâts après Ré fixes} = 1000 - 50 = 950
''')
st.latex(r'''
\text{Dégâts après Ré \%} = 950 \times (1- \frac{30}{100}) = 950 \times 0.7 = 665
''')
st.latex(r'''
\text{Dégâts après Rempart} = 665-143=522
''')

st.latex(r'''
\text{Dégâts après Vulnérabilité} = 522 \times 1.15 = 600.3 \text{ arrondi à 600}
''')


toc.header("4. Dégats et résistances de poussée",divider="gray")
st.markdown("""Pour déterminer les dégats lors d'une poussée, sont pris en compte:
- Les dommages de poussée (dopou) du pousseur 
- Les résistances de poussée (répou) de la cible
- Le nombre de cases de la poussée
- Le niveau du pousseur (lvl)
            
Détails sur le comptage des cases de poussée :
- si un joueur subi une poussée de 4 mais qu'il doit parcourir 2 cases avant d'atteindre le mur, alors on compte que 2 cases pour les dégats de poussée
- une case de poussée en diagonale correspond à 2 cases en ligne 
- Pour les poussées en diagonale les déplacements sont arrondis à l'entier supérieur, avec un tacheté un ressac aura une poussée de 5 donc arrondi à 3 en diagonale
- Si le déplacement est arrondi les dégats ne le sont pas, les dégats d'un ressac avec tacheté sera quand même compté comme une poussée de 5 même si le déplacement est de 3 en diagonale.
""")
st.subheader("Formule:")
st.latex(r'''
\text{Dégâts} = (\frac{\text{lvl}}{2}+\text{dopou}-\text{répou}+32) \times \frac{\text{nb cases de poussée}}{4}
''')

st.subheader("Exemple:")
st.markdown("""Un joueur lvl 200 a 500 de dopou et un tacheté, la cible a 50 de répou est est collée à un mur, les dégats d'une libération lvl 6 (4 cases de poussée de base + 1 tacheté ) seront:
""")
st.latex(r'''
\text{Dégâts} = (\frac{200}{2}+500-50+32) \times \frac{4+1}{4} = 583 \times 1.25 = 728.75 \text{ arrondi à } 728
''')

toc.header("5. Tacle/Fuite",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_14")

toc.header("6. Retrait/Esquive",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_7")
st.markdown(""" Pour déterminer les chances de retirer des PA ou PM, sont pris en compte:
- La stat retrait PA ou PM du lanceur
- La stat esquive PA ou PM de la cible
- Le nombre de PA ou PM totaux de la cible.
- Le nombre de PA ou PM restants de la cible au moment du retrait

Les retraits sont considérés un par un,c'est à dire qu'il est équivalent de tenter de retirer 5 fois un PA ou 5 PA d'un coup. Lorsqu'un PA/PM est retiré, le nombre de PA/PM restants de la cible est modifié pour le retrait suivant.

   pourcentage de chance de retirer un PA = PA ou PM restants de la cible/PA ou PM totaux de la cible x Retrait du lanceur/esquive de la cible. x 1/2          
""")



st.subheader("Formule:")
st.latex(r'''
\text{Probabilité de retirer un PA/PM} = \frac{\text{PA/PM restants de la cible}}{\text{PA/PM totaux de la cible}} \times \frac{\text{retrait du lanceur}}{2 \times \text{esquive de la cible}}
''')
st.markdown("""
Les probabilités d'effectuer une esquive sont calculées de la même manière :
""")
st.latex(r'''
\text{Probabilité d'esquive} = 1 -\text{ Probabilité de retrait}
''')

st.subheader("Exemple:")
st.markdown("""Un xelor a 90 de retrait PA et utilise ralentissement (-2 PA) sur une cible ayant 50 d'esquive pa et 10 pa sur 12 totaux car elle s'est déjà fait retirer 2 PA par un précédent ralentissement.

La probabilité R1 de retirer le premier PA est de :
""")
st.latex(r'''
\text{R1} = \frac{10}{12} \times \frac{90}{2 \times 50} = 0.75
''')
st.markdown("""On a donc 75% de chance de retirer le premier PA, si ça échoue la probabilité de retirer le second est la même.
Si le retrait passe, la probabilité R2 de retirer le second PA est alors :
""")
st.latex(r'''
\text{R2} = \frac{9}{12} \times \frac{90}{2 \times 50} = 0.675
''')
st.markdown("""On a donc 67.5% de chance de retirer le second PA.

On peut calculer les probabilités de retirer 0 *(P0)*, 1 *(P1)* ou 2 *(P2)* PA avec le ralentissement :
- P2 : les deux retraits R1 & R2 passent
- P0 : le retrait R1 échoue deux fois
- P1 : soit le R1 passe et R2 échoue soit R1 échoue une fois puis passe
""")
st.latex(r'''
\text{P2} = \text{R1} \times \text{R2} = 0.75 \times 0.675 = 0.50625 \approx 50\%
''')
st.latex(r'''
\text{P0} = (1-\text{R1}) \times (1-\text{R1}) = 0.25 \times 0.25 = 0.0625 \approx 6\%
''')
st.latex(r'''
\text{P2} = \text{R1} \times (1-\text{R2}) + (1-\text{R1}) \times \text{R1}  = 0.75 \times 0.325 +  0.25 \times 0.75 =  0.43125 \approx 43\%
''')
toc.header("7. Invocations Osamodas",divider="gray")
source("Warp")
toc.header("8. Bombes",divider="gray")
source("Emrys")

st.divider()
st.caption("L'objectif de cette page est de rassembler les différentes formules de calcul et données utiles à connaître dans le jeu, tant pour le quotidien que le théorycraft.")
toc.generate()
