import json

# ── Block 1: JSON ──────────────────────────────────────────

# PYTHON DICT → JSON STRING
client = {
    "name": "Himalayan Treks",
    "industry": "trekking",
    "budget": 300,
    "paid": True
}

json_string = json.dumps(client)
print("Dict → JSON String:")
print(json_string)
print(type(json_string))

# JSON STRING → PYTHON DICT
json_data = '{"name": "Pokhara Adventures", "budget": 500, "paid": false}'
python_dict = json.loads(json_data)
print("\nJSON String → Dict:")
print(python_dict)
print(type(python_dict))
print(python_dict["name"])

# WRITE JSON TO FILE
with open("client_data.json", "w") as f:
    json.dump(client, f, indent=4)
print("\nJSON file written.")

# READ JSON FROM FILE
with open("client_data.json", "r") as f:
    loaded = json.load(f)
print("JSON file loaded:")
print(loaded)
print(loaded["industry"])