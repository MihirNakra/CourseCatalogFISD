with open("./CourseCatalog/courses.txt", "r", encoding="utf-8") as f:
    text = f.read()
    text.replace("Frisco ISD Academic Guide & Course Catalog Revised  06/24/2021  RETURN TO TABLE OF CONTENTS ", "")
    text.replace("", "")
    temp = text.split("\n")
    count = 1
    removes = []
    for i in range(len(temp)):
        item = temp[i]
        try:
            temp2 = int(item.strip())
            removes.append(item.strip())
        except:
            if item.strip().startswith("Frisco"):
                removes.append(item.strip())
        
        temp[i] = temp[i].strip()
    
    for item in removes:
        temp.remove(item)
    

    while True:
        try:
            temp.remove("")
        except:
            break
    
    
    t = ""
    for item in temp:
        t += item + "\n"


with open("courses_lemmatized.txt", "w", encoding="utf-8") as f:
    f.write(t)

