# front end of the project
import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="wide")


def main():
    st.title("Weather Forecast for the Next Days")
# front end of the project the user interface
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
# backend to bring data from api to the web app
    # adding a block so user dont get an error for not having place filled out
    if place:
        # adding a line graph
        filter_data = get_data(place, days)

        if view == "Temperature":
            # temp plot
            temperatures = [dict["main"]["temp"] for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures"})
            st.plotly_chart(figure)

        if view == "Sky":
            # sky data
            conditions = {"Clear":"sky_imgs/clear.png",
                          "Clouds":"sky_imgs/cloud.png",
                          "Rain":"sky_imgs/rain.png",
                          "Snow":"sky_imgs/snow.png"}
            sky_conditions = [dict["weather"][0]['main'] for dict in filter_data]
            img_pathdata = [conditions[condition] for condition in sky_conditions]

            st.image(img_pathdata, width=115)

if __name__ == '__main__':
    main()
