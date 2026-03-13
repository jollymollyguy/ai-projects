# Block 1: Variables + Data Types

# VARIABLES AND DATA TYPES
name="jollymollyguy"
age = 20
country = "Nepal"
is_learning = True
monthly_target = 10000

print (name)
print (age)
print (is_learning)
print (monthly_target)

# STRING FORMATTING
print(f"my name is {name}. I am {age} years old.")
print (f"Monthly income target: {monthly_target}")

# BASIC MATH
hourly_rate = 25
hours_worked = 10
total_earned = hourly_rate * hours_worked
print(f"Total earned:${total_earned}")


# Block 2: Lists + Dictionaries

# LISTS
SKILLS = ["Python", "n8n", "Anthropic Claude", "Prompt_Engineering"]
print(SKILLS)
print(SKILLS[0])
print(SKILLS[-1])
print(len(SKILLS)) 

SKILLS.append("Next.js")
print(SKILLS)

# LOOP THROUGH LIST
for SKILL in SKILLS:
    print (f"SKILL: {SKILL}")

# DICTIONARIES
client = {
    "name":"Bishesh",
    "industry":"tourism",
    "budget":300,
    "paid": False
}

print(client["name"])
print(client["budget"])

client["paid"] = True
print(client)

# LOOP THROUGH DICTIONARY
for key, value in client.items():
    print(f"{key}:{value}")


# Block 3: Functions

# BASIC FUNCTION
def greet_client(name, industry):
    return f"Hello {name}, I can build AI tools for your {industry} business"

message = greet_client("Himalayan Treks", "Trekking")
print (message)

# FUNCTION WITH CALCULATION
def calculate_project_price(hours, rate=25):
    total= hours*rate
    return f"Project price: ${total}"

print(calculate_project_price(10))
print(calculate_project_price(20, 35))

# FUNCTION WITH LIST
def list_services(services):
    print("my services:")
    for i, service in enumerate(services, 1):
        print(F"{i}.{service}")

my_services = [
    "AI Chatbots",
    "Whatsapp Automation",
    "Itinerary Generator",
    "Email Responder"
]

list_services(my_services)


# Block 4: File I/O

# WRITE TO FILE
with open("clients.txt", "w") as f:
    f.write("Himalayan Treks\n")
    f.write("Pokhara Adventures\n")
    f.write("Everest Tours\n")

print("File written.")

# READ FROM FILE
with open("clients.txt", "r") as f:
    contents = f.read()
    print(contents)

# READ LINE BY LINE
with open("clients.txt", "r") as f:
    for line in f:
        print(f"Clients:{line.strip()}")

# APPEND TO FILE
with open("clients.txt", "a") as f:
    f.write("Annapurna Expeditions\n")

# VERIFY APPEND WORKED
with open("clients.txt", "r") as f:
    print(f.read())


# Block 5: Error Handling

# BASIC ERROR HANDLING
def divide(a, b):
    try:
        result= a / b
        return result 
    except ZeroDivisionError:
        return "Error: cannot divide by zero."

print(divide(10, 2))
print(divide(10, 0))

# FILE ERROR HANDLING
try:
    with open("nonexistent_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found. Check the filename.")

# USER INPUT VALIDATION
def get_project_budget(amount):
    try:
        budget = float(amount)
        if budget <= 0:
            return "Budget must be greater than zero"
        return f"Project Budget Set: ${budget}"
    except ValueError:
        return "Error: Please enter a valid number."

print(get_project_budget("300"))
print(get_project_budget("abc"))
print(get_project_budget("-50"))