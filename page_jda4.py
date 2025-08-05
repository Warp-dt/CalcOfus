import streamlit as st
import pandas as pd

image_path='images/'
graphs_path=image_path+'graphs_jda4/'
st.set_page_config(page_title="CalcOfus",page_icon=image_path+"logo_InvRoxx_tab.png",layout="centered")

st.sidebar.image(image_path+"logo_jda4.png" )

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

st.title(f"Stats des 32 team qualifiées JDA#4".upper())

st.image(graphs_path+"recaputilatif_qualifies_r10.png",use_container_width=True)
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

with st.expander("Compositions d'équipe possibles :"):
# st.title("Compositions Possibles JDA#4")

    # classes_voulues=st.text_input("Classes voulues (séparées par des virgules)", value="",placeholder="ex: osamodas,enutrof",autocomplete="sram,ecaflip")
    classes_voulues=st.multiselect("Classes voulues",options=CLASSES, default=[],placeholder="Sélectionnez les classes voulues",max_selections=3,key=124)
    classes_interdites=st.multiselect("Classes interdites",options=CLASSES, default=[],placeholder="Sélectionnez les classes dont vous ne voulez pas",key=125)




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