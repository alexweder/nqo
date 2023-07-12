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

form, authentication_status, username = authenticator.login('Login','main')






