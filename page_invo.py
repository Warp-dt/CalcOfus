import streamlit as st
import dofusbook_scraping_requests as db
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="CalcInvo",layout="wide")

st.write("# Le calculateur de roxx de tes invo préférées")

######################
#SIDEBAR
######################

st.sidebar.image(image_path+"calcinvo_logo_nom_transp.png" )
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
    
    #soin
    stats_perso["Soin"]=int(st.sidebar.number_input(label="Soin", value=0, step=1))

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
    
    #soin
    stats_perso["Soin"]=int(st.sidebar.number_input(label="Soin", value=db_stats["Soin"], step=1))

    stats_perso["Do"]=int(st.sidebar.number_input(label="Dommages", value=db_stats["Do"],step=1))

    # st.sidebar.write(db_stats)

######################
#Variables générales
######################


def calcul_vita(base,multi):
    vita=base+multi*max(stats_perso["Vita"]-(stats_perso["Lvl"]*5+50),0)
    if vita>0 :
        return vita
    else:
        return 0


######################
#invo loop
######################
INVO_LIST=["dragonnet",'momie','crapaud','tofu','craqueleur','bouftou']
INVO_NOMS=["Dragonnet Rouge",'Momie koalak','Crapaud','Tofu','Craqueleur','Bouftou']
LVL_INVOS=[1,2,3,4,5,6]

stat_heredite={
    1 : 0.3
    ,2 : 0.3
    ,3 : 0.3
    ,4 : 0.3
    ,5 : 0.4
    ,6 : 0.5
}

invo_infos={
    "dragonnet" : {
        'nom' : "Dragonnet Rouge"
        ,'lvl' : [117,167]
        ,'element' : "Intel"
        ,'do' : "Dofeu"
        ,'stats_base' : [100,150,200,250,300,350]
        ,'vita_base' : 100+stats_perso["Lvl"]
        ,'vita_multiplicateur' : [0.15,0.15,0.15,0.15,0.15,0.2]
        ,'sorts' : [
            {'nom' : "Dragofeu"
             ,'vmin' : [14,17,20,23,28,33]
             ,'vmax' : [23,26,29,32,37,42]
             ,'cc' : 0.15
             ,'vmin_cc' : [17,20,23,26,29,36]
             ,'vmax_cc' : [26,29,32,35,38,45]}
            ,{'nom' : "Flamme Persistante"
             ,'vmin' : [36,36,36,36,36,36]
             ,'vmax' : [45,45,45,45,45,45]
             ,'cc' : 0
             ,'vmin_cc' : [0,0,0,0,0,0]
             ,'vmax_cc' : [0,0,0,0,0,0]}
        ]        
    }
    ,"momie" : {
        'nom' : "Momie koalak"
        ,'lvl' : [69,119]
        ,'element' : "Intel"
        ,'do' : "Dofeu"
        ,'stats_base' : [70,105,150,180,220,350]
        ,'vita_base' : (60+stats_perso["Lvl"]*0.6)//1
        ,'vita_multiplicateur' : [0.1,0.1,0.1,0.1,0.1,0.15]
        ,'sorts' : [
            {'nom' : "Malédiction du koalak"
             ,'vmin' : [17,18,19,20,21,26]
             ,'vmax' : [26,27,28,29,30,35]
             ,'cc' : 0
             ,'vmin_cc' : [0,0,0,0,0,0]
             ,'vmax_cc' : [0,0,0,0,0,0]}
            ,{'nom' : "Bandelette Soignante"
             ,'vmin' : 51
             ,'vmax' : 60
             ,"degats" : 40
             ,'cc' : 0
             ,'vmin_cc' : [0,0,0,0,0,0]
             ,'vmax_cc' : [0,0,0,0,0,0]}
        ]        
    }
    ,"crapaud" : {
        'nom' : "Crapaud"
        ,'lvl' : [105,155]
        ,'element' : "Chance"
        ,'do' : "Doeau"
        ,'stats_base' : [100,150,200,250,300,350]
        ,'vita_base' : 100+stats_perso["Lvl"]
        ,'vita_multiplicateur' : [0.15,0.15,0.15,0.15,0.15,0.2]
        ,'sorts' : [
            {'nom' : "Petit Splash"
             ,'vmin' : [14,16,18,20,23,26]
             ,'vmax' : [17,19,21,23,26,29]
             ,'cc' : 0.15
             ,'vmin_cc' : [17,19,21,23,26,29]
             ,'vmax_cc' : [20,22,24,26,29,32]}
            ,{'nom' : "Grand Splash"
             ,'vmin' : [18,19,20,21,24,29]
             ,'vmax' : [21,22,23,24,27,32]
             ,'cc' : 0.15
             ,'vmin_cc' : [20,21,22,23,26,31]
             ,'vmax_cc' : [23,24,24,26,29,34]}
        ]        
    }
    ,"tofu" : {
        'nom' : "Tofu"
        ,'lvl' : [57,107]
        ,'element' : "Chance"
        ,'do' : "Doeau"
        ,'stats_base' : [100,150,200,250,300,350]
        ,'vita_base' : (60+stats_perso["Lvl"]*0.6)//1
        ,'vita_multiplicateur' : [0.1,0.1,0.1,0.1,0.1,0.15]
        ,'sorts' : [
            {'nom' : "Beco du Tofu"
             ,'vmin' : [7,8,9,10,12,14]
             ,'vmax' : [10,11,12,13,15,17]
             ,'cc' : 0.05
             ,'vmin_cc' : [9,10,11,12,14,16]
             ,'vmax_cc' : [12,13,14,15,17,19]}
            ,{'nom' : "Tofurieux"
             ,'vmin' : [21,23,25,27,34,41]
             ,'vmax' : [25,27,29,31,38,45]
             ,'cc' : 0
             ,'vmin_cc' : [0,0,0,0,0,0]
             ,'vmax_cc' : [0,0,0,0,0,0]}
        ]        
    }
    ,"craqueleur" : {
        'nom' : "Craqueleur"
        ,'lvl' : [111,161]
        ,'element' : "Agi"
        ,'do' : "Doair"
        ,'stats_base' : [10,30,50,70,100,150]
        ,'vita_base' : 100+stats_perso["Lvl"]
        ,'vita_multiplicateur' : [0.1,0.1,0.1,0.1,0.15,0.2]
        ,'sorts' : [
            {'nom' : "Ecrasement"
             ,'vmin' : [15,17,19,22,25,28]
             ,'vmax' : [19,21,23,26,29,33]
             ,'cc' : 0.05
             ,'vmin_cc' : [21,23,25,29,31,35]
             ,'vmax_cc' : [21,23,25,29,31,35]}
            ,{'nom' : "Frappe Étourdissante"
             ,'vmin' : [22,24,26,28,30,33]
             ,'vmax' : [26,28,30,32,34,37]
             ,'cc' : 0.1
             ,'vmin_cc' : [25,27,29,31,33,36]
             ,'vmax_cc' : [29,31,33,35,37,40]}
        ]        
    }
    ,"bouftou" : {
        'nom' : "Bouftou"
        ,'lvl' : [63,113]
        ,'element' : "Agi"
        ,'do' : "Doair"
        ,'stats_base' : [10,30,50,70,100,150]
        ,'vita_base' : (60+stats_perso["Lvl"]*0.6)//1
        ,'vita_multiplicateur' : [0.1,0.1,0.1,0.1,0.15,0.2]
        ,'sorts' : [
            {'nom' : "Morsure du Bouftou"
             ,'vmin' : [18,20,22,24,26,31]
             ,'vmax' : [22,24,26,28,30,35]
             ,'cc' : 0.05
             ,'vmin_cc' : [22,24,26,28,30,35]
             ,'vmax_cc' : [22,24,26,28,30,35]}
            ,{'nom' : "Beuglement Assomant"
             ,'vmin' : [13,16,19,22,25,28]
             ,'vmax' : [17,20,23,26,29,32]
             ,'cc' : 0
             ,'vmin_cc' : [0,0,0,0,0,0]
             ,'vmax_cc' : [0,0,0,0,0,0]}
        ]        
    }
}


pillskey=0
for invo in invo_infos.keys():
    l_col, r_col = st.columns((1,1))
    with l_col:

        st.write(f"## {invo_infos[invo]['nom']}")
        
        #TO DO        
        #################################
        # moduler le lvl de base de l'invo selon le lvl de l'osa
        #################################
        if stats_perso["Lvl"]<invo_infos[invo]['lvl'][0]:
            lvl_base=4
        elif stats_perso["Lvl"]<invo_infos[invo]['lvl'][1]:
            lvl_base=5
        else:
            lvl_base=6

        lvl_invo_unchecked = l_col.pills("Lvl invocation", LVL_INVOS, selection_mode="single",default=lvl_base,key=pillskey)
        pillskey+=1
        if lvl_invo_unchecked in LVL_INVOS:
            lvl_invo=lvl_invo_unchecked
        else:
            lvl_invo=lvl_base

        stats_finales=invo_infos[invo]["stats_base"][lvl_invo-1]+stats_perso[invo_infos[invo]["element"]]/2
        do_finaux=stats_perso[invo_infos[invo]["do"]]/2
        soin_finaux=stats_perso["Soin"]/2

        tab_vita="""
    | Vitalité | Boucliers bonus par mob (+20% vita) |
    | ----------- | ----------- |
    """
        tab_vita+="| "+str(int(calcul_vita(invo_infos[invo]['vita_base'],invo_infos[invo]['vita_multiplicateur'][lvl_invo-1])))+" | "+str(int(calcul_vita(invo_infos[invo]['vita_base'],invo_infos[invo]['vita_multiplicateur'][lvl_invo-1])*0.2))+"\n"

        st.write(tab_vita)
        st.text("")

        
        if invo!='momie':
            tab_sorts="| Sort | min | max | min cc | max cc | %cc | Moyenne |\n"
            tab_sorts+="| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |\n"

            for sort in invo_infos[invo]['sorts']: 
                min_val=int((sort["vmin"][lvl_invo-1]*(100+stats_finales)/100+do_finaux)//1)
                max_val=int((sort["vmax"][lvl_invo-1]*(100+stats_finales)/100+do_finaux)//1)
                
                if sort["cc"]>0:
                    cc=int(sort["cc"]*100)
                    min_val_cc=int((sort["vmin_cc"][lvl_invo-1]*(100+stats_finales)/100+do_finaux)//1)
                    max_val_cc=int((sort["vmax_cc"][lvl_invo-1]*(100+stats_finales)/100+do_finaux)//1)
                    moy_val=int(((max_val+min_val)/2*(1-sort["cc"])+(max_val_cc+min_val_cc)/2*sort["cc"])//1)
                else:
                    cc='-'
                    min_val_cc='-'
                    max_val_cc='-'
                    moy_val=int((max_val+min_val)/2//1)

                tab_sorts+=f"| {sort['nom']} | {min_val} | {max_val} | {min_val_cc} | {max_val_cc} | {cc} | **{moy_val}** |\n"
       
            st.markdown(tab_sorts)
        else: #cas de la momie avec son sort de soin là
            #sort de dégats
            tab_malé="| Sort | Dégats min | Dégats max | Dégats moyens | Soin min | Soin max | Soin moyen |\n"
            tab_malé+="| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |\n"
            malé = invo_infos[invo]['sorts'][0]
            min_val=int((malé["vmin"][lvl_invo-1]*(100+stats_finales)/100+do_finaux)//1)
            max_val=int((malé["vmax"][lvl_invo-1]*(100+stats_finales)/100+do_finaux)//1)
            moy_val=int((max_val+min_val)/2//1)
            tab_malé+=f"| {malé['nom']} | {min_val} | {max_val} | **{moy_val}** | {int((min_val*0.6)//1)} | {int((max_val*0.6)//1)} | **{int((moy_val*0.6)//1)}** ||\n"

            #sort de soin
            tab_soin="| Sort | Soin min | Soin max | Soin Moyen | Dégats subis (par la momie) |\n"
            tab_soin+="| ----------- | ----------- | ----------- | ----------- | ----------- |\n"
            soin = invo_infos[invo]['sorts'][1]
            min_soin=int((soin["vmin"]*(100+stats_finales)/100+soin_finaux)//1)
            max_soin=int((soin["vmax"]*(100+stats_finales)/100+soin_finaux)//1)
            moy_soin=int((max_soin+min_soin)/2//1)
            dégats=int((soin["degats"]*(100+stats_finales)/100+do_finaux)//1)
            tab_soin+=f"| {soin['nom']} | {min_soin} | {max_soin} | **{moy_soin}** | {dégats} |\n"

            st.markdown(tab_malé)
            st.markdown(tab_soin)
        st.text("")


    with r_col:
        st.text("")
        st.image(image_path+f"{invo}2.png")


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