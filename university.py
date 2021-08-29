
class Department:

    def __init__(self, n, exam):
        self.accepted_students = []
        self.num_of_free_places = n
        self.exam = exam

    def add_student(self, student):
        self.accepted_students.append(student)

    def show_accepted(self):
        self.accepted_students.sort(key=lambda stud: (-float(stud.results[self.exam]), stud.last_name))
        for student in self.accepted_students:
            print(student.firs_name, student.last_name, student.results[self.exam])

    def __add__(self, other):
        self.num_of_free_places += other

    def __sub__(self, other):
        self.num_of_free_places -= other


class Student:

    def __init__(self, first_name, last_name):
        self.results = {"physics": 0.0, "chemistry": 0.0, "math": 0.0, "computer_science": 0.0}
        self.recruitment_departments = {"first_priority": "", "second_priority": "", "third_priority": ""}
        self.firs_name = first_name
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
    return applicant_obj


def read_from_file():
    list_of_applicants = []
    file = open("applicant_list_6.txt", "r")
    for line in file:
        list_of_applicants.append(create_student(line))
    return list_of_applicants


def choose_best_candidates(list_of_candidates, department_name, department_obj, priority):
    best_candidates = []
    for applicant in list_of_candidates:
        if department_obj.num_of_free_places == 0:
            break
        if applicant.recruitment_departments[priority] == department_name:
            best_candidates.append(applicant)
            department_obj.num_of_free_places -= 1
    for applicant in best_candidates:
        list_of_candidates.remove(applicant)
    return best_candidates


def recruitment(list_of_applicants, departments_dict, stage):
    for department, dep_obj in departments_dict.items():
        list_of_applicants.sort(key=lambda app: (-(app.results[dep_obj.exam]), app.last_name))
        accepted = choose_best_candidates(list_of_applicants, department, dep_obj, stage)
        for student in accepted:
            dep_obj.add_student(student)


def main():
    n = int(input())  # max number of students for each department
    list_of_applicants = read_from_file()
    departments_dict = {"Biotech": Department(n, "chemistry"),
                        "Chemistry": Department(n, "chemistry"),
                        "Engineering": Department(n, "computer_science + math"),
                        "Mathematics": Department(n, "math"),
                        "Physics": Department(n, "physics + math")}
    recruitment(list_of_applicants, departments_dict, "first_priority")
    recruitment(list_of_applicants, departments_dict, "second_priority")
    recruitment(list_of_applicants, departments_dict, "third_priority")
    for department, obj in departments_dict.items():
        print(department)
        obj.show_accepted()
        print("\n")


if __name__ == "__main__":
    main()
