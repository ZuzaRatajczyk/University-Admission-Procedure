
class Department:

    def __init__(self, name, n, exam):
        self.name = name
        self.accepted_students = []
        self.num_of_free_places = n
        self.exam = exam

    def add_student(self, student):
        self.accepted_students.append(student)

    def sort_students(self):
        self.accepted_students.sort(key=lambda stud: (-float(stud.results[self.exam]), stud.first_name))

    def show_accepted(self):
        print(self.name)
        self.sort_students()
        for student in self.accepted_students:
            print(student.first_name, student.last_name, student.results[self.exam])

    def __add__(self, other):
        self.num_of_free_places += other

    def __sub__(self, other):
        self.num_of_free_places -= other


class Student:

    def __init__(self, first_name, last_name):
        self.results = {"physics": 0.0, "chemistry": 0.0, "math": 0.0, "computer_science": 0.0}
        self.recruitment_departments = {"first_priority": "", "second_priority": "", "third_priority": ""}
        self.first_name = first_name
        self.last_name = last_name

    def add_result(self, subject, result):
        self.results[subject] = result

    def add_recruitment_department(self, priority, department):
        self.recruitment_departments[priority] = department

    def calculate_result(self, subject1, subject2):
        self.results[subject1 + " + " + subject2] = (self.results[subject1] + self.results[subject2]) / 2


def create_student(line_from_file):
    applicants_lst = line_from_file.split()
    applicant_obj = Student(applicants_lst[0], applicants_lst[1])
    idx = 2
    for subject in applicant_obj.results.keys():
        applicant_obj.add_result(subject, float(applicants_lst[idx]))
        idx += 1
    for priority in applicant_obj.recruitment_departments.keys():
        applicant_obj.add_recruitment_department(priority, applicants_lst[idx])
        idx += 1
    applicant_obj.calculate_result("computer_science", "math")
    applicant_obj.calculate_result("physics", "math")
    applicant_obj.calculate_result("chemistry", "physics")
    return applicant_obj


def read_from_file():
    list_of_applicants = []
    file = open("applicant_list_6.txt", "r")
    for line in file:
        list_of_applicants.append(create_student(line))
    file.close()
    return list_of_applicants


def write_to_file(department):
    f = open(f"{department.name.lower()}.txt", "w")
    department.sort_students()
    for student in department.accepted_students:
        f.write(student.first_name + " " + student.last_name + " " + str(student.results[department.exam]) + "\n")
    f.close()


def choose_best_candidates(list_of_candidates, department, priority):
    best_candidates = []
    for applicant in list_of_candidates:
        if department.num_of_free_places == 0:
            break
        if applicant.recruitment_departments[priority] == department.name:
            best_candidates.append(applicant)
            department.num_of_free_places -= 1
    for applicant in best_candidates:
        list_of_candidates.remove(applicant)
    return best_candidates


def recruitment(list_of_applicants, departments_list, stage):
    for department in departments_list:
        list_of_applicants.sort(key=lambda app: (-(app.results[department.exam]), app.first_name))
        accepted = choose_best_candidates(list_of_applicants, department, stage)
        for student in accepted:
            department.add_student(student)


def main():
    n = int(input())  # max number of students for each department
    list_of_applicants = read_from_file()
    departments_list = [Department("Biotech", n, "chemistry + physics"),
                        Department("Chemistry", n, "chemistry"),
                        Department("Engineering", n, "computer_science + math"),
                        Department("Mathematics", n, "math"),
                        Department("Physics", n, "physics + math")]
    recruitment(list_of_applicants, departments_list, "first_priority")
    recruitment(list_of_applicants, departments_list, "second_priority")
    recruitment(list_of_applicants, departments_list, "third_priority")
    for department in departments_list:
        department.show_accepted()
        print("\n")
    for department in departments_list:
        write_to_file(department)


if __name__ == "__main__":
    main()
