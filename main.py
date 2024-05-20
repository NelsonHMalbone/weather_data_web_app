# front end of the project
import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="wide")


def main():
    st.title("Weather Forecast for the Next Days")

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

    # adding a line graph
    data = get_data(place, days, view)
    d, t = get_data(days)

    figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperatures"})
    st.plotly_chart(figure)


if __name__ == '__main__':
    main()
