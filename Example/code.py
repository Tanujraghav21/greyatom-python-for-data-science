# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Cornia Cortes']
# Concatenate both the strings
new_class = (class_1 + class_2)
print(new_class)
# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses = {'math':65,'English':70,'History':80,'French':70,'Science':60}




# Slice the dict and stores  the all subjects marks in variable




# Store the all the subject in one variable `Total`
V_1 = courses.values()
total = sum(V_1)

# Print the total
print(total)
# Insert percentage formula
percentage =(total/500)*100
# Print the percentage

print(percentage)



# Create the Dictionary
 
mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua bengio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}


# Given string
topper = max(mathematics,key = mathematics.get)
print(topper)

# Create variable first_name 
first_name = topper.split()[0]
print(first_name)
# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]
print(last_name)
# Concatenate the string
full_name = last_name +" "+ first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


