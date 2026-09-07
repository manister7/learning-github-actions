import requests
import json
response = requests.get("http://api.open-notify.org/astros.json")

#=output = response.json()

pretty_json = json.dumps(output, indent=5)

list_of_people = output.get("people")

def list_people():
    print(f"the people current in space are:")
    for people in list_of_people:
        print(people.get("name"))

list_people()