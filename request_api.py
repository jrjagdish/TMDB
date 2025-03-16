import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()


#get url of TMDB
def get_by_key(categorey):
    
#url = http
   API_KEY = os.getenv("API_KEY")
   url = f"https://api.themoviedb.org/3/movie/{categorey}?api_key={API_KEY}"
   
   
   response = requests.get(url)
   print(response)
   if response.status_code == 404:
      
      return "Error:unable to connect to the server"
   
     
   if response.status_code == 200:
      data = response.json()
      json_data =json.dumps(data,indent=4)
      return json_data
        
   
   


