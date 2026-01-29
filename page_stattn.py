import streamlit as st
import pandas as pd

image_path='images/'
graphs_path=image_path+'graphs_jda4/'
graphs_path_kmc1=image_path+'graphs_kmc1/'
graphs_path_kmc2=image_path+'graphs_kmc2/'
st.set_page_config(page_title="StatsTournois",layout="wide")

st.sidebar.image(image_path+"logo_stattn.png" )

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

SERVEURS=['Blair','Kelerog','Talok','Tiliwan','Touch tournament',]

tab_KMC2,tab_KMC1,tab_jda4=st.tabs(["KMC #2","KMC #1","JDA #4"])

@st.cache_data
def filtrer_compositions_jda4(classes_voulues, classes_interdites,session_state_df,df):
    st.session_state[session_state_df] =   [comp for comp in df if
                                    not any([c in comp.values() for c in classes_interdites]) 
                                    and
                                    all([c in comp.values() for c in classes_voulues])]

@st.cache_data
def filtrer_compositions(classes_voulues, classes_interdites,session_state_df,df):
    st.session_state[session_state_df] =   [comp for comp in df if
                                    not any([c in comp for c in classes_interdites]) 
                                    and
                                    all([c in comp for c in classes_voulues])]

def update_points(df,points,temp_points):
    st.session_state[points]=st.session_state[temp_points]
    df["Points"]= df.apply(lambda row: st.session_state[points][row["C1"]] + st.session_state[points][row["C2"]] + st.session_state[points][row["C3"]], axis=1)


with tab_KMC2:
    compo_kmc2=pd.read_excel("data/compositions_KMC#2.xlsx",usecols=["C1","C2","C3"]).values.tolist()
    
    st.html('<div style="text-align: center; font-size: 50px;font-weight: bold"> STATS KELEROG MASTER CUP #2 </div>')

    list_statsKMC2_images=[graphs_path_kmc2+"Compo les plus jouées.png",
                graphs_path_kmc2+"Nombre de pick des classes.png",
                graphs_path_kmc2+"Duos les plus joués.png",
                graphs_path_kmc2+"heat_Duos les plus joués.png"]
    st.image(list_statsKMC2_images, caption=None, use_container_width=True)

    with st.expander("Compositions d'équipe possibles :",expanded=False):
    # st.title("Compositions Possibles JDA#4")

        classes_voulues_kmc2=st.multiselect("Classes voulues",options=CLASSES, default=[],placeholder="Sélectionnez les classes voulues",max_selections=3,key="classes_voulues_kmc2")
        classes_interdites_kmc2=st.multiselect("Classes interdites",options=CLASSES, default=[],placeholder="Sélectionnez les classes dont vous ne voulez pas",key="classes_interdites_kmc2")

        st.button("Filtrer les compositions", key="filter_compositions_kmc2",on_click=filtrer_compositions, args=(classes_voulues_kmc2, classes_interdites_kmc2,"temp_compo_kmc2",compo_kmc2))
                
        points_kmc2_default={
            'cra':      6,
            'ecaflip':  6,
            'eniripsa': 11,
            'enutrof':  9,
            'feca':     10,
            'iop':      8,
            'osamodas': 9,
            'pandawa':  7,
            'roublard': 7,
            'sacrieur': 9,
            'sadida':   10,
            'sram':     5,
            'steamer':  8,
            'xelor':    11,
            'zobal':    10}
        
        
        if "points_kmc2" not in st.session_state:
            st.session_state.points_kmc2={
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
        if "temp_points_kmc2" not in st.session_state:
            st.session_state.temp_points_kmc2={
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
        
        try:
            compositions_kmc2 = pd.DataFrame(st.session_state["temp_compo_kmc2"],columns=["C1","C2","C3"])

        except:
            compositions_kmc2 = pd.DataFrame(compo_kmc2,columns=["C1","C2","C3"])

        try:
            compositions_kmc2["Points"]= compositions_kmc2.apply(lambda row: st.session_state.points_kmc2[row['C1']] + st.session_state.points_kmc2[row['C2']] + st.session_state.points_kmc2[row['C3']], axis=1)
        except:
            pass

        st.write("### Nombre de compositions trouvées :", str(len(compositions_kmc2)))
        st.dataframe(compositions_kmc2,hide_index=True)
        st.image(image_path+"restrictions_kmc2.png" )
        st.write(f"""#### Points par classe\n 
Ces points servent à trier les {len(compositions_kmc2)} compositions possibles.
""")            

        st.button(label="Appliquer les points",on_click=update_points,args=(compositions_kmc2,"points_kmc2","temp_points_kmc2"),width="stretch",key="update_points_kmc2")

        for classe in CLASSES:
            st.session_state.temp_points_kmc2[classe] = st.number_input(f"Points {classe.capitalize()}", value=points_kmc2_default[classe], step=1, key=f"points_{classe}_kmc2")
        # sram_pts = st.number_input("Points Sram", value=4, step=1)

with tab_KMC1:
    compo_kmc1=[('sram', 'ecaflip', 'cra'),
 ('sram', 'ecaflip', 'steamer'),
 ('sram', 'ecaflip', 'sadida'),
 ('sram', 'ecaflip', 'xelor'),
 ('sram', 'ecaflip', 'sacrieur'),
 ('sram', 'ecaflip', 'roublard'),
 ('sram', 'ecaflip', 'feca'),
 ('sram', 'ecaflip', 'zobal'),
 ('sram', 'ecaflip', 'pandawa'),
 ('sram', 'cra', 'osamodas'),
 ('sram', 'cra', 'steamer'),
 ('sram', 'cra', 'sadida'),
 ('sram', 'cra', 'xelor'),
 ('sram', 'cra', 'eniripsa'),
 ('sram', 'cra', 'enutrof'),
 ('sram', 'cra', 'sacrieur'),
 ('sram', 'cra', 'iop'),
 ('sram', 'cra', 'roublard'),
 ('sram', 'cra', 'feca'),
 ('sram', 'cra', 'zobal'),
 ('sram', 'cra', 'pandawa'),
 ('sram', 'osamodas', 'steamer'),
 ('sram', 'osamodas', 'sacrieur'),
 ('sram', 'osamodas', 'iop'),
 ('sram', 'osamodas', 'roublard'),
 ('sram', 'osamodas', 'pandawa'),
 ('sram', 'steamer', 'sadida'),
 ('sram', 'steamer', 'xelor'),
 ('sram', 'steamer', 'enutrof'),
 ('sram', 'steamer', 'roublard'),
 ('sram', 'steamer', 'feca'),
 ('sram', 'steamer', 'pandawa'),
 ('sram', 'sadida', 'sacrieur'),
 ('sram', 'sadida', 'roublard'),
 ('sram', 'sadida', 'feca'),
 ('sram', 'xelor', 'enutrof'),
 ('sram', 'xelor', 'roublard'),
 ('sram', 'eniripsa', 'enutrof'),
 ('sram', 'eniripsa', 'iop'),
 ('sram', 'eniripsa', 'roublard'),
 ('sram', 'eniripsa', 'pandawa'),
 ('sram', 'enutrof', 'sacrieur'),
 ('sram', 'enutrof', 'iop'),
 ('sram', 'enutrof', 'roublard'),
 ('sram', 'enutrof', 'feca'),
 ('sram', 'enutrof', 'zobal'),
 ('sram', 'sacrieur', 'iop'),
 ('sram', 'sacrieur', 'roublard'),
 ('sram', 'sacrieur', 'zobal'),
 ('sram', 'sacrieur', 'pandawa'),
 ('sram', 'iop', 'roublard'),
 ('sram', 'iop', 'feca'),
 ('sram', 'iop', 'zobal'),
 ('sram', 'iop', 'pandawa'),
 ('sram', 'roublard', 'feca'),
 ('sram', 'roublard', 'zobal'),
 ('sram', 'roublard', 'pandawa'),
 ('sram', 'feca', 'pandawa'),
 ('ecaflip', 'cra', 'steamer'),
 ('ecaflip', 'cra', 'sadida'),
 ('ecaflip', 'cra', 'xelor'),
 ('ecaflip', 'cra', 'sacrieur'),
 ('ecaflip', 'cra', 'roublard'),
 ('ecaflip', 'cra', 'feca'),
 ('ecaflip', 'cra', 'zobal'),
 ('ecaflip', 'cra', 'pandawa'),
 ('ecaflip', 'steamer', 'sadida'),
 ('ecaflip', 'steamer', 'xelor'),
 ('ecaflip', 'steamer', 'roublard'),
 ('ecaflip', 'steamer', 'feca'),
 ('ecaflip', 'steamer', 'pandawa'),
 ('ecaflip', 'sadida', 'sacrieur'),
 ('ecaflip', 'sadida', 'roublard'),
 ('ecaflip', 'sadida', 'feca'),
 ('ecaflip', 'xelor', 'roublard'),
 ('ecaflip', 'sacrieur', 'roublard'),
 ('ecaflip', 'sacrieur', 'zobal'),
 ('ecaflip', 'sacrieur', 'pandawa'),
 ('ecaflip', 'roublard', 'feca'),
 ('ecaflip', 'roublard', 'zobal'),
 ('ecaflip', 'roublard', 'pandawa'),
 ('ecaflip', 'feca', 'pandawa'),
 ('cra', 'osamodas', 'steamer'),
 ('cra', 'osamodas', 'sacrieur'),
 ('cra', 'osamodas', 'iop'),
 ('cra', 'osamodas', 'roublard'),
 ('cra', 'osamodas', 'pandawa'),
 ('cra', 'steamer', 'sadida'),
 ('cra', 'steamer', 'xelor'),
 ('cra', 'steamer', 'enutrof'),
 ('cra', 'steamer', 'roublard'),
 ('cra', 'steamer', 'feca'),
 ('cra', 'steamer', 'pandawa'),
 ('cra', 'sadida', 'sacrieur'),
 ('cra', 'sadida', 'roublard'),
 ('cra', 'sadida', 'feca'),
 ('cra', 'xelor', 'enutrof'),
 ('cra', 'xelor', 'roublard'),
 ('cra', 'eniripsa', 'enutrof'),
 ('cra', 'eniripsa', 'iop'),
 ('cra', 'eniripsa', 'roublard'),
 ('cra', 'eniripsa', 'pandawa'),
 ('cra', 'enutrof', 'sacrieur'),
 ('cra', 'enutrof', 'iop'),
 ('cra', 'enutrof', 'roublard'),
 ('cra', 'enutrof', 'feca'),
 ('cra', 'enutrof', 'zobal'),
 ('cra', 'sacrieur', 'iop'),
 ('cra', 'sacrieur', 'roublard'),
 ('cra', 'sacrieur', 'zobal'),
 ('cra', 'sacrieur', 'pandawa'),
 ('cra', 'iop', 'roublard'),
 ('cra', 'iop', 'feca'),
 ('cra', 'iop', 'zobal'),
 ('cra', 'iop', 'pandawa'),
 ('cra', 'roublard', 'feca'),
 ('cra', 'roublard', 'zobal'),
 ('cra', 'roublard', 'pandawa'),
 ('cra', 'feca', 'pandawa'),
 ('osamodas', 'steamer', 'roublard'),
 ('osamodas', 'steamer', 'pandawa'),
 ('osamodas', 'sacrieur', 'iop'),
 ('osamodas', 'sacrieur', 'roublard'),
 ('osamodas', 'sacrieur', 'pandawa'),
 ('osamodas', 'iop', 'roublard'),
 ('osamodas', 'iop', 'pandawa'),
 ('osamodas', 'roublard', 'pandawa'),
 ('steamer', 'sadida', 'roublard'),
 ('steamer', 'sadida', 'feca'),
 ('steamer', 'xelor', 'enutrof'),
 ('steamer', 'xelor', 'roublard'),
 ('steamer', 'enutrof', 'roublard'),
 ('steamer', 'enutrof', 'feca'),
 ('steamer', 'roublard', 'feca'),
 ('steamer', 'roublard', 'pandawa'),
 ('steamer', 'feca', 'pandawa'),
 ('sadida', 'sacrieur', 'roublard'),
 ('sadida', 'roublard', 'feca'),
 ('xelor', 'enutrof', 'roublard'),
 ('eniripsa', 'enutrof', 'iop'),
 ('eniripsa', 'enutrof', 'roublard'),
 ('eniripsa', 'iop', 'roublard'),
 ('eniripsa', 'iop', 'pandawa'),
 ('eniripsa', 'roublard', 'pandawa'),
 ('enutrof', 'sacrieur', 'iop'),
 ('enutrof', 'sacrieur', 'roublard'),
 ('enutrof', 'sacrieur', 'zobal'),
 ('enutrof', 'iop', 'roublard'),
 ('enutrof', 'iop', 'feca'),
 ('enutrof', 'iop', 'zobal'),
 ('enutrof', 'roublard', 'feca'),
 ('enutrof', 'roublard', 'zobal'),
 ('sacrieur', 'iop', 'roublard'),
 ('sacrieur', 'iop', 'zobal'),
 ('sacrieur', 'iop', 'pandawa'),
 ('sacrieur', 'roublard', 'zobal'),
 ('sacrieur', 'roublard', 'pandawa'),
 ('iop', 'roublard', 'feca'),
 ('iop', 'roublard', 'zobal'),
 ('iop', 'roublard', 'pandawa'),
 ('iop', 'feca', 'pandawa'),
 ('roublard', 'feca', 'pandawa')]
    
    st.html('<div style="text-align: center; font-size: 50px;font-weight: bold"> STATS KELEROG MASTER CUP #1 </div>')

    list_statsKMC1_images=[graphs_path_kmc1+"Compo les plus jouées.png",
                graphs_path_kmc1+"Nombre de pick des classes.png",
                graphs_path_kmc1+"Duos les plus joués.png",
                graphs_path_kmc1+"heat_Duos les plus joués.png"]

    st.image(list_statsKMC1_images, caption=None, use_container_width=True)
    with st.expander("Compositions d'équipe possibles :",expanded=False):
    # st.title("Compositions Possibles JDA#4")

        classes_voulues_kmc1=st.multiselect("Classes voulues",options=CLASSES, default=[],placeholder="Sélectionnez les classes voulues",max_selections=3,key="classes_voulues_kmc1")
        classes_interdites_kmc1=st.multiselect("Classes interdites",options=CLASSES, default=[],placeholder="Sélectionnez les classes dont vous ne voulez pas",key="classes_interdites_kmc1")

        st.button("Filtrer les compositions", key="filter_compositions_kmc1",on_click=filtrer_compositions, args=(classes_voulues_kmc1, classes_interdites_kmc1,"temp_compo_kmc1",compo_kmc1))
                
        points_kmc1_default={
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
        
        
        if "points_kmc1" not in st.session_state:
            st.session_state.points_kmc1={
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
        if "temp_points_kmc1" not in st.session_state:
            st.session_state.temp_points_kmc1={
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
        
        try:
            compositions_kmc1 = pd.DataFrame(st.session_state["temp_compo_kmc1"],columns=["C1","C2","C3"])

        except:
            compositions_kmc1 = pd.DataFrame(compo_kmc1,columns=["C1","C2","C3"])

        try:
            compositions_kmc1["Points"]= compositions_kmc1.apply(lambda row: st.session_state.points_kmc1[row['C1']] + st.session_state.points_kmc1[row['C2']] + st.session_state.points_kmc1[row['C3']], axis=1)
        except:
            pass

        st.write("### Nombre de compositions trouvées :", str(len(compositions_kmc1)))
        st.dataframe(compositions_kmc1,hide_index=True)
        st.image(image_path+"restrictions_kmc1.png" )
        st.write(f"""#### Points par classe\n 
Ces points servent à trier les {len(compositions_kmc1)} compositions possibles.
""")            

        st.button(label="Appliquer les points",on_click=update_points,args=(compositions_kmc1,"points_kmc1","temp_points_kmc1"),width="stretch",key="update_points_kmc1")

        for classe in CLASSES:
            st.session_state.temp_points_kmc1[classe] = st.number_input(f"Points {classe.capitalize()}", value=points_kmc1_default[classe], step=1, key=f"points_{classe}_kmc1")
        # sram_pts = st.number_input("Points Sram", value=4, step=1)
        
with tab_jda4:
    ronde=10
    
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


    st.title(f"Stats des 32 team qualifiées JDA#4".upper())

    st.image(graphs_path+"recaputilatif_qualifies_r10.png",use_container_width=True)
    st.image(graphs_path+"DRAFT winrate A-B.png",use_container_width=True)
    st.image(graphs_path+"DRAFT winrate classes.png",use_container_width=True)
    st.title(f"Stats à la fin des rondes JDA#4".upper())
    st.image(graphs_path+f"recapitulatif_winrates_ronde_{ronde}.jpg",use_container_width=True)
    list_stats_images=[graphs_path+"Kelerog_recaputilatif.png",
                    graphs_path+"Blair_recaputilatif.png",
                    graphs_path+"Tiliwan_recaputilatif.png",
                    graphs_path+"Talok_recaputilatif.png"]

    with st.expander("Stats par serveur :"):
        st.image(list_stats_images, caption=None, use_container_width=True)

    with st.expander("Détail des 154 équipes inscrites :"):
    # st.write("## Liste des 154 équipes inscrites")
        compos_inscrites=pd.read_csv("data/compositions_JDA#4.csv",sep=";")

        select_equipe = st.text_input("Rechercher une équipe")
        select_joueur=st.text_input("Rechercher un joueur")
        select_serveur=st.multiselect("Filtrer par serveur",options=SERVEURS, default=SERVEURS,placeholder="Sélectionnez le serveur",max_selections=5)
        select_classes=st.multiselect("Filtrer par classes/compo",options=CLASSES, default=[],placeholder="Sélectionnez les classes voulues",max_selections=3,key=123)
        deselect_classes=st.multiselect(label='Filtrer par classes/compo',label_visibility='collapsed',options=CLASSES, default=[],placeholder="Sélectionnez les classes dont vous ne voulez pas",key=122)
        def filtrer_inscrits(select_serveur, select_classes,deselect_classes):
            # Regrouper les colonnes dans une même série pour les traitements
            C_cols = ['C1', 'C2', 'C3']
            S_cols = ['Serveur1', 'Serveur2', 'Serveur3']
            J_cols = ['J1', 'J2', 'J3']

            # Condition 1 : Tous les éléments de clasv sont présents dans les colonnes C1 à C3
            cond1 = compos_inscrites[C_cols].apply(lambda row: all(cl in row.values for cl in select_classes), axis=1)

            # Condition 2 : Aucun élément de clasn ne doit être présent
            cond2 = compos_inscrites[C_cols].apply(lambda row: all(cl not in row.values for cl in deselect_classes), axis=1)

            # Condition 3 : Au moins un élément de servv dans les colonnes Serveur1 à Serveur3
            cond3 = compos_inscrites[S_cols].apply(lambda row: any(sv in row.values for sv in select_serveur), axis=1)
            
            # Condition 4 : select_joueur est contenu (partiellement, au début) dans une des colonnes J1 à J3
            if select_joueur:
                joueur = select_joueur.lower().strip()
                cond4 = compos_inscrites[J_cols].apply(
                    lambda row: any(joueur in str(j).lower() for j in row.values if pd.notna(j)), axis=1
                )
            else:
                cond4 = True  # Ne pas filtrer si aucun joueur spécifié
            
            # Condition 5 : nom d’équipe contient le texte entré (partiel, insensible à la casse)
            if select_equipe:
                equipe = select_equipe.lower().strip()
                cond5 = compos_inscrites["equipe"].str.lower().str.contains(equipe, na=False)
            else:
                cond5 = True

            # Combiner les conditions
            st.session_state["temp_inscrits"] = compos_inscrites[cond1 & cond2 & cond3 & cond4 &cond5]
            
        st.button("Filtrer les inscrits", key="filter_inscrits",on_click=filtrer_inscrits, args=(select_serveur, select_classes,deselect_classes))
        try:
            inscrits = pd.DataFrame(st.session_state["temp_inscrits"])

        except:
            inscrits = pd.DataFrame(compos_inscrites)

        st.dataframe(inscrits,hide_index=True,on_select='ignore')


    with st.expander("Compositions d'équipe possibles :"):
    # st.title("Compositions Possibles JDA#4")

        classes_voulues=st.multiselect("Classes voulues",options=CLASSES, default=[],placeholder="Sélectionnez les classes voulues",max_selections=3,key=124)
        classes_interdites=st.multiselect("Classes interdites",options=CLASSES, default=[],placeholder="Sélectionnez les classes dont vous ne voulez pas",key=125)

        st.button("Filtrer les compositions", key="filter_compositions_jda4",on_click=filtrer_compositions_jda4, args=(classes_voulues, classes_interdites,"temp_df",df))
                
        points_jda4_default={
            'cra':      4,
            'ecaflip':  6,
            'eniripsa': 9,
            'enutrof':  6,
            'feca':     7,
            'iop':      3,
            'osamodas': 8,
            'pandawa':  5,
            'roublard': 3,
            'sacrieur': 6,
            'sadida':   6,
            'sram':     0,
            'steamer':  5,
            'xelor':    10,
            'zobal':    7}
        
        
        if "points_jda4" not in st.session_state:
            st.session_state.points_jda4={
                'cra':      4,
                'ecaflip':  6,
                'eniripsa': 9,
                'enutrof':  6,
                'feca':     7,
                'iop':      3,
                'osamodas': 8,
                'pandawa':  5,
                'roublard': 3,
                'sacrieur': 6,
                'sadida':   6,
                'sram':     0,
                'steamer':  5,
                'xelor':    10,
                'zobal':    7}
        if "temp_points_jda4" not in st.session_state:
            st.session_state.temp_points_jda4={
                'cra':      4,
                'ecaflip':  6,
                'eniripsa': 9,
                'enutrof':  6,
                'feca':     7,
                'iop':      3,
                'osamodas': 8,
                'pandawa':  5,
                'roublard': 3,
                'sacrieur': 6,
                'sadida':   6,
                'sram':     0,
                'steamer':  5,
                'xelor':    10,
                'zobal':    7}
        
        try:
            compositions_jda4 = pd.DataFrame(st.session_state["temp_df"])

        except:
            compositions_jda4 = pd.DataFrame(df)

        try:
            compositions_jda4["Points"]= compositions_jda4.apply(lambda row: st.session_state.points_jda4[row['C1']] + st.session_state.points_jda4[row['C2']] + st.session_state.points_jda4[row['C3']], axis=1)
        except:
            pass

        st.write("### Nombre de compositions trouvées :", str(len(compositions_jda4)))
        st.dataframe(compositions_jda4,hide_index=True)
        st.image(image_path+"restrictions_JDA#4.png" )
        st.write("""#### Points par classe\n 
Ces points servent à trier les 171 compositions possibles.\n
J'ai mis des valeurs par défaut, mais vous pouvez les modifier si vous le souhaitez.
""")            

        st.button(label="Appliquer les points",on_click=update_points,args=(compositions_jda4,"points_jda4","temp_points_jda4"),width="stretch",key="update_points_jda4")

        for classe in CLASSES:
            st.session_state.temp_points_jda4[classe] = st.number_input(f"Points {classe.capitalize()}", value=points_jda4_default[classe], step=1, key=f"points_{classe}")
        # sram_pts = st.number_input("Points Sram", value=4, step=1)

