# values in dicts are columns in file with applicants
RECRUITMENT_STAGES = {"first_admission": 6, "second_admission": 7, "third_admission": 8}
EXAMS = {"physics": 2, "chemistry": 3, "math": 4, "computer_science": 5}


class Department:

    def __init__(self, n, exam):
        self.accepted_students = []
        self.num_of_free_places = n
        self.exam_idx = exam

    def add_student(self, student):
        self.accepted_students.append(student)

    def show_accepted(self):
        self.accepted_students.sort(key=lambda x: (-float(x[self.exam_idx]), x[0]))
        for student in self.accepted_students:
            print(" ".join(student[:2]), student[self.exam_idx])

    def __add__(self, other):
        self.num_of_free_places += other

    def __sub__(self, other):
        self.num_of_free_places -= other


def read_from_file():
    list_of_applicants = []
    file = open("applicant_list_5.txt", "r")
    for line in file:
        list_of_applicants.append(line.split())
    # list_of_applicants.sort(key=lambda x: (-float(x[2]), x[0]))
    return list_of_applicants


def choose_best_candidates(list_of_candidates, depart, obj, stage_of_admission):
    best_candidates = []
    for applicant in list_of_candidates:
        if obj.num_of_free_places == 0:
            break
        if applicant[stage_of_admission] == depart:
            best_candidates.append(applicant)
            obj.num_of_free_places -= 1
    for applicant in best_candidates:
        list_of_candidates.remove(applicant)
    return best_candidates


def recruitment(list_of_applicants, departments_dict, stage):
    for department, obj in departments_dict.items():
        list_of_applicants.sort(key=lambda x: (-float(x[obj.exam_idx]), x[0]))
        accepted = choose_best_candidates(list_of_applicants, department, obj, RECRUITMENT_STAGES[stage])
        for student in accepted:
            obj.add_student(student)


def main():
    n = int(input())  # max number of students for each department
    list_of_applicants = read_from_file()
    departments_dict = {"Biotech": Department(n, EXAMS["chemistry"]),
                        "Chemistry": Department(n, EXAMS["chemistry"]),
                        "Engineering": Department(n, EXAMS["computer_science"]),
                        "Mathematics": Department(n, EXAMS["math"]),
                        "Physics": Department(n, EXAMS["physics"])}
    recruitment(list_of_applicants, departments_dict, "first_admission")
    recruitment(list_of_applicants, departments_dict, "second_admission")
    recruitment(list_of_applicants, departments_dict, "third_admission")
    for department, obj in departments_dict.items():
        print(department)
        obj.show_accepted()
        print("\n")


if __name__ == "__main__":
    main()
