class Department:

    def __init__(self, n):
        self.accepted_students = []
        self.num_of_free_places = n

    def add_student(self, student):
        self.accepted_students.append(student)

    def show_accepted(self):
        self.accepted_students.sort(key=lambda x: (-float(x[2]), x[0]))
        for student in self.accepted_students:
            print(" ".join(student[:3]))

    def __add__(self, other):
        self.num_of_free_places += other

    def __sub__(self, other):
        self.num_of_free_places -= other


def read_from_file():
    list_of_applicants = []
    file = open("applicants.txt", "r")
    for line in file:
        list_of_applicants.append(line.split())
    list_of_applicants.sort(key=lambda x: (-float(x[2]), x[0]))
    return list_of_applicants


def choose_best_candidates(list_of_candidates, depart, obj, department_idx):
    best_candidates = []
    for applicant in list_of_candidates:
        if obj.num_of_free_places == 0:
            break
        if applicant[department_idx] == depart:
            best_candidates.append(applicant)
            obj.num_of_free_places -= 1
    for applicant in best_candidates:
        list_of_candidates.remove(applicant)
    return best_candidates


def main():
    n = int(input())  # max number of students for each department
    list_of_applicants = read_from_file()
    departments_dict = {"Biotech": Department(n), "Chemistry": Department(n), "Engineering": Department(n),
                        "Mathematics": Department(n), "Physics": Department(n)}
    for department, obj in departments_dict.items():
        accepted = choose_best_candidates(list_of_applicants, department, obj, 3)
        for student in accepted:
            obj.add_student(student)
    for department, obj in departments_dict.items():
        accepted = choose_best_candidates(list_of_applicants, department, obj, 4)
        for student in accepted:
            obj.add_student(student)
    for department, obj in departments_dict.items():
        accepted = choose_best_candidates(list_of_applicants, department, obj, 5)
        for student in accepted:
            obj.add_student(student)
    for department, obj in departments_dict.items():
        print(department)
        obj.show_accepted()
        print("\n")


if __name__ == "__main__":
    main()
