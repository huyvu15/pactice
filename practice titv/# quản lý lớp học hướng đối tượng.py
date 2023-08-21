# quản lý lớp học hướng đối tượng
''' Question
Xây dựng 1 lớp biểu diễn các đối tượng khóa học. Trong đó mỗi khóa học
có các thông số: Tên khóa học, năm học, mã khóa học, giảng viên
'''
   
# tự code lại 1 chương trình đơn giản hơn sau khi học xong tính kế thừa
# và tính đa hình

# Define class Course
class Course:
    def __init__(self,name, year, id_number, lecturer):
        self.name = name
        self.year = year
        self.id_number = id_number
        self.lecturer = lecturer
        self.student_list = [] # do chưa có list student nên ở đây cta khởi tạo 1 list empty
    
    def print_student(self):
        print("----------Students in course " + self.name + "----------")
        for i in self.student_list:
            txt = "{:<16} {:<16} {:<6d} {:<16}"
            txt2 = "{:<16} {:<16} {:<6} {:<16}"
            print(txt2.format("First name", "Last name", "Age", "Email"))
            print(txt.format(i.first_name, i.last_name, i.age, i.email))
           
    def print_lecturer(self):
        print("\n\n\n----------Lecturer in course " + self.name + "----------")
        txt = "{:<16} {:<16d}"
        txt2 = "{:<16} {:<16}"
        print(txt2.format("Name", "Bank Account"))
        print(txt.format(self.lecturer.first_name, self.lecturer.bank_account)) 
    
    def enroll(self,student):
        self.student_list.append(student)



# áp dụng tính kế thừa cho 2 class student và lecturer do chúng gần giống nhau
# Define class Person
class Person:
    def __init__(self,first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
   
    def print_info(self):
        print(self.first_name+" "+self.last_name+" "+ str(self.age)+" year old!")
        
        
# Define class Student 
class Student(Person):
    def __init__(self, f_name, l_name, age, email,student_id, grade = -1):
        super().__init__(f_name, l_name, age, email)
        self.student_id = student_id
        self.grade = grade
        
    # kế thừa hàm print_info của lớp cha Person, và do không muốn dùng nhiều hàm khác nhau
    # nên cta sử dụng tính đa hình
    # nạp chồng
    def print_info(self):
        super().print_info()
        print("Student ID: "+self.student_id)
        print("GradeL "+str(self.grade))
    
# Define class Lecturer:
class Lecturer(Person):
    def __init__(self, f_name, l_name, age, email,banhk_account):
        super().__init__(f_name, l_name, age, email)
        self.bank_account = banhk_account
    
    # nập chồng
    def print_info(self):
        super().print_info()
        print("Bank Account:"+ str(self.bank_account))

# khai báo khởi tạo các đối tượng cụ thể
lecturer_TEK4VN = Lecturer("Hưng","Đặng",35,"hungnguyen@tek4.vn",1234567)
python_course = Course("Lập trình Python cơ bản",2019,1234,lecturer_TEK4VN)
student_hai = Student("Hải","Nguyễn",18,"hainguyen@tek4.vn","108001024")
student_ba=Student("Ba", "Nguyễn", 21, "banguyen@tek4.vn", "108001025")
python_course.enroll(student_hai)
python_course.enroll(student_ba)    

# In ra sinh viên có trong khóa học
python_course.print_student()
python_course.print_lecturer()
student_hai.print_info()
lecturer_TEK4VN.print_info()   
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
