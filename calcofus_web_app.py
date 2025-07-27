import streamlit as st
image_path='images/'

######################
# Pages
######################
pg = st.navigation([
    st.Page("page_accueil.py", title="Accueil", icon=":material/home:"),
    st.Page("page_invo.py", title="Invocations", icon=":material/cruelty_free:"),
    st.Page("page_bombes.py", title="Bombes", icon=":material/bomb:"),
    st.Page("page_sorts.py", title="Sorts", icon=":material/sword_rose:"),
    st.Page("page_dopou.py", title="Dopou", icon=":material/directions_alt:"),
    st.Page("page_taclefuite.py", title="Tacle/Fuite", icon=":material/do_not_step:"),
    st.Page("page_persofus.py", title="Pages perso", icon=":material/data_loss_prevention:"),
    st.Page("page_jda4.py", title="Stats JDA#4", icon=":material/bar_chart:"),
    st.Page("8_formulofus.py", title="Formules Dofus Touch", icon=":material/function:"),
    # st.Page(pages_path+"page_ret.py", title="Retrait PA/PM", icon=":material/star:"),
    # st.Page(pages_path+"page_steam.py", title="Tourelles Steamer", icon=":material/star:"),


])
pg.run()

