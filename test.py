class Department:
    def __init__(self,emp_dept):
        self.dept_name = emp_dept

    def display_dept_name(self):
        return print(self.dept_name)



class Employee(Department):
    def __init__(self,*args):   
        super().__init__(args[4])    
        self.emp_detail = []
        self.emp_name = args[0]
        self.emp_age = args[1]
        self.emp_city = args[2]
        self.emp_id = args[3]

    def add_employee_details(self):
        emp_detail = input("enter the Employee details: ")
        self.emp_detail.append(emp_detail)
        return self.emp_detail
 
    def modify_emp_details(self, emp_id):
        if emp_id in self.emp_detail:
            print(self.emp_detail)
            

    def display_emp_details(self):
        pass

    def remove_emp_details(self):
        pass


if __name__ == '__main__':
    obj1 = Employee('Pranu', 30, 'Pune', '1','IT')
    obj1.add_employee_details()
    

