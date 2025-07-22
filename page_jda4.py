import streamlit as st
import pandas as pd

image_path='images/'
st.set_page_config(page_title="CalcOfus",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

st.sidebar.image(image_path+"logo_jda4.png" )


st.title("Compositions Finales JDA#4")

df=[{'C1': 'cra', 'C3': 'ecaflip', 'C2': 'xelor'},
 {'C1': 'ecaflip', 'C3': 'feca', 'C2': 'steamer'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'xelor'},
 {'C1': 'ecaflip', 'C3': 'roublard', 'C2': 'xelor'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'feca'},
 {'C1': 'ecaflip', 'C3': 'feca', 'C2': 'pandawa'},
 {'C1': 'cra', 'C3': 'eniripsa', 'C2': 'enutrof'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'feca'},
 {'C1': 'ecaflip', 'C3': 'sadida', 'C2': 'steamer'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'steamer'},
 {'C1': 'ecaflip', 'C3': 'pandawa', 'C2': 'steamer'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'sadida'},
 {'C1': 'ecaflip', 'C3': 'sacrieur', 'C2': 'sadida'},
 {'C1': 'ecaflip', 'C3': 'sadida', 'C2': 'zobal'},
 {'C1': 'ecaflip', 'C3': 'pandawa', 'C2': 'sadida'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'sacrieur'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'zobal'},
 {'C1': 'ecaflip', 'C3': 'pandawa', 'C2': 'sacrieur'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'osamodas'},
 {'C1': 'cra', 'C3': 'osamodas', 'C2': 'pandawa'},
 {'C1': 'enutrof', 'C3': 'feca', 'C2': 'steamer'},
 {'C1': 'feca', 'C3': 'pandawa', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'sadida'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'enutrof'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'sacrieur'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'pandawa'},
 {'C1': 'cra', 'C3': 'feca', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'xelor'},
 {'C1': 'cra', 'C3': 'roublard', 'C2': 'xelor'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'feca'},
 {'C1': 'cra', 'C3': 'feca', 'C2': 'pandawa'},
 {'C1': 'enutrof', 'C3': 'sadida', 'C2': 'steamer'},
 {'C1': 'pandawa', 'C3': 'sadida', 'C2': 'steamer'},
 {'C1': 'enutrof', 'C3': 'sacrieur', 'C2': 'sadida'},
 {'C1': 'enutrof', 'C3': 'sadida', 'C2': 'zobal'},
 {'C1': 'pandawa', 'C3': 'sacrieur', 'C2': 'sadida'},
 {'C1': 'eniripsa', 'C3': 'enutrof', 'C2': 'iop'},
 {'C1': 'eniripsa', 'C3': 'enutrof', 'C2': 'roublard'},
 {'C1': 'ecaflip', 'C3': 'sram', 'C2': 'xelor'},
 {'C1': 'ecaflip', 'C3': 'feca', 'C2': 'iop'},
 {'C1': 'ecaflip', 'C3': 'feca', 'C2': 'roublard'},
 {'C1': 'cra', 'C3': 'sadida', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'pandawa', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'sadida'},
 {'C1': 'cra', 'C3': 'sacrieur', 'C2': 'sadida'},
 {'C1': 'cra', 'C3': 'sadida', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'pandawa', 'C2': 'sadida'},
 {'C1': 'cra', 'C3': 'eniripsa', 'C2': 'iop'},
 {'C1': 'cra', 'C3': 'eniripsa', 'C2': 'roublard'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'sacrieur'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'pandawa', 'C2': 'sacrieur'},
 {'C1': 'enutrof', 'C3': 'iop', 'C2': 'osamodas'},
 {'C1': 'enutrof', 'C3': 'osamodas', 'C2': 'roublard'},
 {'C1': 'iop', 'C3': 'osamodas', 'C2': 'pandawa'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'steamer'},
 {'C1': 'ecaflip', 'C3': 'roublard', 'C2': 'steamer'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'sadida'},
 {'C1': 'ecaflip', 'C3': 'roublard', 'C2': 'sadida'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'iop'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'roublard'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'sacrieur'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'zobal'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'pandawa'},
 {'C1': 'ecaflip', 'C3': 'roublard', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'osamodas'},
 {'C1': 'cra', 'C3': 'osamodas', 'C2': 'roublard'},
 {'C1': 'feca', 'C3': 'iop', 'C2': 'steamer'},
 {'C1': 'feca', 'C3': 'roublard', 'C2': 'steamer'},
 {'C1': 'iop', 'C3': 'roublard', 'C2': 'xelor'},
 {'C1': 'enutrof', 'C3': 'feca', 'C2': 'iop'},
 {'C1': 'enutrof', 'C3': 'feca', 'C2': 'roublard'},
 {'C1': 'feca', 'C3': 'iop', 'C2': 'pandawa'},
 {'C1': 'cra', 'C3': 'sram', 'C2': 'xelor'},
 {'C1': 'eniripsa', 'C3': 'enutrof', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'iop'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'roublard'},
 {'C1': 'cra', 'C3': 'feca', 'C2': 'iop'},
 {'C1': 'cra', 'C3': 'feca', 'C2': 'roublard'},
 {'C1': 'iop', 'C3': 'sadida', 'C2': 'steamer'},
 {'C1': 'roublard', 'C3': 'sadida', 'C2': 'steamer'},
 {'C1': 'enutrof', 'C3': 'iop', 'C2': 'steamer'},
 {'C1': 'enutrof', 'C3': 'roublard', 'C2': 'steamer'},
 {'C1': 'iop', 'C3': 'pandawa', 'C2': 'steamer'},
 {'C1': 'enutrof', 'C3': 'iop', 'C2': 'sadida'},
 {'C1': 'enutrof', 'C3': 'roublard', 'C2': 'sadida'},
 {'C1': 'iop', 'C3': 'sacrieur', 'C2': 'sadida'},
 {'C1': 'iop', 'C3': 'sadida', 'C2': 'zobal'},
 {'C1': 'iop', 'C3': 'pandawa', 'C2': 'sadida'},
 {'C1': 'roublard', 'C3': 'sadida', 'C2': 'zobal'},
 {'C1': 'eniripsa', 'C3': 'iop', 'C2': 'roublard'},
 {'C1': 'enutrof', 'C3': 'iop', 'C2': 'sacrieur'},
 {'C1': 'enutrof', 'C3': 'iop', 'C2': 'zobal'},
 {'C1': 'enutrof', 'C3': 'roublard', 'C2': 'zobal'},
 {'C1': 'iop', 'C3': 'pandawa', 'C2': 'sacrieur'},
 {'C1': 'ecaflip', 'C3': 'feca', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'eniripsa', 'C2': 'sram'},
 {'C1': 'enutrof', 'C3': 'osamodas', 'C2': 'sram'},
 {'C1': 'osamodas', 'C3': 'pandawa', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'roublard', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'sadida'},
 {'C1': 'cra', 'C3': 'roublard', 'C2': 'sadida'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'iop'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'roublard'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'sacrieur'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'pandawa'},
 {'C1': 'cra', 'C3': 'roublard', 'C2': 'zobal'},
 {'C1': 'iop', 'C3': 'osamodas', 'C2': 'roublard'},
 {'C1': 'ecaflip', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'ecaflip', 'C3': 'sadida', 'C2': 'sram'},
 {'C1': 'ecaflip', 'C3': 'enutrof', 'C2': 'sram'},
 {'C1': 'ecaflip', 'C3': 'sacrieur', 'C2': 'sram'},
 {'C1': 'ecaflip', 'C3': 'sram', 'C2': 'zobal'},
 {'C1': 'ecaflip', 'C3': 'pandawa', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'osamodas', 'C2': 'sram'},
 {'C1': 'feca', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'iop', 'C3': 'sram', 'C2': 'xelor'},
 {'C1': 'roublard', 'C3': 'sram', 'C2': 'xelor'},
 {'C1': 'enutrof', 'C3': 'feca', 'C2': 'sram'},
 {'C1': 'feca', 'C3': 'pandawa', 'C2': 'sram'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'roublard'},
 {'C1': 'feca', 'C3': 'iop', 'C2': 'roublard'},
 {'C1': 'cra', 'C3': 'ecaflip', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'feca', 'C2': 'sram'},
 {'C1': 'sadida', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'enutrof', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'pandawa', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'enutrof', 'C3': 'sadida', 'C2': 'sram'},
 {'C1': 'sacrieur', 'C3': 'sadida', 'C2': 'sram'},
 {'C1': 'sadida', 'C3': 'sram', 'C2': 'zobal'},
 {'C1': 'pandawa', 'C3': 'sadida', 'C2': 'sram'},
 {'C1': 'eniripsa', 'C3': 'iop', 'C2': 'sram'},
 {'C1': 'eniripsa', 'C3': 'roublard', 'C2': 'sram'},
 {'C1': 'enutrof', 'C3': 'sacrieur', 'C2': 'sram'},
 {'C1': 'enutrof', 'C3': 'sram', 'C2': 'zobal'},
 {'C1': 'pandawa', 'C3': 'sacrieur', 'C2': 'sram'},
 {'C1': 'iop', 'C3': 'roublard', 'C2': 'steamer'},
 {'C1': 'iop', 'C3': 'roublard', 'C2': 'sadida'},
 {'C1': 'enutrof', 'C3': 'iop', 'C2': 'roublard'},
 {'C1': 'iop', 'C3': 'roublard', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'cra', 'C3': 'sadida', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'enutrof', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'sacrieur', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'sram', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'pandawa', 'C2': 'sram'},
 {'C1': 'iop', 'C3': 'osamodas', 'C2': 'sram'},
 {'C1': 'osamodas', 'C3': 'roublard', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'roublard'},
 {'C1': 'ecaflip', 'C3': 'iop', 'C2': 'sram'},
 {'C1': 'ecaflip', 'C3': 'roublard', 'C2': 'sram'},
 {'C1': 'feca', 'C3': 'iop', 'C2': 'sram'},
 {'C1': 'feca', 'C3': 'roublard', 'C2': 'sram'},
 {'C1': 'iop', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'roublard', 'C3': 'sram', 'C2': 'steamer'},
 {'C1': 'iop', 'C3': 'sadida', 'C2': 'sram'},
 {'C1': 'roublard', 'C3': 'sadida', 'C2': 'sram'},
 {'C1': 'enutrof', 'C3': 'iop', 'C2': 'sram'},
 {'C1': 'enutrof', 'C3': 'roublard', 'C2': 'sram'},
 {'C1': 'iop', 'C3': 'sacrieur', 'C2': 'sram'},
 {'C1': 'iop', 'C3': 'sram', 'C2': 'zobal'},
 {'C1': 'iop', 'C3': 'pandawa', 'C2': 'sram'},
 {'C1': 'roublard', 'C3': 'sram', 'C2': 'zobal'},
 {'C1': 'cra', 'C3': 'iop', 'C2': 'sram'},
 {'C1': 'cra', 'C3': 'roublard', 'C2': 'sram'},
 {'C1': 'iop', 'C3': 'roublard', 'C2': 'sram'}]

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


list_stats_images=[image_path+"JDA4_Compo les plus jouées.png",
                  image_path+"JDA4_Nombre de pick des classes.png",
                  image_path+"JDA4_Duos les plus joués.png",
                  image_path+"JDA4_heat_duos les plus joués.png"]
list_captions=["JDA#4 - Compositions les plus jouées",
               "JDA#4 - Nombre de pick des classes",
               "JDA#4 - Duos les plus joués",
               "JDA#4 - Heatmap des duos les plus joués"]
st.image(list_stats_images, caption=list_captions, use_container_width=True)

st.write("## Liste des 154 équipes inscrites")
compos=pd.read_csv("data/compositions_JDA#4.csv",sep=";")
st.dataframe(compos,hide_index=True,on_select='ignore')



st.title("Compositions Possibles JDA#4")

# classes_voulues=st.text_input("Classes voulues (séparées par des virgules)", value="",placeholder="ex: osamodas,enutrof",autocomplete="sram,ecaflip")
classes_voulues=st.multiselect("Classes voulues",options=CLASSES, default=[],placeholder="Sélectionnez les classes voulues",max_selections=3)
classes_interdites=st.multiselect("Classes interdites",options=CLASSES, default=[],placeholder="Sélectionnez les classes dont vous ne voulez pas")
points={'cra': 0,
        'ecaflip': 0,
        'eniripsa': 0,
        'enutrof': 0,
        'feca': 0,
        'iop': 0,
        'osamodas': 0,
        'pandawa': 0,
        'roublard': 0,
        'sacrieur': 0,
        'sadida': 0,
        'sram': 0,
        'steamer': 0,
        'xelor': 0,
        'zobal': 0}
points_default={'cra': 4,
        'ecaflip': 6,
        'eniripsa': 9,
        'enutrof': 6,
        'feca': 7,
        'iop': 3,
        'osamodas': 8,
        'pandawa': 5,
        'roublard': 3,
        'sacrieur': 6,
        'sadida': 6,
        'sram': 0,
        'steamer': 5,
        'xelor': 10,
        'zobal': 7}



with st.sidebar:
    st.write("""# Points par classe\n 
Ces points servent à trier les 171 compositions possibles.\n
J'ai mis des valeurs par défaut, mais vous pouvez les modifier si vous le souhaitez.
""")
    for classe in points:
        points[classe] = st.number_input(f"Points {classe.capitalize()}", value=points_default[classe], step=1, key=f"points_{classe}")
    # sram_pts = st.number_input("Points Sram", value=4, step=1)

def filtrer_compositions(classes_voulues, classes_interdites):
    # st.write("Filtrage des compositions...")
    # st.write(classes_voulues, classes_interdites)
    st.session_state["temp_df"] =   [comp for comp in df if
                                    not any([c in comp.values() for c in classes_interdites]) 
                                    and
                                    all([c in comp.values() for c in classes_voulues])]
    # st.write(st.session_state["temp_df"])

# filtrer_compositions(["cra","ecaflip"], ["xelor"])
st.button("Filtrer les compositions", key="filter_compositions",on_click=filtrer_compositions, args=(classes_voulues, classes_interdites))
try:
    compositions = pd.DataFrame(st.session_state["temp_df"])

except:
    compositions = pd.DataFrame(df)

try:
    compositions["Points"]= compositions.apply(lambda row: points[row['C1']] + points[row['C2']] + points[row['C3']], axis=1)
except:
    pass

st.write("### Nombre de compositions trouvées :", str(len(compositions)))
st.dataframe(compositions,hide_index=True)

st.image(image_path+"restrictions_JDA#4.png" )