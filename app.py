from dash import Dash , dcc
import pandas as pd 

# CONSTANTS 
URL = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2016-weather-data-seattle.csv"


# instantiate the app 
app = Dash(title="2016 Seattle Weather App")


# DATA 
weather_df = pd.read_csv(URL)


# HELPERS




# convert date to datetime
weather_df['Date'] = pd.to_datetime(weather_df['Date']) 
# add year column using dt.year on Date col 
weather_df['Year'] = weather_df.Date.dt.year 

# COMPONENTS 
dd1 = dcc.Dropdown(
    weather_df['Year'].unique(), 
    2001, 
    id='dd-1', 
    multi=True)

graph1 = dcc.Graph(id="histo1")

# LAYOUT
app.layout = [
    dd1,
    graph1
]


if __name__ == '__main__':
    app.run()