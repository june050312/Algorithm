before = "olleh"
after = "helo"

for i in before:
    if i in after:
        after = after.replace(i, "", 1)
    else:
        print(0)
        break
else:
    print(1)