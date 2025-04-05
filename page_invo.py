import streamlit as st
import dofusbook_scraping_requests as db
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="CalcInvo",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

st.write("# Le calculateur de roxx de tes invo préférées")

st.write("### Dans la suite de l'outil on part du principe que l'osa est lvl 200 et ses invo sont lvl 6")


######################
#SIDEBAR
######################

st.sidebar.image(image_path+"calcinvo_logo_nom_transp.png" )
st.sidebar.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio DofusBook**',icon="📚")


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
    stats_perso["Lvl"]=int(st.sidebar.number_input(label="Lvl",min_value=0,max_value=200,value=200))

    #stats
    stats_perso["Vita"]=int(st.sidebar.text_input("Vitalité globale", value=stats_perso["Lvl"]*5+50, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Intel"]=int(st.sidebar.text_input("Intelligence", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Chance"]=int(st.sidebar.text_input("Chance", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Agi"]=int(st.sidebar.text_input("Agilité", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["pui"]=int(st.sidebar.text_input("Puissance", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #do fixes
    stats_perso["Dofeu"]=int(st.sidebar.text_input("Dommages Feu", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doeau"]=int(st.sidebar.text_input("Dommages Eau", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doair"]=int(st.sidebar.text_input("Dommages Air", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Dopou"]=int(st.sidebar.text_input("Dommages de Poussée", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #soin
    stats_perso["Soin"]=int(st.sidebar.text_input("Soin", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    stats_perso["Do"]=int(st.sidebar.text_input("Dommages", value=0, max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
else:
    stats_perso["Lvl"]=int(st.sidebar.number_input(label="Lvl",min_value=0,max_value=200,value=db_stats["Lvl"]))

    #stats
    stats_perso["Vita"]=int(st.sidebar.text_input("Vitalité globale", value=db_stats["Vitalité"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Intel"]=int(st.sidebar.text_input("Intelligence", value=db_stats["Intelligence"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Chance"]=int(st.sidebar.text_input("Chance", value=db_stats["Chance"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Agi"]=int(st.sidebar.text_input("Agilité", value=db_stats["Agilité"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["pui"]=int(st.sidebar.text_input("Puissance", value=db_stats["Puissance"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #do fixes
    stats_perso["Dofeu"]=int(st.sidebar.text_input("Dommages Feu", value=db_stats["Do Feu"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doeau"]=int(st.sidebar.text_input("Dommages Eau", value=db_stats["Do Eau"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Doair"]=int(st.sidebar.text_input("Dommages Air", value=db_stats["Do Air"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    stats_perso["Dopou"]=int(st.sidebar.text_input("Dommages de Poussée", value=db_stats["Do Poussée"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #soin
    stats_perso["Soin"]=int(st.sidebar.text_input("Soin", value=db_stats["Soin"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    stats_perso["Do"]=int(st.sidebar.text_input("Dommages", value=db_stats["Do"], max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    # st.sidebar.write(db_stats)

######################
#Variables générales
######################

lvl_invo=6

def calcul_vita(base,multi):
    vita=base+multi*(stats_perso["Vita"]-1050)
    if vita>0 :
        return vita
    else:
        return 0


######################
#invo loop
######################
INVO_LIST=["dragonnet",'momie','crapaud','tofu','craqueleur','bouftou']
INVO_NOMS=["Dragonnet Rouge",'Momie koalak','Crapaud','Tofu','Craqueleur','Bouftou']

invo_infos={
    "dragonnet" : {
        'nom' : "Dragonnet Rouge"
        ,'element' : "Intel"
        ,'do' : "Dofeu"
        ,'stats_base' : 350
        ,'vita_base' : 300
        ,'vita_multiplicateur' : 0.2
        ,'sorts' : [
            {'nom' : "Dragofeu"
             ,'vmin' : 41
             ,'vmax' : 50
             ,'cc' : 0.15
             ,'vmin_cc' : 46
             ,'vmax_cc' : 55}
            ,{'nom' : "Flamme Persistante"
             ,'vmin' : 36
             ,'vmax' : 45
             ,'cc' : 0
             ,'vmin_cc' : 99999
             ,'vmax_cc' : 99999}
        ]        
    }
    ,"momie" : {
        'nom' : "Momie koalak"
        ,'element' : "Intel"
        ,'do' : "Dofeu"
        ,'stats_base' : 350
        ,'vita_base' : 180
        ,'vita_multiplicateur' : 0.15
        ,'sorts' : [
            {'nom' : "Malédiction du koalak"
             ,'vmin' : 26
             ,'vmax' : 35
             ,'cc' : 0
             ,'vmin_cc' : 99999
             ,'vmax_cc' : 99999}
            ,{'nom' : "Bandelette Soignante"
             ,'vmin' : 51
             ,'vmax' : 60
             ,"degats" : 40
             ,'cc' : 0
             ,'vmin_cc' : 99999
             ,'vmax_cc' : 99999}
        ]        
    }
    ,"crapaud" : {
        'nom' : "Crapaud"
        ,'element' : "Chance"
        ,'do' : "Doeau"
        ,'stats_base' : 350
        ,'vita_base' : 300
        ,'vita_multiplicateur' : 0.2
        ,'sorts' : [
            {'nom' : "Petit Splash"
             ,'vmin' : 26
             ,'vmax' : 29
             ,'cc' : 0.15
             ,'vmin_cc' : 29
             ,'vmax_cc' : 32}
            ,{'nom' : "Grand Splash"
             ,'vmin' : 29
             ,'vmax' : 32
             ,'cc' : 0.15
             ,'vmin_cc' : 31
             ,'vmax_cc' : 34}
        ]        
    }
    ,"tofu" : {
        'nom' : "Tofu"
        ,'element' : "Chance"
        ,'do' : "Doeau"
        ,'stats_base' : 350
        ,'vita_base' : 180
        ,'vita_multiplicateur' : 0.15
        ,'sorts' : [
            {'nom' : "Beco du Tofu"
             ,'vmin' : 14
             ,'vmax' : 17
             ,'cc' : 0.05
             ,'vmin_cc' : 16
             ,'vmax_cc' : 19}
            ,{'nom' : "Tofurieux"
             ,'vmin' : 41
             ,'vmax' : 45
             ,'cc' : 0
             ,'vmin_cc' : 44
             ,'vmax_cc' : 48}
        ]        
    }
    ,"craqueleur" : {
        'nom' : "Craqueleur"
        ,'element' : "Agi"
        ,'do' : "Doair"
        ,'stats_base' : 150
        ,'vita_base' : 300
        ,'vita_multiplicateur' : 0.2
        ,'sorts' : [
            {'nom' : "Ecrasement"
             ,'vmin' : 28
             ,'vmax' : 33
             ,'cc' : 0.05
             ,'vmin_cc' : 35
             ,'vmax_cc' : 35}
            ,{'nom' : "Frappe Étourdissante"
             ,'vmin' : 33
             ,'vmax' : 37
             ,'cc' : 0.1
             ,'vmin_cc' : 36
             ,'vmax_cc' : 40}
        ]        
    }
    ,"bouftou" : {
        'nom' : "Bouftou"
        ,'element' : "Agi"
        ,'do' : "Doair"
        ,'stats_base' : 150
        ,'vita_base' : 180
        ,'vita_multiplicateur' : 0.2
        ,'sorts' : [
            {'nom' : "Morsure du Bouftou"
             ,'vmin' : 31
             ,'vmax' : 35
             ,'cc' : 0.05
             ,'vmin_cc' : 35
             ,'vmax_cc' : 35}
            ,{'nom' : "Beuglement Assomant"
             ,'vmin' : 28
             ,'vmax' : 32
             ,'cc' : 0
             ,'vmin_cc' : 99999
             ,'vmax_cc' : 99999}
        ]        
    }
}

for invo in invo_infos.keys():
    l_col, r_col = st.columns((1,1))
    with l_col:

        st.write(f"## {invo_infos[invo]['nom']}")

        stat_base=350 #A VERIFIER

        stats_finales=invo_infos[invo]["stats_base"]+stats_perso[invo_infos[invo]["element"]]/2
        do_finaux=stats_perso[invo_infos[invo]["do"]]/2

        tab_vita="""
    | Vitalité | Boucliers bonus par mob (+20% vita) |
    | ----------- | ----------- |
    """
        tab_vita+="| "+str(int(calcul_vita(invo_infos[invo]['vita_base'],invo_infos[invo]['vita_multiplicateur'])))+" | "+str(int(calcul_vita(invo_infos[invo]['vita_base'],invo_infos[invo]['vita_multiplicateur'])*0.2))+"\n"

        st.write(tab_vita)
        st.text("")

        tab_sorts="| Sort | min | max | min cc | max cc | %cc | Moyenne |\n"
        tab_sorts+="| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |\n"

        for sort in invo_infos[invo]['sorts']:
            min_val=int((sort["vmin"]*(100+stats_finales)/100+do_finaux)//1)
            max_val=int((sort["vmax"]*(100+stats_finales)/100+do_finaux)//1)
            
            if sort["cc"]>0:
                cc=int(sort["cc"]*100)
                min_val_cc=int((sort["vmin_cc"]*(100+stats_finales)/100+do_finaux)//1)
                max_val_cc=int((sort["vmax_cc"]*(100+stats_finales)/100+do_finaux)//1)
                moy_val=int(((max_val+min_val)/2*(1-sort["cc"])+(max_val_cc+min_val_cc)/2*sort["cc"])//1)
            else:
                cc='-'
                min_val_cc='-'
                max_val_cc='-'
                moy_val=int((max_val+min_val)/2//1)

            tab_sorts+=f"| {sort['nom']} | {min_val} | {max_val} | {min_val_cc} | {max_val_cc} | {cc} | **{moy_val}** |\n"
       
        st.markdown(tab_sorts)
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