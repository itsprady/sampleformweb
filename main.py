import streamlit as st

name=st.text_input("ENTER YOUR NAME: ")
fname=st.text_input("ENTER YOUR FATHER NAME: ")
address=st.text_area("ENTER YOUR ADDRESS: ")
classdata = st.selectbox("ENTER YOUR CLASS:",("CHOOSE YOUR CLASS",1,2,3,4,5,6,7,8,9,10))
button = st.button("DONE")
if button :
    st.markdown(
        f"""
        NAME : {name}
        FATHER NAME : {fname}
        ADDRESS : {address}
        CLASS : {classdata}

        """
    )