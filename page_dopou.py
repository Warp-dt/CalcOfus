import streamlit as st
image_path='images/'



######################
# Page Title
######################

st.set_page_config(page_title="CalcOpou",layout="wide")

######################
#SIDEBAR
######################

with st.sidebar:
    st.image(image_path+"calcopou_logo_nom_transp.png" )
    # st.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio DofusBook**',icon="📚")

##############
# DOPOU
##############

st.write("## Calculateur de dégats de poussée")

lvl = st.number_input("Lvl",value=200,key=101)
dopou = st.number_input("DoPou",value=0,key=102)
repou = st.number_input("RePou",value=0,key=103)
nb_cases = st.number_input("Cases de poussée",value=4,key=104)
dégats_pou= (lvl/2+dopou-repou+32)/4*nb_cases

tab_dopou="""
| Dégats de la poussée|
| ----------- |
"""
tab_dopou+="| "+str(int(dégats_pou))+'\n'
st.write(tab_dopou)


table_style = """
<style>
    table {
        width: 100%;  /* Le tableau prend toute la largeur disponible */
        border-collapse: collapse; /* Supprime les espaces entre les bordures */
        text-align: center; /* Centre le texte dans toutes les cellules */

    }
    th, td {
        border: 1px solid white;  /* Bordures blanches autour des cellules */
        padding: 8px;  /* Ajoute un espace de 8px à l'intérieur des cellules */
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