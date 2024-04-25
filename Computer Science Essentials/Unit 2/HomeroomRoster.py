#Homeroom roster program
#This program is designed to allow a teacher to:
#1) See students in homeroom 2) add/remove students to/from homeroom
#3) See basic info about students

#create an object called Student
class Student:
    def __init__(self, name, grade, ID, address, age, locker_number):
        self.name = name
        self.grade = grade
        self.ID = ID
        self.address = address
        self.age = age
        self.locker_numebr = locker_number

list_of_homeroom_students = []

#Funtions
def add_to_homeroom():
    #create a new student object with the following properties:
    #name, grade, ID, address, age, locker_number
   
    #name
    print("creating new student")
    print("what is their name?")
    name = input("->")

    #grade
    print("what is their grade?")
    grade = input("->")

    #ID
    print("what is their ID number?")
    ID_number = input("->")

    #adress
    print("what is their address")
    address  = input("->")

    #age
    print("what is their age?")
    age  = input("->")
    
    #locker number
    print("what is their locker number?")
    locker_number  = input("->")
   
   #Create the student object using the variables created above
   #name, grade, ID, address, age, locker_number
    baked_potato = Student(name, grade, ID_number, address, age, locker_number)
    list_of_homeroom_students.append(baked_potato)
    print("created a student with the details below")
    print("Name:", baked_potato.name)
    print("grade:", baked_potato.grade)
    print("ID:", baked_potato.ID)
    print("Address:", baked_potato.address)
    print("Age:", baked_potato.age)
    print("Locker Number:", baked_potato.locker_number)


def get_number_of_students():
    number = len(list_of_homeroom_students)
    return number
def search_list_for_student(search_name):
    for counter in list_of_homeroom_students:
        if search_name == counter.name:
            print("This student is on the list")
            return
    print("This student is not on the list")
def get_student_address():
    print("Searching list for student's address")
    for counter in list_of_homeroom_students:
        if counter.name == search_name:
            print(counter.address)
def get_student_basic_info():
    print("getting information about this student")
    for counter in list_of_homeroom_students:
        if counter.name == search_name:
            print("Grade: ",counter.grade)
            print("ID: ",counter.ID)
            print("Address: ",get_student_address(search_name))
            print("Age: ",counter.age)
            print("Locker Number: ",counter.locker_number)
def list_homeroom_students():
    print("Now showing the list of homeroom students")
    for counter in list_of_homeroom_students:
        print(counter.name)

#MAIN CODE
while True:
    print("What would you like to do:")
    print("1: View Homeroom Roster")
    print("2: Add student to homeroom")
    print("3: Remove student from homeroom")
    print("4: Get student ID number")
    print("5: See number of students in Homeroom")
    print("6: See basic student imformation (address, ID, Grade, Age, locker numeber)")
    print("7: See if a student is on the homeroom list")
    print("8: Exit Program")
    try:
        choice = int(input ("->"))
        print("You selected option", choice)
        if choice == 1:
           #see list of students
            list_homeroom_students()
        elif choice == 2:
            #add students to homeroom
            add_to_homeroom()
        elif choice == 3:
            #remove students from homeroom
            pass
        elif choice == 4:
            #get student ID
            pass
        elif choice == 5:
            #get number of students
            print("Getting number of homeroom students")
            print(get_number_of_students())
        elif choice == 6:
            #see basic info about a student
            pass
        elif choice == 7:
            #search the roster to see if a student is on it
            print("What student do you want to search")
            search_name = input("->")
            search_list_for_student(search_name)
        elif choice == 8:
            #exit program
            break
        else:
            print("An error has occured")
    except: 
        print("Please use a valid number")

print("Thanks for using the homeroom software")
 