import streamlit as st
import dofusbook_scraping_requests as db
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="CalcoBoom",layout="wide")

st.write("# Calculateur de vitalité & dégats des bombes")


######################
#SIDEBAR
######################

st.sidebar.image(image_path+"calcoboom_logo_nom_transp.png" )
st.sidebar.page_link("https://d-bk.net/fr/tl/4BAS",label='**Biblio DofusBook**',icon="📚")


db_stats="no_db"

db_link=st.sidebar.text_input("Lien dofusbook",placeholder="https://d-bk.net/fr/t/A7si")
if db_link!='':
    try:
        db_stats=db.get_stats(db_link)  
        if "db_name" in db_stats.keys():
            st.sidebar.write("Stuff sélectionné :")
            st.sidebar.write(" "+db_stats["db_name"])
    except Exception as e:
            st.sidebar.write(f"Erreur dans la récupération des stats : {e}")
    
    # if type(db_stats)==str:
    #     st.sidebar.write(db_stats)
    # else:
    #     st.sidebar.write("Si les stats sont mal récupérées verifiez votre lien ou relancez la recherche, dofusbook bug parfois")
stats_perso={}

st.sidebar.write("# Stats du personnage") 
# st.sidebar.write("(les stats du parchotage et des points investis ne comptent pas pour les dégats des invo, seul l'équipement compte)") 

if db_link=='' or type(db_stats)==str:
    stats_perso["Lvl"]=int(st.sidebar.number_input(label="Lvl",min_value=0,max_value=200,value=200,step=1))

    #stats
    stats_perso["Vita"]=int(st.sidebar.number_input(label="Vitalité globale", value=stats_perso["Lvl"]*5+50,step=1,min_value=0))
    stats_perso["Intel"]=int(st.sidebar.number_input(label="Intelligence", value=0,step=1))
    stats_perso["Chance"]=int(st.sidebar.number_input(label="Chance", value=0,step=1))
    stats_perso["Agi"]=int(st.sidebar.number_input(label="Agilité", value=0,step=1))
    stats_perso["pui"]=int(st.sidebar.number_input(label="Puissance", value=0,step=1))

    #do fixes
    stats_perso["Dofeu"]=int(st.sidebar.number_input(label="Dommages Feu", value=0, step=1))
    stats_perso["Doeau"]=int(st.sidebar.number_input(label="Dommages Eau", value=0, step=1))
    stats_perso["Doair"]=int(st.sidebar.number_input(label="Dommages Air", value=0, step=1))

    stats_perso["Do"]=int(st.sidebar.number_input(label="Dommages", value=0, step=1))
else:
    stats_perso["Lvl"]=int(st.sidebar.number_input(label="Lvl",min_value=0,max_value=200,value=db_stats["Lvl"],step=1))

    #stats
    stats_perso["Vita"]=int(st.sidebar.number_input(label="Vitalité globale", value=db_stats["Vitalité"],step=1,min_value=0))
    stats_perso["Intel"]=int(st.sidebar.number_input(label="Intelligence", value=db_stats["Intelligence"],step=1))
    stats_perso["Chance"]=int(st.sidebar.number_input(label="Chance", value=db_stats["Chance"],step=1))
    stats_perso["Agi"]=int(st.sidebar.number_input(label="Agilité", value=db_stats["Agilité"],step=1))
    stats_perso["pui"]=int(st.sidebar.number_input(label="Puissance", value=db_stats["Puissance"],step=1))

    #do fixes
    stats_perso["Dofeu"]=int(st.sidebar.number_input(label="Dommages Feu", value=db_stats["Do Feu"],step=1))
    stats_perso["Doeau"]=int(st.sidebar.number_input(label="Dommages Eau", value=db_stats["Do Eau"],step=1))
    stats_perso["Doair"]=int(st.sidebar.number_input(label="Dommages Air", value=db_stats["Do Air"],step=1))

    stats_perso["Do"]=int(st.sidebar.number_input(label="Dommages", value=db_stats["Do"],step=1))

    # st.sidebar.write(db_stats)

######################
#Variables générales
######################


def calcul_vita_bombes(pvroub,lvlroub,coef_bombe,pvbase):
    return (pvroub-(lvlroub*5+50))*coef_bombe+pvbase 

lvls_bombes = ["4", "5", "6"]
vita_bombes_base={"4": 19
                  ,"5": 23
                  ,"6" : 28}
elements=["Feu","Air","Eau"]
type_bombes=["Explobombes","Tornabombes","Bombes à eau"]
elt_to_do={
    "Feu" : "Dofeu"
    ,"Air" : "Doair"
    ,"Eau" : "Doeau"
}

elt_to_carac={
    "Feu" : "Intel"
    ,"Air" : "Agi"
    ,"Eau" : "Chance"
}
bombes_do=dict()
bombes_do[elements[0]]={ #Feu
    '4':{
        'explo':{
            'min' : 14
            ,'max': 15 
        }
        ,'mur':{
            'min' : 15
            ,'max': 17 
        }
    }
    ,'5':{
        'explo':{
            'min' : 15
            ,'max': 16 
        }
        ,'mur':{
            'min' : 16
            ,'max': 18 
        }
    }
    ,'6':{
        'explo':{
            'min' : 20
            ,'max': 22 
        }
        ,'mur':{
            'min' : 19
            ,'max': 21 
        }
    }
}
bombes_do[elements[1]]={ #Air
    '4':{
        'explo':{
            'min' : 11
            ,'max': 12 
        }
        ,'mur':{
            'min' : 11
            ,'max': 13 
        }
    }
    ,'5':{
        'explo':{
            'min' : 12
            ,'max': 13 
        }
        ,'mur':{
            'min' : 12
            ,'max': 14 
        }
    }
    ,'6':{
        'explo':{
            'min' : 17
            ,'max': 19 
        }
        ,'mur':{
            'min' : 15
            ,'max': 17 
        }
    }
}
bombes_do[elements[2]]={ #Eau
    '4':{
        'explo':{
            'min' : 11
            ,'max': 12 
        }
        ,'mur':{
            'min' : 11
            ,'max': 13 
        }
    }
    ,'5':{
        'explo':{
            'min' : 12
            ,'max': 13 
        }
        ,'mur':{
            'min' : 12
            ,'max': 14 
        }
    }
    ,'6':{
        'explo':{
            'min' : 14
            ,'max': 16 
        }
        ,'mur':{
            'min' : 12
            ,'max': 14 
        }
    }
}
def calcul_bonus_combo(bombes_combo):#bonus combo de 1 à 10, 0 signifie qu'il n'y a pas de bombe
    combo_total=0

    for combo in bombes_combo:
        if combo<6:
            combo_total+=combo*20
        else :
            combo_total+=100+30*(combo-5)

    return combo_total

# def calcul_degats_bombes(dommages_min=20,dommages_max=22,stats=1000,do=0,per_do=100,bonus_combo=750,distance=[0,0,0]):
#     degats_min=int(dommages_min*(stats+100)/100+do)
#     degats_max=int(dommages_max*(stats+100)/100+do)

#     degats_min_combo=degats_min*(bonus_combo/100+1)*(1-distance/10)*(1+per_do/100)
#     degats_max_combo=degats_max*(bonus_combo/100+1)*(1-distance/10)*(1+per_do/100)

#     return degats_min_combo,degats_max_combo

def calcul_degats_mur(dommages_min=20,dommages_max=22,stats=1000,do=0,per_do=100,bonus_combo=750):
    degats_min=int(dommages_min*(stats+100)/100+do)
    degats_max=int(dommages_max*(stats+100)/100+do)

    degats_min_combo=degats_min*(bonus_combo/100+1)*(1+per_do/100)
    degats_max_combo=degats_max*(bonus_combo/100+1)*(1+per_do/100)

    return int(degats_min_combo),int(degats_max_combo)

def calcul_degats_explo(dommages_min=20,dommages_max=22,stats=1000,do=0,per_do=100,bonus_combo=750,distance=1):
    degats_min=int(dommages_min*(stats+100)/100+do)
    degats_max=int(dommages_max*(stats+100)/100+do)

    degats_min_combo=degats_min*(bonus_combo/100+1)*(1-distance/10)*(1+per_do/100)
    degats_max_combo=degats_max*(bonus_combo/100+1)*(1-distance/10)*(1+per_do/100)

    return int(degats_min_combo),int(degats_max_combo)

tab_mur,tab_explo,tab_vita=st.tabs(["Murs","Explosions","Vitalité"])

######################
#TAB VITALITÉ
######################

with tab_vita:
    #BOMBE EAU
    st.write("### Bombe à eau")
    left_BE, right_BE = st.columns((1,1))
    with left_BE:

        BE_lvl_bombes_unchecked = st.pills("Lvl Bombe", lvls_bombes, selection_mode="single",default="6",key=2)
        if BE_lvl_bombes_unchecked in lvls_bombes:
            BE_lvl_bombes=BE_lvl_bombes_unchecked
        else:
            BE_lvl_bombes=lvls_bombes[2]
        
        tab_vita_BE="""
    | Vitalité |
    | ----------- |
    """
        tab_vita_BE+="| "+str(int(calcul_vita_bombes(stats_perso["Vita"],stats_perso["Lvl"],0.35,vita_bombes_base[BE_lvl_bombes])))+" |\n"
        st.write(tab_vita_BE)
    with right_BE:
        st.text("")
        st.image(image_path+"Bombe_a_eau.png")

    #BOMBE FEU
    st.write("### Explobombe")
    left_BF, right_BF = st.columns((1,1))
    with left_BF:
        BF_lvl_bombes_unchecked = st.pills("Lvl Bombe", lvls_bombes, selection_mode="single",default="6",key=0)
        if BF_lvl_bombes_unchecked in lvls_bombes:
            BF_lvl_bombes=BF_lvl_bombes_unchecked
        else:
            BF_lvl_bombes=lvls_bombes[2]
        
        tab_vita_BF="""
    | Vitalité |
    | ----------- |
    """
        tab_vita_BF+="| "+str(int(calcul_vita_bombes(stats_perso["Vita"],stats_perso["Lvl"],0.27,vita_bombes_base[BF_lvl_bombes])))+" |\n"
        st.write(tab_vita_BF)
    with right_BF:
        st.text("")
        st.image(image_path+"Explobombe.png")

    #BOMBE AIR
    st.write("### Tornabombe")
    left_BA, right_BA = st.columns((1,1))
    with left_BA:

        BA_lvl_bombes_unchecked = str(st.pills("Lvl Bombe", lvls_bombes, selection_mode="single",default="6",key=1))
        if BA_lvl_bombes_unchecked in lvls_bombes:
            BA_lvl_bombes=BA_lvl_bombes_unchecked
        else:
            BA_lvl_bombes=lvls_bombes[2]
        
        tab_vita_BA="""
    | Vitalité |
    | ----------- |
    """
        tab_vita_BA+="| "+str(int(calcul_vita_bombes(stats_perso["Vita"],stats_perso["Lvl"],0.27,vita_bombes_base[BA_lvl_bombes])))+" |\n"
        st.write(tab_vita_BA)
    with right_BA:
        st.text("")
        st.image(image_path+"Tornabombe.png")

######################
#TAB MUR
######################

with tab_mur:

    with st.container(border=True):   
        st.write("### Boosts sur roublard") 
        stats_perso["roub_pui"]=int(st.number_input(label="Puissance", value=0, key=201, step=1))
        stats_perso["roub_do"]=int(st.number_input(label="Dommages", value=0, key=202, step=1))
        stats_perso["roub_per_do"]=int(st.number_input(label="% dommages", value=0, key=203, step=1))
 
    with st.container(border=True):   
        st.write("### Bombes constituant le mur") 

        mur_g,mur_m,mur_d = st.columns((1,1,1))

        nb_bombes=mur_g.number_input(label="Nombre de Bombes",min_value=1,max_value=3,value=2, step=1)
        bombes_element=mur_m.selectbox("Élément des bombes",options=elements,index=0)
        lvl_bombes_mur=str(mur_d.number_input(label="Lvl des Bombes",min_value=4,max_value=6,value=6, step=1))

        bombes = st.columns((1,1,1))
        bombes_combo=[0,0,0]
        for t in range(nb_bombes):
            bombes_combo[t]=bombes[t].number_input(label=f"Bonus combo Bombe {t+1}",min_value=0,max_value=10,value=5,key=210+t, step=1)

        bonus_combo_total=calcul_bonus_combo(bombes_combo)

    st.markdown("# Dégats du mur :")
    mur_resultat_tab="""
| Dégats min | Dégats max | Moyenne |
| ----------- | ----------- | ----------- |
"""     
    # st.write(bombes_do[bombes_element]["4"],lvl_bombes_mur)
    # st.write(f"stats roub : {stats_perso[elt_to_carac[bombes_element]]}")
    # st.write(f"doroub : {stats_perso[elt_to_do[bombes_element]]}")
    # st.write(f"pui roub : {stats_perso['pui']}")
    # st.write(f"do roub : {stats_perso['Do']}")
    # st.write(f"stats roub : {stats_perso[elt_to_carac[bombes_element]]}")
    mur_min,mur_max=calcul_degats_mur(   bombes_do[bombes_element][lvl_bombes_mur]["mur"]["min"]
                                            ,bombes_do[bombes_element][lvl_bombes_mur]["mur"]["max"]
                                            ,stats=stats_perso[elt_to_carac[bombes_element]]+stats_perso["pui"]+stats_perso["roub_pui"]
                                            ,do=stats_perso[elt_to_do[bombes_element]]+stats_perso["Do"]+stats_perso["roub_do"]
                                            ,per_do=stats_perso["roub_per_do"]
                                            ,bonus_combo=bonus_combo_total)
    mur_resultat_tab+="| "+str(mur_min)+" | "+str(mur_max)+" | "+str(int((mur_min+mur_max)/2))+" |\n"
    st.markdown(mur_resultat_tab)
######################
#TAB EXPLOSION
######################

with tab_explo:

    with st.container(border=True):   
        st.write("### Boosts sur roublard") 
        stats_perso["roub_pui"]=int(st.number_input(label="Puissance", value=0, key=401,step=1))
        stats_perso["roub_do"]=int(st.number_input(label="Dommages", value=0, key=402,step=1))
        stats_perso["roub_per_do"]=int(st.number_input(label="% dommages", value=0, key=403,step=1))
 
    
    with st.container(border=True):   
        st.write("### Bombes dans l'explosion") 
        nb_bombes_explo=st.number_input(label="Nombre de Bombes",min_value=1,max_value=3,value=3, key=501, step=1)

        bombes_explo = st.columns((1,)*nb_bombes_explo)
        for b_id in range(nb_bombes_explo):
            with bombes_explo[b_id]:
                st.markdown(f"#### Bombe {b_id+1}")
        
        bombes_explo_elt=[bombes_explo[b_id].selectbox("Élément",options=elements,index=0,key=601+b_id*10) for b_id in range(nb_bombes_explo)]
        bombes_explo_lvl=[str(bombes_explo[b_id].number_input(label="Lvl",min_value=4,max_value=6,value=6,key=600+b_id*10)) for b_id in range(nb_bombes_explo)]
        bombes_explo_combo=[(bombes_explo[b_id].number_input(label=f"Bonus combo",min_value=0,max_value=10,value=5,key=605+b_id*10)) for b_id in range(nb_bombes_explo)]
        bombes_explo_distance=[(bombes_explo[b_id].number_input(label="Distance",min_value=1,max_value=2,value=1,key=606+b_id*10)) for b_id in range(nb_bombes_explo)]
        bombes_explo_do=[int(bombes_explo[b_id].number_input(label="Boost dommages (sur bombe)", value=0, key=603+b_id*10, step=1)) for b_id in range(nb_bombes_explo)]
        bombes_explo_pui=[int(bombes_explo[b_id].number_input(label="Boost puissance (sur bombe)", value=0, key=602+b_id*10, step=1)) for b_id in range(nb_bombes_explo)]
        bombes_explo_per_do=[int(bombes_explo[b_id].number_input(label="Boost % dommages (sur bombe)", value=0, key=604+b_id*10, step=1)) for b_id in range(nb_bombes_explo)]
        
        bonus_combo_total_explo=calcul_bonus_combo(bombes_explo_combo)

        degats_explo_min=[]
        degats_explo_max=[]
        for b_id in range(nb_bombes_explo):
            
            temp_explo_min,tem_explo_max=calcul_degats_explo(bombes_do[bombes_explo_elt[b_id]][bombes_explo_lvl[b_id]]["explo"]["min"]
                                                            ,bombes_do[bombes_explo_elt[b_id]][bombes_explo_lvl[b_id]]["explo"]["max"]
                                                            ,stats=stats_perso[elt_to_carac[bombes_explo_elt[b_id]]]+stats_perso["pui"]+bombes_explo_pui[b_id]+stats_perso["roub_pui"]
                                                            ,do=stats_perso["Do"+bombes_explo_elt[b_id].lower()]+stats_perso["Do"]+bombes_explo_do[b_id]+stats_perso["roub_do"]
                                                            ,per_do=bombes_explo_per_do[b_id]
                                                            ,bonus_combo=bonus_combo_total_explo                                                            
                                                            ,distance=bombes_explo_distance[b_id])
            degats_explo_min.append(temp_explo_min)
            degats_explo_max.append(tem_explo_max)


    st.markdown("# Dégats de l'explosion :")
    explo_resultat_tab="""
| Dégats min | Dégats max | Moyenne |
| ----------- | ----------- | ----------- |
"""     
    explo_resultat_tab+="| "+str(sum(degats_explo_min))+" | "+str(sum(degats_explo_max))+" | "+str(int((sum(degats_explo_min)+sum(degats_explo_max))/2))+" |\n"
    st.markdown(explo_resultat_tab)

    st.markdown("## Détails :")
    for b_id in range(nb_bombes_explo):
        st.markdown(f"### Bombe {b_id+1}")
        st.markdown(f"""
| Dégats min | Dégats max | Moyenne |
| ----------- | ----------- | ----------- |
| {degats_explo_min[b_id]} | {degats_explo_max[b_id]} | {int((degats_explo_min[b_id]+degats_explo_max[b_id])/2)} |

""")



st.divider()
st.write("Merci au [discord roublard](https://discord.gg/QYKu5Qs5Eh) et à [Emrys](https://www.youtube.com/@emrys30) pour l'aide apportée lors de la création de l'outil ❤️")

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