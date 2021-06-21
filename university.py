def read_from_file():
    list_of_applicants = []
    file = open("applicant_list.txt", "r")
    for line in file:
        list_of_applicants.append(line.split())
    list_of_applicants.sort(key=lambda x: (-float(x[2]), x[0]))
    return list_of_applicants


def choose_best_candidates(list_of_candidates, num_of_places, depart, department_idx):
    best_candidates = []
    for applicant in list_of_candidates:
        if len(best_candidates) == num_of_places:
            break
        if applicant[department_idx] == depart:
            best_candidates.append(applicant)
    for applicant in best_candidates:
        list_of_candidates.remove(applicant)
    return best_candidates


def show_accepted(list_of_students):
    list_of_students.sort(key=lambda x: (-float(x[2]), x[0]))
    for student in list_of_students:
        print(" ".join(student[:3]))


def main():
    n = int(input())  # max number of students for each department
    list_of_applicants = read_from_file()
    departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
    num_of_places = dict.fromkeys(departments, n)
    departments_dict = dict.fromkeys(departments)
    for department in departments_dict:
        accepted = choose_best_candidates(list_of_applicants, n, department, 3)
        num_of_places[department] -= len(accepted)
        departments_dict[department] = accepted
    for department in departments_dict:
        accepted = choose_best_candidates(list_of_applicants, num_of_places[department], department, 4)
        num_of_places[department] -= len(accepted)
        for student in accepted:
            departments_dict[department].append(student)
    for department in departments_dict:
        accepted = choose_best_candidates(list_of_applicants, num_of_places[department], department, 5)
        num_of_places[department] -= len(accepted)
        for student in accepted:
            departments_dict[department].append(student)
    for department in departments_dict:
        print(department)
        show_accepted(departments_dict[department])
        print("\n")


if __name__ == "__main__":
    main()

