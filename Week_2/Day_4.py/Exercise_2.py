

# # Exercise 2: Working with JSON
# Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.
# Access the nested “salary” key.
# Add a new key “birth_date” wich value is of format “YYYY-MM-DD”, to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Save the modified JSON to a file.

import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)
print(f"Full dict: {data}")

salary = data['company']['employee']['payable']['salary']
print("Salary:", salary)

data['company']['employee']['birth_date'] = "1990-05-15"
print(f"Full modified dict: {data}")

with open("employee.json", "w") as f:
  json.dump(data, f, indent=2)
print("Modified data saved to employee.json")

with open("employee.json", "r") as f:
  verified = json.load(f)

print(f"Loaded file dictionary: {verified}")