import streamlit as st


image_path='images/'
st.set_page_config(page_title="CalcOfus",layout="wide")
st.sidebar.image(image_path+"logo_persofus.png" )

st.title("Pages perso")

player_name = st.text_input("Nom de compte (format nom#1234)")
#une fois le nom entré, on peut cliquer sur un bouton pour générer le lien vers la page perso, c'est https://account.ankama.com/fr/profil-ankama/nom-1234
if player_name:
    if st.button("Générer le lien"):
        if "#" in player_name:
            nom, num = player_name.split("#", 1)
            url = f"https://account.ankama.com/fr/profil-ankama/{nom}-{num}"
            st.markdown(f"[Voir la page perso]({url})", unsafe_allow_html=True)
        else:
            st.error("Le format doit être nom#1234")

