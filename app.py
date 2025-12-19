from dash import Dash , dcc, callback, Input, Output
import pandas as pd 
import plotly.express as px


# Exercise:
# add a checkbox to show all years. 

# CONSTANTS 
URL = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2016-weather-data-seattle.csv"

MEANS_FILE = "data/mean_temps_1948-2016.csv"

# instantiate the app 
app = Dash(title="2016 Seattle Weather App")

# DATA 
weather_df = pd.read_csv(URL)
yearly_means_df = pd.read_csv(MEANS_FILE)

# HELPERS

# convert date to datetime
weather_df['Date'] = pd.to_datetime(weather_df['Date']) 

# COMPONENTS 
dd1 = dcc.Dropdown(
    yearly_means_df['Year'], 
    [2001], 
    id='dd-1', 
    multi=True)


options=[
       {'label': 'Show All', 'value': 'all'}
   ]

cb1 = dcc.Checklist(options, 
                     inline=True, 
                     id="cb-1")

graph1 = dcc.Graph(id="histo1")

# LAYOUT
app.layout = [
    dd1,
    cb1,
    graph1
]

@callback(
    Output('histo1','figure'),
    Input('dd-1','value'), 
    Input('cb-1', 'value')
)
def update_barchart(years_, cbs_):

    # DEBUG: print("Years:", years_) 

    # empty df
    filtered_df = pd.DataFrame()

    # if nothing is selected, filter by dropdown
    if not cbs_: 
        # filter the dataframe by years 
        filter_ = yearly_means_df.Year.isin(years_) 
        filtered_df = yearly_means_df[filter_]
    elif "all" in cbs_:
        filtered_df = yearly_means_df
    
    # return a new graphic 
    return px.bar( filtered_df, x='Year', y='Mean_TemperatureC')

if __name__ == '__main__':
    app.run(debug=True)