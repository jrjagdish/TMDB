import json

def display_data(store):
    #data = json.loads(store)
    if store:
       # for movie in data["results"]:
        #   print(f"titles={movie['title']}")
       print(store) 
    else:
        print("no data")       