import mysql.connector

# Storing the Database credentials in a variable
# which we will use to connect to the Database

sqlConnection = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

# Creating the cursor object to navigate through the Database

cursor = sqlConnection.cursor()

word = input("Enter a word: ")

# Executing a Database Query:

# Dictionary is the name of the Database table

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)

# Storing the results of the query in the variable

results = cursor.fetchall()

if results:
    for x in results:
        print(x[1])
else:
    print("No words found!")
