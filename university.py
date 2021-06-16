n = int(input())
m = int(input())
names_and_scores = []
for _ in range(n):
    names_and_scores.append(input().split())
names_and_scores.sort(key=lambda x: (-float(x[2]), x[0]))
print("Successful applicants:")
for i, application in enumerate(names_and_scores):
    print(application[0], application[1])
    if i == m-1:
        break

