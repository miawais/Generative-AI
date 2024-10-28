import sqlite3
import csv

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("employee.db")

# Create a cursor object
cursor = connection.cursor()

# Create the table if it doesn't already exist
table_info = """
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    Education VARCHAR(50),
    JoiningYear INT,
    City VARCHAR(50),
    PaymentTier VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    EverBenched VARCHAR(10),
    ExperienceInCurrentDomain INT,
    LeaveOrNot VARCHAR(10)
)
"""
cursor.execute(table_info)

# Load data from the CSV file
csv_file_path = "Employee.csv"  # Replace with the path to your CSV file

with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)  # Use DictReader to access columns by name
    for row in csv_reader:
        # Extract data from the row
        education = row['Education']
        joining_year = int(row['JoiningYear'])  # Convert to integer
        city = row['City']
        payment_tier = row['PaymentTier']
        age = int(row['Age'])  # Convert to integer
        gender = row['Gender']
        ever_benched = row['EverBenched']
        experience_in_current_domain = int(row['ExperienceInCurrentDomain'])  # Convert to integer
        leave_or_not = row['LeaveOrNot']

        # Insert each row of CSV data into the EMPLOYEE table
        cursor.execute('INSERT INTO EMPLOYEE (Education, JoiningYear, City, PaymentTier, Age, Gender, EverBenched, ExperienceInCurrentDomain, LeaveOrNot) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (education, joining_year, city, payment_tier, age, gender, ever_benched, experience_in_current_domain, leave_or_not))

# Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM EMPLOYEE")
for row in data:
    print(row)

# Commit changes and close the database connection
connection.commit()
connection.close()
