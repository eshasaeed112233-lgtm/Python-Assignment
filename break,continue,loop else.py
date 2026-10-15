# Break
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Loop else
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")