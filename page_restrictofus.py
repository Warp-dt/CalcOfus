import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io
import itertools
import json


image_path='images/'
graphs_path=image_path+'graphs_jda4/'
st.set_page_config(page_title="RestrictOfus",layout="wide")
st.sidebar.image(image_path+"logo_restrictofus.png" )

st.html('<div style="text-align: center; font-size: 50px;font-weight: bold"> Constructeur de Restrictions </div>')


CLASSES=['cra',
'ecaflip',
'eniripsa',
'enutrof',
'feca',
'iop',
'osamodas',
'pandawa',
'roublard',
'sacrieur',
'sadida',
'sram',
'steamer',
'xelor',
'zobal']





def force_symetrie(df: pd.DataFrame):
    for i in CLASSES:
        for j in CLASSES:
            if df.loc[i, j]!=st.session_state.restriction_table.loc[i,j]:
                df.loc[j,i]=df.loc[i, j]
            if i==j:
                df.loc[i, j]=True
    
    st.session_state.restriction_table =df.copy()

    #applique les restri à la liste de compo
    st.session_state.compolist_builder=restri_to_compolist(st.session_state.restriction_table.values.tolist())


# Charger l'image de fond
base = Image.open(image_path+"restri_base.jpg").convert("RGBA")  # assure un mode RGBA

# Charger l'image à superposer
overlay = Image.open(image_path+"interdit.png").convert("RGBA")  # assure un canal alpha
size=37
overlay_resized = overlay.resize((size, size))

@st.cache_data()
def restri_img_from_df(df):
    # Redimensionner l'image
    img=base.copy()

    x_step=107.6
    y_step=56.8
    for i in range(len(CLASSES)):
        for j in range(len(CLASSES)):
            if i!=j and df.loc[CLASSES[i],CLASSES[j]]:
                temp_pos=(355-size//2+int((i*x_step)//1)
                        ,256-size//2+int((j*y_step//1)))
                img.paste(overlay_resized, temp_pos, overlay_resized)  # fonctionne car RGBA

    # Afficher dans Streamlit
    return (img)

@st.cache_data
def image_to_png_buffer(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def reset_restri():
    data = np.zeros((len(CLASSES), len(CLASSES)), dtype=bool)
    np.fill_diagonal(data, True)
    st.session_state.restriction_table = pd.DataFrame(data, index=CLASSES, columns=CLASSES)

all_compo = list(itertools.combinations(CLASSES, 3))

id_cl={
    "cra" : 0
    ,"ecaflip" : 1
    ,"eniripsa" : 2
    ,"enutrof" : 3
    ,"feca" : 4
    ,"iop" : 5
    ,"osamodas" : 6
    ,"pandawa" : 7
    ,"roublard" : 8
    ,"sacrieur" : 9
    ,"sadida" : 10
    ,"sram" : 11
    ,"steamer" : 12
    ,"xelor" : 13
    ,"zobal" : 14
}

@st.cache_data
def restri_to_nbcombo(restri_mat):
    nb_compo=0
    for c in all_compo:
        flag=True

        for i in range(3):
            if restri_mat[id_cl[c[i]]][id_cl[c[(i+1)%3]]]==1 or restri_mat[id_cl[c[i]]][id_cl[c[(i+2)%3]]]==1:
                flag=False

        nb_compo+=flag
    return nb_compo

@st.cache_data
def restri_to_compolist(restri_mat):
    compo_list=[]
    for c in all_compo:
        flag=True

        for i in range(3):
            if restri_mat[id_cl[c[i]]][id_cl[c[(i+1)%3]]]==1 or restri_mat[id_cl[c[i]]][id_cl[c[(i+2)%3]]]==1:
                flag=False

        if flag:compo_list.append(c)
        
    return compo_list
# --- Initialisation ---
if "restriction_table" not in st.session_state:
    data = np.zeros((len(CLASSES), len(CLASSES)), dtype=bool)
    np.fill_diagonal(data, True)
    st.session_state.restriction_table = pd.DataFrame(data, index=CLASSES, columns=CLASSES)

# Initialisation du flag dans le session_state
if "csv_uploaded" not in st.session_state:
    st.session_state.csv_uploaded = False

# --- Créer une version avec diagonale non éditable ---
editable_df = st.session_state.restriction_table.copy()    

size=20
column_config={c : st.column_config.CheckboxColumn(label = None,width = size,) for c in CLASSES}

edited_df = st.data_editor(editable_df,column_config=column_config,row_height=size)

tab_update,tab_reset=st.columns((1,1))
tab_update.button("Applique symétrie & Update image",on_click=force_symetrie,args=(edited_df,),width="stretch")
tab_reset.button("Reset Tableau",on_click=reset_restri,width="stretch")
img=restri_img_from_df(st.session_state.restriction_table)
st.image(img)

# Sauvegarder dans un buffer mémoire au format PNG
buffer=image_to_png_buffer(img)

tab_dll_img,tab_dll_mat= st.columns((1,1))

# Bouton de téléchargement
tab_dll_img.download_button(
    label="Télécharger l'image",
    data=buffer,
    mime="image/png",
    file_name="restrictions.png",
    width="stretch"
)    

# ---------------------------
# 1. Télécharger le CSV
# ---------------------------
@st.cache_data
def dataframe_to_csv_bytes(dataframe: pd.DataFrame) -> bytes:
    """Convertit un DataFrame en CSV et renvoie des bytes pour le téléchargement."""
    csv_str = dataframe.to_csv(index=True)  # CSV sous forme de string
    return csv_str.encode('utf-8')  # Conversion en bytes UTF-8
csv_bytes = dataframe_to_csv_bytes(st.session_state.restriction_table)
tab_dll_mat.download_button(
    label="Télécharger les restrictions (CSV)",
    data=csv_bytes,
    mime="text/csv",
    file_name="restrictions.csv",
    width="stretch"
)

# ---------------------------
# 2. Upload d'un CSV
# ---------------------------

uploaded_file = st.file_uploader("Upload un CSV", type=["csv"])

# Étape 1 : Premier upload d'un fichier CSV
if uploaded_file is not None and not st.session_state.csv_uploaded:
    try:
        uploaded_df = pd.read_csv(uploaded_file, index_col=0)

        # Vérification : structure correcte
        if list(uploaded_df.columns) == CLASSES and list(uploaded_df.index) == CLASSES:
            # Remplacer la table dans session_state
            st.session_state.restriction_table = uploaded_df.astype(bool)

            # Marquer comme traité pour éviter boucle infinie
            st.session_state.csv_uploaded = True
            
            st.success("CSV importé avec succès et table mise à jour ✅")

            #applique les restri à la liste de compo
            st.session_state.compolist_builder=restri_to_compolist(st.session_state.restriction_table.values.tolist())

            # Forcer le rerun propre
            st.rerun()
        else:
            st.error("Le CSV n'a pas la bonne structure ou les bonnes classes ❌")

    except Exception as e:
        st.error(f"Erreur lors de l'import du CSV : {e}")

# Étape 2 : Si le fichier est toujours là après le rerun
elif uploaded_file is not None and st.session_state.csv_uploaded:
    st.info("Le fichier CSV est importé. Supprimez-le pour en charger un autre.")

# Étape 3 : Si le fichier est retiré
elif uploaded_file is None and st.session_state.csv_uploaded:
    st.session_state.csv_uploaded = False
    

@st.cache_data
def builder_compo_filtre(classes_voulues, classes_interdites,session_state_list,compo_list):
    st.session_state[session_state_list] =   [comp for comp in compo_list if
                                not any([c in comp for c in classes_interdites]) 
                                and
                                all([c in comp for c in classes_voulues])]
with st.expander("Détails sur ces restrictions :",expanded=True):
    # st.write(st.session_state.restriction_table.values.tolist())
    restri_mat=st.session_state.restriction_table.values.tolist()

    if "points_builder" not in st.session_state:
        st.session_state.points_builder={
        'cra':      0,
        'ecaflip':  0,
        'eniripsa': 0,
        'enutrof':  0,
        'feca':     0,
        'iop':      0,
        'osamodas': 0,
        'pandawa':  0,
        'roublard': 0,
        'sacrieur': 0,
        'sadida':   0,
        'sram':     0,
        'steamer':  0,
        'xelor':    0,
        'zobal':    0}
    if "temp_points_builder" not in st.session_state:
        st.session_state.temp_points_builder={
        'cra':      0,
        'ecaflip':  0,
        'eniripsa': 0,
        'enutrof':  0,
        'feca':     0,
        'iop':      0,
        'osamodas': 0,
        'pandawa':  0,
        'roublard': 0,
        'sacrieur': 0,
        'sadida':   0,
        'sram':     0,
        'steamer':  0,
        'xelor':    0,
        'zobal':    0}
    
    compolist_builder=restri_to_compolist(restri_mat)
    if "compolist_builder" not in st.session_state:
        st.session_state.compolist_builder=compolist_builder
    nbcompo_builder=len(st.session_state.compolist_builder)
    st.write(f"### Nombre de compo possibles : {nbcompo_builder}")

    classes_voulues_builder=st.multiselect("Classes voulues",options=CLASSES, default=[],placeholder="Sélectionnez les classes voulues",max_selections=3,key=524)
    classes_interdites_builder=st.multiselect("Classes interdites",options=CLASSES, default=[],placeholder="Sélectionnez les classes dont vous ne voulez pas",key=525)

    st.button("Filtrer les compositions",
                key="filter_compositions_builder",
                on_click=builder_compo_filtre,
                args=(classes_voulues_builder, 
                    classes_interdites_builder,
                    "compolist_builder",
                    compolist_builder),
                width="stretch")

    if nbcompo_builder>0:
        compossibles=pd.DataFrame(st.session_state.compolist_builder,columns=["C1","C2","C3"])
        compossibles["Points"]= compossibles.apply(lambda row: st.session_state.points_builder[row['C1']] + st.session_state.points_builder[row['C2']] + st.session_state.points_builder[row['C3']], axis=1)
        st.dataframe(compossibles,hide_index=True)

    # Fonction utilitaire : DataFrame -> Excel buffer
    @st.cache_data
    def dataframe_to_excel_bytes(df: pd.DataFrame) -> bytes:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        buffer.seek(0)
        return buffer

    if nbcompo_builder > 0:
        # --- Bouton téléchargement Excel des compositions possibles ---
        excel_buffer = dataframe_to_excel_bytes(compossibles)
        st.download_button(
            label="Télécharger les compositions (Excel)",
            data=excel_buffer,
            file_name="compositions_possibles.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            width="stretch"
        )

    def update_points_builder():
        st.session_state.points_builder=st.session_state.temp_points_builder
    
    st.button(label="Appliquer les points",on_click=update_points_builder,width="stretch")
    with st.expander("Points par classe"):
        st.write("""#### Points par classe\n 
Ces points servent à trier les compositions possibles.""")
        for classe in CLASSES:
            st.session_state.temp_points_builder[classe] = st.number_input(f"Points {classe.capitalize()}", value=0, step=1, key=f"points_builder_{classe}")
    
    # --- Bouton téléchargement JSON des points ---
    points_json = json.dumps(st.session_state.points_builder, indent=2)
    st.download_button(
        label="Télécharger les points (JSON)",
        data=points_json,
        file_name="points_par_classe.json",
        mime="application/json",
        width="stretch"
    )