import sqlite3

con = sqlite3.connect("catalog.db")
db = con.cursor()

with open("./CourseCatalog/t.txt", "r", encoding="utf-8") as courses:
    text = courses.read()
    text = text.split("\n")
    # print(text)

    statements = ["1 - Skip", "2 - 1 credit", "3 - Description", "4 - Subject", "5 - Name", "6 - is AP?", "7 - Prequisite", "8 - Grades?", "9 - End of Course"]
    count = 0
    while True:
        item = text[count]
        course = {
            "credit": None,
            "description": "",
            "subject": None,
            "name": None,
            "isAP": False,
            "grades": None,
            "prerequisite": None
        }
        if item.strip() != "":
            for t in statements:
                print(t)
            print("\n\n")
            print(item)
            answer = input("Input >>> ")
            if answer == "2":
                course.update({"credit": item.strip()})
            elif answer == "3":
                course.update({"description": course['description'] + " " + item.strip()})
            elif answer == "4":
                course.update({"subject": item.strip()})
            elif answer == "5":
                course.update({"name": item.strip()})
            elif answer == "6":
                course.update({"isAP": True})
            elif answer == "7":
                course.update({"prerequisite": item.strip()})
            elif answer == "8":
                grades = input("What Grades?")
                course.update({"grades": grades.strip()})          
            elif answer == "9":
                db.execute("INSERT INTO courses (name, description, credit, isAP, grades, prerequisite) VALUES (?, ?, ?, ?, ?, ?)",
                (course['name'], course['description'], course['credit'], course['isAP'], course["grades"], course['prerequisite']))
                con.commit()
            elif answer == "1":
                pass
            
            elif answer == "0":
                count -= 2
            
            elif answer == "":
                count += 1
            else:
                print("Try Again")

            

