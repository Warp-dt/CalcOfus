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


st.title("LES FORMULES DE DOFUS TOUCH")
st.header("1. Lignes de sorts",divider="gray")
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
st.header("2. Sorts de réductions de dégats",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_8")
st.markdown("""
Sorts comme rempart ou armure de sel qui appliquent une réduction fixe.\n
Cette réduction s'applique après les résistances fixes et % mais avant les %dommages finaux.
""")
st.subheader("Formules :")
st.latex(r'''
\text{Réduction} = \text{Base} \times \frac{100 + 5 \times \text{Lvl lançeur}}{100}
''')
st.subheader("Exemple :")
st.latex(r'''
\text{Rempart Lvl 6 Joueur Lvl 200} : \text{Réduction} = 13 \times \frac{100 + 5 \times 200}{100} = 143
''')
st.header("3. Résistances/Réductions de dégats",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_9")
st.header("4. Dégats et résistances de poussée",divider="gray")
st.header("5. Retrait/Esquive",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_7")
st.header("6. Tacle/Fuite",divider="gray")
source("JoL","https://forums.jeuxonline.info/sujet/801243/les-formules-de-calcul-dans-dofus#titre_14")
st.header("7. Invocations Osamodas",divider="gray")
source("Warp")
st.header("8. Bombes",divider="gray")
source("Emrys")

st.divider()
st.caption("L'objectif de cette page est de rassembler les différentes formules de calcul et données utiles à connaître dans le jeu, tant pour le quotidien que le théorycraft.")