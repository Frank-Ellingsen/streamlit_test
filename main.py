import streamlit as st
import os
import pandas as pd

st.title("Streamlit 2025")
st.header("Welcome to the future of Streamlit!")


df=pd.DataFrame({
    "Column 1": [1, 2, 3],
    "Column 2": [4, 5, 6],
    "Column 3": [7, 8, 9]
})    

st.dataframe(df)


st.data_editor(df)




st.subheader("This is a subheader for Streamlit 2025")
st.markdown("## Markdown Example")
st.markdown("This is a **bold** text and this is *italic* text.")
st.caption("This is a caption for the Streamlit app.")

st.divider()
st.write("Hello, Streamlit 2025 world!!!!")

st.write(123)

3+4

print("Hello, Streamlit!")
pressed = st.button("Click me")
print(pressed)

st.image(os.path.join(os.getcwd(),"static", "profil.png"),)


