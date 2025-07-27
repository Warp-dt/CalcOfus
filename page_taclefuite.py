import streamlit as st
import dofusbook_scraping_requests as db
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="CalcoTac",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

st.write("## Calculateur de Tacle/Fuite")


######################
#SIDEBAR
######################

st.sidebar.image(image_path+"calcoTac_logo_nom_transp.png" )


######################
#Calculateur
######################
with st.container(border=True):    
    st.write('### Fuyard')
    fuitecol, pmcol, pacol = st.columns((1,1,1))
    fuite=fuitecol.number_input(label="Fuite",min_value=0,max_value=None,value=50)
    pm=pmcol.number_input(label="PM",min_value=0,max_value=None,value=6)
    pa=pacol.number_input(label="PA",min_value=0,max_value=None,value=12)


with st.container(border=True):    
    st.write('### Tacleur(s)')
    nb_tac=st.number_input(label="Nombre de Tacleurs",min_value=1,max_value=3,value=1)

    tacs = st.columns((1,1,1))
    tacles=[0,0,0]
    for t in range(nb_tac):
        tacles[t]=tacs[t].number_input(label=f"Tacleur {t+1}",min_value=0,max_value=None,value=50,key=100+t)
    # st.write(tacles)
    

p1=min(max((fuite+2)/(2*(tacles[0]+2)),0),1)
p2=min(max((fuite+2)/(2*(tacles[1]+2)),0),1)
p3=min(max((fuite+2)/(2*(tacles[2]+2)),0),1)
ptot=p1*p2*p3
couleur_table="#4a3a23"
alerte_full_tacle=''
if int(pm-(pm*ptot)//1)==pm:
    couleur_table="#630000"
    alerte_full_tacle=' **FULL TACLE !**'
elif int(pm-(pm*ptot)//1)==0:
    couleur_table="#333B00"
    alerte_full_tacle=' **FULL DÉTACLE !**'

tab_res="""
| PM perdus | PA perdus |
| ----------- | ----------- |
"""
tab_res+=f"""| {int(pm-(pm*ptot)//1)}{alerte_full_tacle} | {int(pa-(pa*ptot)//1)} |"""

st.write(tab_res)

st.write(""" Valeurs à retenir :
- Pour détacler 100% un tacleur il faut (Tacle x 2) + 2 en fuite minimum
- Le Pandawasta a 52 de tacle : il faut 106 de fuite pour détacler 100%
- La bloqueuse a 50 de tacle : il faut 102 de fuite pour détacler 100%

""")
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