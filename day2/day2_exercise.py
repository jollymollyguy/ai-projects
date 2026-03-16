# 1. Create a list of 5 Nepali cities. Print only the first and last one.

nepali_cities = [
    "Kathmandu", "Dhangadhi", "Pokhara", "Bhaktapur", "Nepalgunj"
]
print(nepali_cities[0])
print(nepali_cities[-1])


# 2. Create a dictionary for a freelance project with keys: client, price, delivered. Print each key-value pair using a loop.

project = {
    "client" : "Rajesh",
    "price" : 200,
    "delivered" : True
}

for key, value in project.items():
    print(f"{key}:{value}")


# 3. Write a function that takes a number and returns whether it's positive, negative, or zero.

def check_number(num):
    if num>0:
        return  "Positive"
    elif num<0:
        return "Negative"     
    else:  
        return "Zero"

print (check_number(-2))
print (check_number(45))
print (check_number(0))


# 4. Write to a file called notes.txt with 3 lines of text. Read it back and print it.

with open("notes.txt", "w") as f:
    f.write("Rabin\n")
    f.write("Rajesh\n")
    f.write("Nabin\n")

with open("notes.txt","r") as f:
    name=f.readlines()

name.reverse()

for names in name:
    print(names.strip())


# 5. Write a function that divides two numbers with error handling for zero division and non-number inputs.

def num_divide(num1,num2):
    try:
        a= float(num1)
        b= float(num2)
        result = a/b
        return result
    except ValueError: return "Error: Non-number input."
    except ZeroDivisionError: return "Error: Cannot divide by zero."

print(num_divide(4,2))
print(num_divide(4,0))
print(num_divide(5,"abc"))