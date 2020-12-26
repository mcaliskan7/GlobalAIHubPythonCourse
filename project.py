student_list = ["Nikola Tesla","Albert Einstein","James Clerk Maxwell","Max Planck"]
courses = ["Mathematics","Physics","Python Programming","Algorithms","Deutsch"]

def letter_grade():
    
    courses_input = input("\nWhich courses do you take (Enter by comma without blank): ")
    course_list = list(courses_input.split(","))
    
    if len(course_list) >= 3 and len(course_list) <= 5:
        
        for i in course_list:
            if i not in courses:
                return print("There is no course called",i,"in your class.")
        
        course = input("Enter one of the courses you take to see your letter grade: ")
        
        if course in course_list:
            
            grades = {"midterm":0,"final":0,"project":0}
            
            midterm = int(input("\nEnter your midterm grade: "))
            grades["midterm"] = midterm
            final = int(input("Enter your final grade: "))
            grades["final"] = final
            project = int(input("Enter your project grade: "))
            grades["project"] = project
            
            grade = (midterm*30 + final*50 + project*20)/100
            
            if grade >= 90:
                return print("\nYour letter grade is AA.")
            elif grade >= 70 and grade < 90:
                return print("\nYour letter grade is BB.")
            elif grade >= 50 and grade < 70:
                return print("\nYour letter grade is CC.")
            elif grade >= 30 and grade < 50:
                return print("\nYour letter grade is DD.")
            else:
                return print("\nYour letter grade is FF. You failed this course.")
        
        elif course not in course_list and course in courses:
            return print("\nYou didn't take this course.")
        
        else:
            return print("\nThere is no course called",course,"in your class.")
        
    else:
        return print("\nYou must take a minimum of 3 and maximum of 5 courses. You failed in class.")


for i in range(4):
    
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    
    student_info = name + " " + surname
    
    if student_info in student_list:
        
        print("\n",student_info,",","Welcome to the Student Managent System!")
        letter_grade()
        break
    
    elif i <= 2:
        
        print("Login failed. Try again.\n")
    
    else:
        
        print("Please try again later.")
