import sqlite3

FORBIDDEN = []


with open("./data_collection/courses_lemmatized.txt", "r", encoding="utf-8") as cfile:
    text = cfile.read().splitlines()
    name = ""
    pre = ""
    grades = ""
    description = ""
    isAp = "False"
    isPreAp = "False"
    credit = ""
    # print(text)
    subject = ""
    i = 0
    while i < len(text)-1:
            isAp = "False"
            isPreAp = "False"
            line = text[i]
        # if "credit)" in line:
            a = i
            temp = ""
            while a >= 0 or "." not in text[a]:
                temp = text[a]
                a -= 1

            if temp != "":
                subject = temp

            if "1/2 credit" in line:
                credit = "1/2"

            elif "1 credit" in line:
                credit = "1"
            
            elif "2 credits" in line:
                credit = "2"
            
            elif "3 credits" in line:
                credit = "3"
            
            elif "no credit" in line:
                credit = "0"
            
            index = line.find("-")
            name = line[0:index].strip()
            if "–" in name:
                index = line.find("–")
                name = line[0:index].strip()

            if "Advanced" in name:
                isPreAp = "True"
            
            elif "AP " in name:
                isAp = "True"
        
            i += 1

            line = text[i]
            pre = ""
            if "Prerequisite" in line:
                pre = line[line.find(":") + 1:].strip()
                grades = "9,10,11,12"
            
            else:
                if line == "11th –12th grade" or "11th – 12th grade":
                    grades = "11,12"

                elif line == "10th –12th grade" or "10th – 12th grade":
                    grades = "10,11,12"
                
                elif line == "9th –12th grade" or "9th - 12th Grade":
                    grades = "9,10,11,12"
                
                else:
                    grades = "12"
                        
            i += 1
            line = [i]
            if "Prerequisite" in line:
                pre = line[line.find(":") + 1:].strip()
            
  
            
            if pre == "":
                pre = "None"
            

            
            while i < len(text) and "credit)" not in text[i] and "credits)" not in text[i]:
                if "Prerequisite:" not in text[i]:
                    description += text[i] + " "
                i += 1
            


            con = sqlite3.connect("catalog.db")
            db = con.cursor()
            db.execute("INSERT INTO courses (name, description, credit, isAP, grades, prerequisite, isPreAp) \
                VALUES(?, ?, ?, ?, ?, ?, ?)", (name, description, credit, isAp, grades, pre, isPreAp))
            
            con.commit()

            print(description + "\n\n")
            description = ""

        
        
        
        
            
            




                

