
class Department:

    def __init__(self, name, n, exam):
        self.name = name
        self.accepted_students = []
        self.num_of_free_places = n
        self.exam = exam

    def _get_candidate_result(self, candidate):
        special_exam_result = candidate.results["special_exam"]
        exam_result = candidate.results[self.exam]
        return special_exam_result if special_exam_result > exam_result else exam_result

    def sort_students(self, students):
        def get_tuple(student):
            return -(self._get_candidate_result(student)), student.first_name
        students.sort(key=get_tuple)

    def recruit(self, candidates, stage):
        self.sort_students(candidates)
        for applicant in candidates:
            if self.num_of_free_places == 0:
                break
            if applicant.recruitment_departments[stage] == self.name:
                self.accepted_students.append(applicant)
                self.num_of_free_places -= 1
        for student in self.accepted_students:
            if student in candidates:
                candidates.remove(student)

    def add_student(self, student):
        self.accepted_students.append(student)

    def show_accepted(self):
        print(self.name)
        self.sort_students(self.accepted_students)
        for student in self.accepted_students:
            print(student.first_name, student.last_name, self._get_candidate_result(student))

    def write_accepted_to_file(self):
        self.sort_students(self.accepted_students)
        with open(f"{self.name.lower()}.txt", "w") as f:
            for student in self.accepted_students:
                f.write(student.first_name + " " + student.last_name + " " + str(self._get_candidate_result(student)) + "\n")


class Candidate:

    def __init__(self, first_name, last_name, results_list, candidate_priorities):
        self.subjects = ["physics", "chemistry", "math", "computer_science", "special_exam"]
        results_list = [float(result) for result in results_list]
        self.results = dict(zip(self.subjects, results_list))
        self.priorities = ["first_priority", "second_priority", "third_priority"]
        self.recruitment_departments = dict(zip(self.priorities, candidate_priorities))
        self.first_name = first_name
        self.last_name = last_name

    def add_result(self, subject, result):
        self.results[subject] = result

    def add_recruitment_department(self, priority, department):
        self.recruitment_departments[priority] = department

    def calculate_result(self, subject1, subject2):
        self.results[subject1 + " + " + subject2] = (self.results[subject1] + self.results[subject2]) / 2


def create_applicant(line_from_file):
    applicants_lst = line_from_file.split()
    applicant_obj = Candidate(applicants_lst[0], applicants_lst[1], applicants_lst[2:7], applicants_lst[7:])
    applicant_obj.calculate_result("computer_science", "math")
    applicant_obj.calculate_result("physics", "math")
    applicant_obj.calculate_result("chemistry", "physics")
    return applicant_obj


def read_from_file():
    list_of_applicants = []
    with open("applicant_list_7.txt", "r") as file:
        for line in file:
            list_of_applicants.append(create_applicant(line))
    return list_of_applicants


def recruitment(list_of_applicants, departments_list, stage):
    for department in departments_list:
        department.recruit(list_of_applicants, stage)


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
        department.write_accepted_to_file()
        print("\n")
    for department in departments_list:
        department.show_accepted()
        print("\n")


if __name__ == "__main__":
    main()
