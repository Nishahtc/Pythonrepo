name=("India","Nepal","America","Canada","Bhutan")
print(name[2])
try:
    name[1]="australia"
except TypeError as error:
    print("error found", error)




