
import streamlit as st
import streamlit_authenticator as stauth
import app as ap


def autentificador ():

     names = ['Administrador','Stefany Campana']
     usernames =['admin','scampana']
     passwords =['123','456']

     hashed_passwords = stauth.Hasher(passwords).generate()

     authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name',
     'some_signature_key', cookie_expiry_days=30)

     name, authentication_status, username = authenticator.login('Login','main')

     if authentication_status:
        authenticator.logout('Logout','main')
        st.write('Welcome *%s*' % (name))
        ap.dashboard()
     elif authentication_status == False:
        st.error('Username/password is incorrect')
     elif authentication_status == None:
        st.warning ('Please enter your username and password')

    



