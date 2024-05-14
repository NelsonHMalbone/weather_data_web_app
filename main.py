import streamlit as st

st.set_page_config(layout="wide")
def main():
    st.title("Weather Forecast for the Next 1- 5 Days")

    # text input to Enter Location
    place = st.text_input("Place: ", key='location')

    # Slider for amount of days to see
    days = st.slider("Forecast Days: ",
                       min_value=1,
                       max_value=5,
                       help="Select the number of forecasted days", key="projected")

    # drop down to view plot graph or sky_view using a tuple
    view = st.selectbox("Select data to view",
                        ("Temperature", "Sky"))

    # output
    st.subheader(f"{view} for the next {days} days in {place.title()} ")


if __name__ == '__main__':
    main()
