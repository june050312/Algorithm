my_string = "He11oWor1d"
overwrite_string = "lloWorl"
s = 2

print(my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):])