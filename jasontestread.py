import json

# Dictionary of states and capitals
states_and_capitals = {
  "Andhra Pradesh": "Amaravati",
  "Arunachal Pradesh": "Itanagar",
  "Bihar": "Patna",
  "Goa": "Panaji",
  "Gujarat": "Gandhinagar",
  "Haryana": "Chandigarh",
  "Kerala": "Thiruvananthapuram"
}

# Open a file for writing
with open("jasontest.json", "w") as f:
  # Write the dictionary to the file in JSON format
  json.dump(states_and_capitals, f)

f = open(r"jasontest.json", "r")
print(f.read())

