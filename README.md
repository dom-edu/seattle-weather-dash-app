# Install 
```
pip install -r requirements.txt
```
# Generate means.csv file  
```
weather_df['Year'] = weather_df.Date.dt.year
yearly_means_df = weather_df.groupby('Year')['Mean_TemperatureC'].mean()
yearly_means_df.to_csv('yearly_means.csv)
```