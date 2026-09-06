import streamlit as st
import dofusbook_scraping_requests as db
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="CalcoTac",layout="wide")

st.sidebar.image(image_path+"calcoret_logo_nom_transp.png" )

st.write("## Calculateur de Retrait/Esquive")
st.caption("Logique et formules détaillées [ici](http://localhost:8501/formulofus#6-retrait-esquive)")

######################
#Calculateur
######################
with st.container(border=True):    
    
    st.write('### Retireur')
    st.caption("Personnage qui essaie de retirer des PA/PM.")
    # colretPA,colretPM = st.columns((1,1))
    # retPA=colretPA.number_input(label="Retrait PA",min_value=0,max_value=None,value=100)
    ret=st.number_input(label="Retrait PA/PM",min_value=0,max_value=None,value=100)
    nb_ret=st.number_input(label="Nombre de retrait PA/PM tentés",min_value=1,max_value=None,value=2,help="Par exemple le ralentissement retire 2 PA, chaque PA/Pm est retiré l'un après l'autre donc retirer avec 1 sort 2PA ou 2 sorts 1PA c'est pareil.")


with st.container(border=True):    
    st.write('### Esquiveur')
    st.caption("Personnage qui subit le retrait.")
    esq=st.number_input(label="Esquive PA/PM",min_value=0,max_value=None,value=50)
    papmcible=st.number_input(label="Nombre de PA/PM max",help="Avant tout retrait, mais boost compris.",min_value=0,max_value=None,value=12) 

probabilites = {0: 1.0}

for _ in range(nb_ret):
    nouvelles = {}

    for nb_retires, proba_etat in probabilites.items():
        pa_restants = papmcible - nb_retires

        if pa_restants <= 0:
            # Plus rien à retirer
            nouvelles[nb_retires] = nouvelles.get(nb_retires, 0) + proba_etat
            continue

        p_retrait = (
            pa_restants / papmcible
            * ret / esq
            * 0.5
        )

        p_retrait = min(1.0, max(0.0, p_retrait))

        # Succès : on retire 1 PA
        nouvelles[nb_retires + 1] = (
            nouvelles.get(nb_retires + 1, 0)
            + proba_etat * p_retrait
        )

        # Échec : aucun PA retiré
        nouvelles[nb_retires] = (
            nouvelles.get(nb_retires, 0)
            + proba_etat * (1 - p_retrait)
        )

    probabilites = nouvelles

esperance=0
for i in probabilites:
    esperance+=i*probabilites[i]

st.subheader("Résultat")
# st.write('---')

col1, col2 = st.columns(2)

st.markdown(
    f"""
    <div style="
        background-color: #161a22;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 10px;
    ">
        <div style="
            color: #9da3ae;
            font-size: 0.85rem;
            margin-bottom: 4px;
        ">
            PA/PM moyens retirés
        </div>
        <div style="
            color: #E6E9EF;
            font-size: 2rem;
            font-weight: 600;
        ">
            {esperance:.2f}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


coltab,colgraph=st.columns((1,2))

#TABLEAU
tab_res="""
| PA/PM retirés | Probabilité |
| ----------- | ----------- |
"""
for i in reversed(probabilites):
    tab_res+=f"""| {i} | {round(probabilites[i]*100,2)} % |\n"""

coltab.write(tab_res)

#=========================
# BAR CHART HTML/CSS
# =========================
bars_html = ""

# TITRES
bars_html += """
<div style="
    display: grid;
    grid-template-columns: 35px 1fr;
    gap: 10px;
    margin-bottom: 6px;
">
    <div style="
        color: #9da3ae;
        font-size: 0.8rem;
        text-align: right;
    ">
        PA/PM
    </div>

    <div style="
        color: #9da3ae;
        font-size: 0.8rem;
    ">
        Probabilité %
    </div>
</div>
"""

# BARRES
for i in reversed(probabilites):
    proba = probabilites[i] * 100

    bars_html += f"""
    <div style="
        display: grid;
        grid-template-columns: 35px 1fr;
        align-items: center;
        gap: 10px;
        height: 38.61px;
    ">

        <div style="
            color: #E6E9EF;
            font-size: 0.9rem;
            text-align: right;
        ">
            {i}
        </div>

        <div style="
            position: relative;
            height: 22px;
            background: rgba(255,255,255,0.04);
            border-radius: 5px;
        ">

            <div style="
                position: absolute;
                left: 0;
                top: 0;
                height: 100%;
                width: {proba}%;
                background: #333B00;
                border-radius: 5px;
            "></div>

            <span style="
                position: absolute;
                left: calc({proba}% + 8px);
                top: 50%;
                transform: translateY(-50%);
                color: #E6E9EF;
                font-size: 0.85rem;
                white-space: nowrap;
            ">
                {proba:.2f} %
            </span>

        </div>
    </div>
    """

colgraph.html(
    f"""
    <div style="
        width: 100%;
        padding: 13px 0;
    ">
        {bars_html}
    </div>
    """
)

couleur_table="#333B00"
table_style = f"""
<style>
    table {{
        width: 100%;  /* Le tableau prend toute la largeur disponible */
        border-collapse: collapse; /* Supprime les espaces entre les bordures */
        text-align: center; /* Centre le texte dans toutes les cellules */

    }}
    th, td {{
        border: 1px solid white;  /* Bordures blanches autour des cellules */
        padding: 8px;  /* Ajoute un espace de 8px à l'intérieur des cellules */
    }}
    th {{
        background-color: {couleur_table}; /* Couleur d'arrière-plan des en-têtes */
        color: #FAFAFA; /* Couleur du texte des en-têtes */
        
    }}
    td {{
        background-color: #262730; /* Fond sombre des cellules */
        color: #FAFAFA; /* Texte blanc */
    }}
</style>
"""

st.markdown(table_style, unsafe_allow_html=True)

