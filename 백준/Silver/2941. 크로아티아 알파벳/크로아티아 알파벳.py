croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

for alpha in croatian_alphabets:
    string = string.replace(alpha, '*')

print(len(string))