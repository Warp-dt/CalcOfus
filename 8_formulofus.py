import streamlit as st
import unicodedata

image_path='images/'
st.set_page_config(page_title="FormulOfus",layout="wide")

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

        # Normalize the string
        n= unicodedata.normalize('NFKD', text)  

        res = ''.join([c for c in n if not unicodedata.combining(c)])  

        key ="-".join(res.replace(". "," ").replace("/"," ").split(" ")).lower()
        # key = "-".join(filter(str.isalnum, text)).lower()

        # st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        st.header(text,divider=divider)
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

st.html('<div style="text-align: center; font-size: 50px;font-weight: bold"> LES FORMULES DE DOFUS TOUCH </div>')
st.header("Sommaire")
toc.placeholder()

toc.header("1. Lignes de sorts",divider="gray")
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
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_8")
st.markdown("""
Sorts comme rempart ou armure de sel qui appliquent une réduction fixe.\n
Cette réduction s'applique en même temps que les résistances fixes, avant les résistances %.
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
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_9")
st.markdown("""
Pour déterminer les dégats finaux, sont pris en compte dans l'ordre :
- Résistances Fixes (résistances élémentaires & résistances critiques)
- Résistances %
- Sorts de réduction de dommages type rempart
- % dommages subis ou occasionnés
""")
st.subheader("Formule :")
st.latex(r'''
\text{Dégats finaux} = (\text{Dégats} - \text{Résistances fixes} - \text{sorts de réduction}) \times (1-\frac{ \text{Résistances\%} }{100}) \times \text{\%dommages subis}
''')
st.subheader("Exemple :")
st.markdown("""
Un joueur reçoit une attaque feu faisant 1000 de dégats sur poutch, il a :
- 50 résistances fixes feu
- 30% résistances feu
- un rempart
- une vulnérabilité (x115% dommages subis)
""")
st.latex(r'''
\text{Dégâts après Ré fixes} = 1000 - 50 - 143 = 807
''')
st.latex(r'''
\text{Dégâts après Ré \%} = 807 \times (1- \frac{30}{100}) = 807 \times 0.7 = 564.9
''')

st.latex(r'''
\text{Dégâts après Vulnérabilité} = 564.9 \times 1.15 = 649,635 \text{ arrondi à 649}
''')


toc.header("4. Dégats et résistances de poussée",divider="gray")
st.markdown("""Pour déterminer les dégats lors d'une poussée, sont pris en compte :
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
st.subheader("Formule :")
st.latex(r'''
\text{Dégâts} = (\frac{\text{lvl}}{2}+\text{dopou}-\text{répou}+32) \times \frac{\text{nb cases de poussée}}{4}
''')

st.subheader("Exemple :")
st.markdown("""Un joueur lvl 200 a 500 de dopou et un tacheté, la cible a 50 de répou est est collée à un mur, les dégats d'une libération lvl 6 (4 cases de poussée de base + 1 tacheté ) seront :
""")
st.latex(r'''
\text{Dégâts} = (\frac{200}{2}+500-50+32) \times \frac{4+1}{4} = 583 \times 1.25 = 728.75 \text{ arrondi à } 728
''')


toc.header("5. Tacle/Fuite",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_14")
st.markdown("""
Pour déterminer les Pa et Pm restants du fuyard après avoir détaclé, sont pris en compte :
- Le tacle du tacleur
- La fuite du fuyard
- Les PA/PM du fuyard au moment où il tente de détacler
""")

st.subheader("Formule :")
st.markdown("Il faut d'abord calculer le **Coefficient** (Coef) de fuite :")
st.latex(r'''
\text{Coef} = \frac{\text{Fuite} + 2}{2 \times (\text{Tacle} + 2)}
''')
st.markdown("On multiplie ensuite ce **Coefficient** aux nombres de PA/PM actuels du fuyard pour obtenir ses PA/PM restants après avoir détaclé :")

st.latex(r'''
\text{PA/PM restants} = \text{PA/PM actuels} \times \text{Coef (arrondis à l'entier le plus proche, et si on est à .5 pile entre deux c'est supérieur)} 
''')
st.markdown("On voit donc que pour ne perdre à coup sûr aucun PA ni PM le Coef doit être à 1 ou plus donc :")
st.latex(r'''
\text{Fuite} \geq 2 \times \text{Tacle} + 2
''')

toc.header("6. Retrait/Esquive",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_7")
st.markdown(""" Pour déterminer les chances de retirer des PA ou PM, sont pris en compte :
- La stat retrait PA ou PM du lanceur
- La stat esquive PA ou PM de la cible
- Le nombre de PA ou PM totaux de la cible.
- Le nombre de PA ou PM restants de la cible au moment du retrait

Les retraits sont considérés un par un,c'est à dire qu'il est équivalent de tenter de retirer 5 fois un PA ou 5 PA d'un coup. Lorsqu'un PA/PM est retiré, le nombre de PA/PM restants de la cible est modifié pour le retrait suivant.

   pourcentage de chance de retirer un PA = PA ou PM restants de la cible/PA ou PM totaux de la cible x Retrait du lanceur/esquive de la cible. x 1/2          
""")



st.subheader("Formule :")
st.latex(r'''
\text{Probabilité de retirer un PA/PM} = \frac{\text{PA/PM restants de la cible}}{\text{PA/PM totaux de la cible}} \times \frac{\text{retrait du lanceur}}{2 \times \text{esquive de la cible}}
''')
st.markdown("""
Les probabilités d'effectuer une esquive sont calculées de la même manière :
""")
st.latex(r'''
\text{Probabilité d'esquive} = 1 -\text{ Probabilité de retrait}
''')

st.subheader("Exemple :")
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
st.subheader("Vitalité :")
st.markdown("""Pour calculer la vitalité des invocations sont pris en compte :
- Le niveau de l'invocation
- Le niveau de l'osamodas
- La vitalité de l'osamodas
- Deux caractéristiques propre à chaque invo : Le coefficient d'hérédité de la vitalité et la vitalité de base
""")

st.subheader("Formule :")

st.latex(r'''
\text{Vitalité invocation} = \text{Vita Base} + \text{Vita Coef} \times (\text{Vitalité osa} - 5 \times \text{Lvl osa} -50)
''')

st.subheader("Statistiques :")
st.markdown("""
Pour calculer les statistiques des invocations sont pris en compte:
- Les stats de base de l'invocation (dépend du lvl de l'invocation)
- Les stats de l'osamodas

Les invocations vont hériter de 50% de certaines stats de l'osamodas:
-	Intelligence/Chance/Agilité : 50% sont transmises aux invocations de l'élément (⚠️ les stats issues des parchemins & des points de caractéristiques investis **sont transmises** )
-	Dommages Feu/Eau/Air : 50% sont transmis aux invocations de l'élément
-	Soin : 50% sont transmis à la momie
-	Sagesse : 50% sont transmis au craqueleur

Donc notamment ne sont pas transmis :
-	Puissance
-	Dommages non élémentaires
-	Dommages critiques
-	% critiques
-	Tacle/Fuite


""")
st.subheader("Données par invocation :")
tab_dragcrap="""
| Lvl invo | Vita Base | Vita Coef | Stats Base |
| ----------- | ----------- | ----------- | ----------- |
| 1 | 100 + Lvl osa | 15% | 100 |
| 2 | 100 + Lvl osa | 15% | 150 |
| 3 | 100 + Lvl osa | 15% | 200 |
| 4 | 100 + Lvl osa | 15% | 250 |
| 5 | 100 + Lvl osa | 15% | 300 |
| 6 | 100 + Lvl osa | 20% | 350 |"""

tab_momie="""
| Lvl invo | Vita Base | Vita Coef | Stats Base |
| ----------- | ----------- | ----------- | ----------- |
| 1 | Lvl osa x 0.6 + 60 | 10% | 70 |
| 2 | Lvl osa x 0.6 + 60 | 10% | 105 |
| 3 | Lvl osa x 0.6 + 60 | 10% | 150 |
| 4 | Lvl osa x 0.6 + 60 | 10% | 180 |
| 5 | Lvl osa x 0.6 + 60 | 10% | 220 |
| 6 | Lvl osa x 0.6 + 60 | 15% | 350 |"""

tab_tofu="""
| Lvl invo | Vita Base | Vita Coef | Stats Base |
| ----------- | ----------- | ----------- | ----------- |
| 1 | Lvl osa x 0.6 + 60 | 10% | 100 |
| 2 | Lvl osa x 0.6 + 60 | 10% | 150 |
| 3 | Lvl osa x 0.6 + 60 | 10% | 200 |
| 4 | Lvl osa x 0.6 + 60 | 10% | 250 |
| 5 | Lvl osa x 0.6 + 60 | 10% | 300 |
| 6 | Lvl osa x 0.6 + 60 | 15% | 350 |"""

tab_craq="""
| Lvl invo | Vita Base | Vita Coef | Stats Base |
| ----------- | ----------- | ----------- | ----------- |
| 1 | 100 + Lvl osa | 10% | 10 |
| 2 | 100 + Lvl osa | 10% | 30 |
| 3 | 100 + Lvl osa | 10% | 50 |
| 4 | 100 + Lvl osa | 10% | 70 |
| 5 | 100 + Lvl osa | 15% | 100 |
| 6 | 100 + Lvl osa | 20% | 150 |"""

tab_bouf="""
| Lvl invo | Vita Base | Vita Coef | Stats Base |
| ----------- | ----------- | ----------- | ----------- |
| 1 | Lvl osa x 0.6 + 60 | 10% | 10 |
| 2 | Lvl osa x 0.6 + 60 | 10% | 30 |
| 3 | Lvl osa x 0.6 + 60 | 10% | 50 |
| 4 | Lvl osa x 0.6 + 60 | 10% | 70 |
| 5 | Lvl osa x 0.6 + 60 | 15% | 100 |
| 6 | Lvl osa x 0.6 + 60 | 20% | 150 |"""
st.markdown("- **Dragonnet rouge & Crapaud :**")
st.markdown(tab_dragcrap)
st.markdown("- **Momie koalak :**")
st.markdown(tab_momie)
st.markdown("- **Tofu :**")
st.markdown(tab_tofu)
st.markdown("- **Craqueleur :**")
st.markdown(tab_craq)
st.markdown("- **Bouftou :**")
st.markdown(tab_bouf)

toc.header("8. Bombes",divider="gray")
source("Emrys","https://www.youtube.com/@emrys30")
st.subheader("Vitalité :")
st.markdown("""Pour calculer la vitalité des bombes sont pris en compte :
- La vitalité du roublard
- Le niveau du roublard
- La vitalité de base de la bombe (dépend du lvl de la bombe)
- Le coefficient de transmission de la vitalité du roublard (dépend de l'élément de la bombe)
""")
st.markdown("#### Formule vitalité :")

st.latex(r'''
\text{Vitalité bombe} = (\text{vitalité roub} - 5 \times \text{lvl roub} +50) \times \text{coef vitalité} + \text{vitalité base bombe}
''')
st.subheader("Bonus combo :")
st.markdown("""Le bonus combo sur chaque bombe augmente de 20% pour les 5 premiers niveau puis de 30% sur les 5 suivants avec un maximum de 10 bonus combo à +250%

Lors d'une explosion ou d'un mur le bonus combo en % de toutes les bombes impliquées dans les dégats est sommé pour être appliqué aux dégats.
""")

st.subheader("Dégats :")
st.markdown("""Pour calculer les dégats ds bombes sont pris en compte :
- Les dégats de base de la bombe (dépend de son élément)
- Les stats et dommages du roublard (caractéristiques dans l'élément, puissance et dommages)
- Le bonus combo des bombes constituant le mur ou l'explosion
- La distance de la cible par rapport aux bombes
    - Dans un mur les dégats sont considérés à 0 PO
    - Dans une explosion la distance entre les bombes et la cible est prise en compte, au cac c'est 1PO, avec une case d'écart c'est 2 PO
- ⚠️Les boosts sont considérés différemment lors d'une explosion par rapport à un mur :
    - Pour les dégats d'un mur ne sont considérés que les boosts (puissances/dommages) présents sur le roublard, et les % dommages finaux occasionnés considérés sont ceux appliqués sur le roublard.
    - Lors d'une explosion en plus des boosts du roublard pour chaque bombe les boosts (puissances/dommages) présents sur elle sont aussi ajoutés, et les % dommages finaux occasionnés considérés sont ceux appliqués sur la bombe. 

Pour comprendre cette différence de comportement lors des murs et explosions il faut se dire que lors d'une explosion les bombes deviennent des entités à part entière, alors que le mur est en quelque sorte un sort du roublard. Cette distinction permet au roublard de faire des dégats avec ses bombes en les faisant exploser même si il est sous corruption par exemple.
"""
)

st.markdown("#### Formule :")
st.markdown('Les éléments en italique ne sont appliqués que lors des *explosions*.')
st.latex(r'''
\text{Dégats avant bonus combo} = \text{Dégats Base} \times \frac{\text{100 + stats roub + puissance roub \textit{(+ puissance bombe)}}}{100}+\text{dommages roub \textit{(+ dommages bombe)}} \text{ (arrondi à l'entier inférieur})
''')
st.latex(r'''
\text{Dégats finaux} = \text{Dégats avant bonus combo}\times (1-\frac{\text{distance}}{10}) \times (\frac{\text{bonus combo en \%} + 100}{100}) \times \text{\% dommages occasionnés roublard/bombe} \text{ (arrondi à l'entier inférieur})
''')
st.subheader("Données par type de bombe :")

tab_explo="""
| Lvl bombe | Vita Base | Vita Coef | dégats mur min | dégats mur max | dégats explosion min | dégats explosion max |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 4 | 19 | 27% | 15 | 17 | 14 | 15 |
| 5 | 23 | 27% | 16 | 18 | 15 | 16 |
| 6 | 28 | 27% | 19 | 21 | 20 | 22 |
"""
tab_torna="""
| Lvl bombe | Vita Base | Vita Coef | dégats mur min | dégats mur max | dégats explosion min | dégats explosion max |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 4 | 19 | 27% | 11 | 13 | 11 | 12 |
| 5 | 23 | 27% | 12 | 14 | 12 | 13 |
| 6 | 28 | 27% | 15 | 17 | 17 | 19 |
"""
tab_bombeau="""
| Lvl bombe | Vita Base | Vita Coef | dégats mur min | dégats mur max | dégats explosion min | dégats explosion max |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 4 | 19 | 35% | 11 | 13 | 11 | 12 |
| 5 | 23 | 35% | 12 | 14 | 12 | 13 |
| 6 | 28 | 35% | 12 | 14 | 14 | 16 |
"""
st.markdown("- **ExploBombe :**")
st.markdown(tab_explo)
st.markdown("- **TornaBombe :**")
st.markdown(tab_torna)
st.markdown("- **Bombe à eau :**")
st.markdown(tab_bombeau)



st.divider()
st.caption("L'objectif de cette page est de rassembler les différentes formules de calcul et données utiles à connaître dans le jeu, tant pour le quotidien que le théorycraft.")
toc.generate()


table_style = """
<style>
    table {
        width: 100%;  /* Le tableau prend toute la largeur disponible */
        border-collapse: collapse; /* Supprime les espaces entre les bordures */
    }
    th, td {
        border: 1px solid white;  /* Bordures blanches autour des cellules */
        padding: 8px;  /* Ajoute un espace de 8px à l'intérieur des cellules */
        text-align: center; /* Centre le texte dans les cellules */
    }
    th {
        background-color: #333B00; /* Couleur d'arrière-plan des en-têtes */
        color: #FAFAFA; /* Couleur du texte des en-têtes */
    }
    td {
        background-color: #262730; /* Fond sombre des cellules */
        color: #FAFAFA; /* Texte blanc */
    }
</style>
"""
st.markdown(table_style, unsafe_allow_html=True)