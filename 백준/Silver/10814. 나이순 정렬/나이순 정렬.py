import sys
input = sys.stdin.read

def sort_by_age(members):
    sorted_members = sorted(members, key=lambda x: x[0])
    return sorted_members

data = input().split('\n')
n = int(data[0])
members = []

for i in range(1, n + 1):
    if data[i]:
        age, name = data[i].split()
        age = int(age)
        members.append((age, name))

sorted_members = sort_by_age(members)

for age, name in sorted_members:
    print(age, name)