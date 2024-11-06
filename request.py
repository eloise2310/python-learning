# MAKING A HTTP REQUEST 
# creating a programme that lists the current people in space

import requests 

# returns all the info about the people currently in space
response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()
print(json) 

# using a for loop - we can access specific data e.g. the name
print("The people currently in space are:")
for person in json["people"]:
    print(person["name"])
