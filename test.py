import mysql.connector
import sys
import os

debugMode = False
host = 'localhost'
user = 'root'
password = 'toor'
database = 'capstone'

def insertFaculty(facultyName, designation, yearsOfExperience: int, areasOfInterest, domain, acceptableGroups: int):
    try:
        connection = mysql.connector.connect(host = host, database = database, user = user, password = password)

        cursor = connection.cursor()

        # args = ("Achal MAAMA", "Assistant Professor", 4, "SpaSe", "NiCE", 3, 0)
        args = (facultyName, designation, yearsOfExperience,areasOfInterest, domain, acceptableGroups, 0)

        result = cursor.callproc("InsertFaculty", args)

        connection.commit()
        connection.close()

        if debugMode:
            print(result)

        return result[6]
    except Exception as e:
        print(f"[-ERROR]: {e}")

def removeFaculty(column, data):
    acceptableColumns = ["name", "designation", "yearsofexperience", "areasofinterest", "domain", "acceptablegrps", "fid"]
    try:
        connection = mysql.connector.connect(host = host, database = database, user = user, password = password)

        cursor = connection.cursor()

        # query = "delete from faculty where name = 'Achal MAAMA'"
        if column.lower() in acceptableColumns:
            query = f"delete from faculty where {column} = '{data}'"

            result = cursor.execute(query)
            if debugMode:
                print(result)
                print(cursor.rowcount)
            connection.commit()
            connection.close()
            return cursor.rowcount
        else:
            print(f"Column {column} is not acceptable")

    except Exception as e:
        print(f"[-ERROR]: {e}")


if __name__ == '__main__':

    args = sys.argv

    if "--debug" in args:
        debugMode = True

    while True:

        print("\n\n")

        print("Capstone Database Managaement")
        print("Choose option: ")
        print("1) Insert Faculty")
        print("2) Delete a Faculty")
        print("99) Exit")
        choice = input("=> ")

        os.system("cls")

        if choice == "1":

            facultyName = input("Enter the faculty name: ")
            designation = input(f"Enter {facultyName}'s Designation: ")
            yearsOfExperience = input("Enter years of experience (integer): ")
            try:
                yearsOfExperience = int(yearsOfExperience)
            except:
                print(f"Please enter only integer values, {yearsOfExperience} is not an integer")
                continue

            areasOfInterest = input(f"Enter {facultyName}'s Area of Interest: ")
            domain = input("Enter the domain: ")
            acceptableGroups = input(f"Enter the number of groups {facultyName} is accepting (Integer value): ")
            try:
                acceptableGroups = int(acceptableGroups)
            except:
                print("Please enter only integer values")
                continue

            result = insertFaculty(facultyName, designation, yearsOfExperience, areasOfInterest, domain, acceptableGroups)
            print()
            if result == -1:
                print("Insertion failed, faculty already exists")
            else:
                print("Faculty has been inserted")

        elif choice == "2":

            column = input("Enter the column to match: ")
            data = input("Enter the data to match the column with: ")


            result = removeFaculty(column, data)

            print(f"Query executed: {result} rows deleted")
        
        elif choice == "99":
            print("Bye")
            exit(0)
        
        else:
            print(f"Invalid choice: {choice}")


        