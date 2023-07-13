import streamlit as st
import streamlit_authenticator as stauth
import yaml
from pathlib import Path

from yaml.loader import SafeLoader

with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login('Login','main')

if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main', key='unique_key')
        st.write(f'Welcome {st.session_state["name"]}')
        st.title('Content')
elif st.session_state["authentication_status"] is False:
        st.error('Wrong Username/Password')
elif st.session_state["authentication_status"] is None:
        st.warning('Please enter Username/Password')

if authentication_status:
        try:
                if authenticator.reset_password(username, 'Reset Password'):
                        st.success('Password Modified')
        except Exception as e:
                st.error(e)
        
        try: 
                if authenticator.register_user('Register User', preauthorization=False):
                        st.sucess('User Registered')
        except Exception as e:
                st.error(e)

