import json

# Task 1 — Build a JSON Structure
# Create a Python dictionary representing a user profile with the following fields: name, age, email, is_active, and a list of skills. Convert it to a JSON string using json.dumps() and print it with proper indentation

user_profile={
"name":"Joe", "age":15, "email":"Joe@gmail.com", "is_active":True,
"skills":['C','C++','Python']
}

json_user_profile=json.dumps(user_profile)
print(json_user_profile)

# Task 2 — Parse an API Response
# You receive the following mock API response as a JSON string:

json_string_task2={ "status": "success", 
                    "data": {"user_id": 101, 
                             "username": "alex99", 
                             "score": 87.5
                            }
                }

print(f"The {json_string_task2['data']['username']}")
print(f"The {json_string_task2['data']['score']}")
print(f"User {json_string_task2['data']['username']} scored {json_string_task2['data']['score']} points")

# Task 3 — Handle Nested JSON
# Given the nested JSON below, extract and print the city and zip code of the user:

json_string={
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}

json_string['address']["country"]="India"
print(json_string)
