import requests
import pandas as pd   # For creating a DataFrame so  that we can store our data as CSV
import os 
from dotenv import load_dotenv

load_dotenv()    # Env file ko laod kr rhe hain yeha par 

url = "https://api.ipstack.com/check"
access_key = os.getenv("IPSTACK_ACCESSKEY")
response = requests.get(
    url,
    params={
        "access_key":access_key
        
        }
)

if response.status_code==200:
    data = response.json()

    region_name = data['region_name']
    city = data['city']
    zip = data['zip']
    capital = data['location']['capital']
    language = data['location']['languages'][1]

    df = pd.DataFrame([{
        "region_name": region_name,
        "city":city,
        "zip":zip,
        "capital":capital,
        "language":language
    }])

    df.to_csv("IpStack_data.csv", index=False)
    print("Your data has been saved successfully !!")