import csv
from faker import Faker
import re

fake = Faker()

users = []

# Create user data
for i in range(200):
    full_name = fake.name()
    first_name = full_name.split()[0].lower()  # Extracting the first name
    # Removing any non-alphanumeric characters from the first name
    first_name = re.sub(r'[^a-zA-Z0-9]', '', first_name)
    username = first_name + str(i).zfill(3)  # Adding zero-padded numbers to ensure the same length
    email = first_name + str(i).zfill(3) + "@example.com"
    password = fake.password(length=15, special_chars=True, digits=True, upper_case=True, lower_case=True)
    # Increase roleId by 1 for each user
    user = {
        "fullName": full_name,
        "userName": username,
        "email": email,
        "password": password,
        "roleId": i
    }
    users.append(user)

# Define CSV headers
headers = ["fullName", "userName", "email", "password", "roleId"]

# Write data to CSV file
with open('users.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    
    # Write headers
    writer.writeheader()
    
    # Write user data
    writer.writerows(users)
