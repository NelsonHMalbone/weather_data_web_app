import streamlit as st

st.set_page_config(layout="wide")
def main():
    st.title("Weather Forecast for the Next 1- 5 Days")
    st.text('Place:')
    st.text_input("")
    st.text("Forecast Days:")
    st.slider("", min_value=0, max_value=5)
    st.text("Select Data to view")
    st.selectbox("", ["Temperature", "Sky"])
    st.title("Temperature for the next '#' days in 'City' ")

if __name__ == '__main__':
    main()
