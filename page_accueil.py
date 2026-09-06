import streamlit as st
image_path='images/'

######################
# Page Title
######################

st.set_page_config(page_title="CalcOfus",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")


# import platform
# plat=platform.platform()
# if plat=="Linux-6.1.100+-x86_64-with-glibc2.31": #streamlit
#     st.write("J'ai changé l'hébergement de mon application, vous pouvez la retrouver sur CalcOfus.fr 🥳")
#     st.link_button("clique ici pour aller sur le nouveau site! (je vais bientôt supprimer celui-ci, sauvegarde l'url du nouveau)", "https://calcofus.fr", help=None, type="secondary", disabled=False, use_container_width=True)

# elif plat=="Linux-6.8.0-52-generic-x86_64-with-glibc2.36": #serveur 
#     pass
# else :
#     st.write("🥳 J'ai changé l'hébergement de mon application, vous pouvez la retrouver sur CalcOfus.fr 🥳")
#     st.link_button("clique ici pour aller sur le nouveau site! (je vais bientôt supprimer celui-ci, sauvegarde l'url du nouveau)", "https://calcofus.fr", help=None, type="secondary", disabled=False, use_container_width=True)
######################
#SIDEBAR
######################

with st.sidebar:
    st.image(image_path+"logo_nom_transp.png" )
    # st.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio DofusBook**',icon="📚")

##############
# Présentation
##############

st.html('<div style="text-align: center; font-size: 50px;font-weight: bold"> Calcofus </div>')
st.html("""
        <div style='text-align: center; 
                    font-size:20px'>
        Sur cette page vous pouvez retrouver les différents outils que j'ai créé pour vous aider dans votre aventure sur Dofus Touch.
        </div>""")
st.html("""
        <div style='text-align: center; 
                    font-size:20px'>
Utilisez la barre sur la gauche pour naviguer entre les outils, ou bien cliquez sur les noms des outils ci-dessous.
        </div>""")

##############
# Outils
##############
col1, col2,col3 = st.columns((1,1,1),vertical_alignment='top')
with col1:
    with st.container(border=True):
        st.page_link("page_invo.py",label='**CalcInvo**',icon=":material/cruelty_free:", use_container_width=True)
        st.write("""Calculateur de dégats des invocations""")
# - importation des stats depuis dofusbook possible
# - ou entrée des stats custom dans la sidebar""")
with col2:
    with st.container(border=True):
        st.page_link("page_bombes.py",label='**CalcoBoom**',icon=":material/bomb:", use_container_width=True)
        st.write("""Calculateur de dégats des bombes""")
# - importation des stats depuis dofusbook possible
# - ou entrée des stats custom dans la sidebar""")
with col3:
    with st.container(border=True):
        st.page_link("page_dopou.py",label='**CalcOpou**',icon=":material/directions_alt:", use_container_width=True)
        st.write("Calculateur de dégats de poussée")

col4, col5,col6 = st.columns((1,1,1))
with col4:
    with st.container(border=True):
        st.page_link("page_sorts.py",label='**CalcSorts**',icon=":material/sword_rose:", use_container_width=True)
        st.write("Calculateur de ligne de dégats de sort")
with col5:
    with st.container(border=True):
        st.page_link("page_taclefuite.py",label='**CalcoTac**',icon=":material/do_not_step:", use_container_width=True)
        st.write("Calculateur de Tacle/Fuite")
with col6:
    with st.container(border=True):
        st.page_link("page_ret.py",label="**CalcoRet**", icon=":material/star:", use_container_width=True)
        st.text("Calculateur de Retrait/Esquive")

col7, col8,col9 = st.columns((1,1,1))
with col7:
    with st.container(border=True):
        st.page_link("page_persofus.py",label='**PersOfus**',icon=":material/data_loss_prevention:", use_container_width=True)
        st.write("Générateur de lien vers les pages perso à partir du nom de compte.")

with col8:
    with st.container(border=True):
        st.page_link("page_stattn.py",label="**Stats Tournois**", icon=":material/bar_chart:", use_container_width=True)
        st.text("Stats des Tournois PVP")
        st.link_button("Site du KTA ⚔️", "https://ktarena.com/fr/", help=None, type="secondary", icon="⚔️", disabled=False, use_container_width=True)
        st.link_button("Discord Tournois 🗨️", "https://discord.gg/nC7g6vDnmT", help=None, type="secondary", icon="🗨️", disabled=False, use_container_width=True)

with col9:
    with st.container(border=True):
        st.page_link("page_restrictofus.py",label="**RestrictOfus**", icon=":material/rule:", use_container_width=True)
        st.text("Créateur de restrictions pour Tournois PVP")

st.html("""
        <div style='text-align: center; 
                    font-size:20px'>
Vous pouvez aussi suivre mes différents projets :
        </div>""")
with st.container(border=True):    
    st.page_link("https://discord.gg/dfDV8Zvwqp",label='**Dofus Touls**',icon="🗨️")
    st.write("Sur ce serveur discord tu peux retrouver toutes les ressources autour de mes projets ainsi qu'un endroit pour discuter !")
    st.link_button("Rejoins nous sur discord 🤩", "https://discord.gg/dfDV8Zvwqp", help=None, type="secondary", icon="🤩", disabled=False, use_container_width=True)

##############
# Réseaux
##############
twitch, youtube,warpBot = st.columns((1,1,1))
with twitch:
    with st.container(border=True):    
        st.page_link("https://www.twitch.tv/warp_is_fine",label='**Twitch**',icon="👾", use_container_width=True)
        st.write("Viens suivre avec moi les meilleurs tournois de dofus touch ❤️")
        st.link_button("Follow la chaîne pour être prévenu quand je lance un stream", "https://www.twitch.tv/warp_is_fine", help=None, type="secondary", icon="🎙️", disabled=False, use_container_width=True)

with youtube:
    with st.container(border=True):
        st.page_link("https://www.youtube.com/channel/UCVMa-curO2R2fJNQALwB2tQ",label='**Youtube**',icon="🔴", use_container_width=True)
        st.write("Ma chaîne youtube est remplie de matchs de tournois commentés, de retransmission de mes participations, et plus encore")
        st.link_button("Abonne toi pour ne rien manquer", "https://www.youtube.com/channel/UCVMa-curO2R2fJNQALwB2tQ", help=None, type="secondary", icon="🎥", disabled=False, use_container_width=True)

with warpBot:
    with st.container(border=True):
        st.page_link("https://discord.com/oauth2/authorize?client_id=1288167324586872842",label='**MetaPano**',icon="🦾")
        st.write("Ce bot discord vous renseigne sur les meilleurs stuff pvp du moment🤩")
        st.link_button("Ajoute le sur discord 🦿", "https://discord.com/oauth2/authorize?client_id=1288167324586872842", help=None, type="secondary", icon="🦾", disabled=False, use_container_width=True)


warp_bliblio,metapano, vide2 = st.columns((1,1,1))
with warp_bliblio:
    with st.container(border=True):    
        st.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio de Warp**',icon="📚", use_container_width=True)
        st.write("Tu peux y retrouver plus de 500 stuffs faits mains !")
        st.link_button("C'est par ici les stuffs!", "https://d-bk.net/fr/tl/11eJ", help=None, type="secondary", icon="🥋", disabled=False, use_container_width=True)
with metapano:
    with st.container(border=True):    
        st.page_link("https://d-bk.net/fr/tl/4BAS",label='**Biblio MetaPano 🤖**',icon="📚", use_container_width=True)
        st.write("Une sélection des meilleurs stuff méta du moment !")
        st.link_button("C'est par ici les stuffs!", "https://d-bk.net/fr/tl/4BAS", help=None, type="secondary", icon="🥋", disabled=False, use_container_width=True)
with vide2:
    with st.container(border=True):
        pass