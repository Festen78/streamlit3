import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()
def accueil():
  
      st.title("Bienvenu sur ma page !!")
      st.markdown(
          """
          <div style="text-align: center;">
              <img src="https://media.tenor.com/NabW5Fd7IgsAAAAM/clapping-leonardo-dicaprio.gif" width="300">
          </div>
          """,
          unsafe_allow_html=True
      )

def chat():  
      st.write("😺 Les photos de mon chat")
      col1, col2, col3 = st.columns(3)

      with col1:
        st.image("https://www.animaniacs.fr/wp-content/uploads/2013/08/catgriffe.gif")

      with col2:
        st.image("https://lh4.googleusercontent.com/proxy/TFuPxmdbI09yHDwTH2tXOqPHY4eTAgfYt43xsvpz3_Vf5pB0K24hxedn2nmGI0r1-PPW60Cc5NWRdOWLsDyEOw5H3F0MA0fSTQ")

      with col3:
        st.image("https://i.gifer.com/Ysvq.gif")
      
      
if st.session_state["authentication_status"]:
  with st.sidebar:
      authenticator.logout("Déconnexion")
      st.markdown(f"Bienvenue, *{st.session_state.get('username')}* !")
      
      selection = option_menu(
          menu_title=None,
          options = ["🤩 Accueil", "😺 Les photos de mon chat"]
      )

  if selection == "🤩 Accueil":
    accueil()
  elif selection == "😺 Les photos de mon chat":
    chat()
    
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
    

    
