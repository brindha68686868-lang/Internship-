import json

# Sample JSON data (string format)
json_data = '''
{
    "name": "Brindha",
    "age": 18,
    "city": "Salem",
    "skills": ["Python", "HTML", "CSS"]
}
'''

# Convert JSON string to Python dictionary
data = json.loads(json_data)

# Access values
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])
print("Skills:", ", ".join(data["skills"]))

# Add new data
data["email"] = "brindha@example.com"

# Convert dictionary back to JSON
updated_json = json.dumps(data, indent=4)

print("\nUpdated JSON:")
print(updated_json)