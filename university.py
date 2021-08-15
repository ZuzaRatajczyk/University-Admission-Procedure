class Department:

    def __init__(self, n, score_idx):
        self.accepted_students = []
        self.num_of_free_places = n
        self.score_idx = score_idx

    def add_student(self, student):
        self.accepted_students.append(student)

    def show_accepted(self):
        self.accepted_students.sort(key=lambda x: (-float(x[self.score_idx]), x[0]))
        for student in self.accepted_students:
            print(" ".join(student[:2]), student[self.score_idx])

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
    departments_dict = {"Biotech": Department(n, 3), "Chemistry": Department(n, 3), "Engineering": Department(n, 5),
                        "Mathematics": Department(n, 4), "Physics": Department(n, 2)}
    for department, obj in departments_dict.items():
        list_of_applicants.sort(key=lambda x: (-float(x[obj.score_idx]), x[0]))
        accepted = choose_best_candidates(list_of_applicants, department, obj, 6)
        for student in accepted:
            obj.add_student(student)
    for department, obj in departments_dict.items():
        list_of_applicants.sort(key=lambda x: (-float(x[obj.score_idx]), x[0]))
        accepted = choose_best_candidates(list_of_applicants, department, obj, 7)
        for student in accepted:
            obj.add_student(student)
    for department, obj in departments_dict.items():
        list_of_applicants.sort(key=lambda x: (-float(x[obj.score_idx]), x[0]))
        accepted = choose_best_candidates(list_of_applicants, department, obj, 8)
        for student in accepted:
            obj.add_student(student)
    for department, obj in departments_dict.items():
        print(department)
        obj.show_accepted()
        print("\n")


if __name__ == "__main__":
    main()
