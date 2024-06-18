import requests

g = requests.get(
    "http://127.0.0.1:8000"
)
print(f"Status Code: {g.status_code}")
print(f"Result: {g.json().get('message')}")
print("\n")

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

r = requests.post(
    "http://127.0.0.1:8000/inference",
    json=data,
)

# Print the status code with format
print(f"Status code: {r.status_code}")

# Print the result
try:
    print(f"Result: {r.json().get('result')}")

except requests.exceptions.JSONDecodeError:
    print("Error decoding JSON response")
    print(r.text)
