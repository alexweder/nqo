import streamlit_authenticator as stauth
from pathlib import Path

hashed_passwords = stauth.Hasher(['123']).generate()

print(hashed_passwords)

f= open("tpm.txt","a")
print (hashed_passwords, file=f)
f.close()

