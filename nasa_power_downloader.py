#imports
import sqlite3

#variables and constants
Base_url='https://power.larc.nasa.gov/api/temporal/daily/point?'
parameters='ALLSKY_SFC_SW_DWN,T2M,RH2M,WS10M&community=RE&longitude=-3.7038&latitude=40.4168&start=20200101&end=20241231&format=CSV'

#trying out to get data from the API
def fetch_nasa_power_data():
    import requests
    url = Base_url + parameters
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        return data
    else:
        print("Error fetching data:", response.status_code)
        return None
data = fetch_nasa_power_data()
print(data)