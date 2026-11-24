age = int(input("enter your age :"))
marks  = int(input("enter your marks :"))

if age >= 18:
    print("eligible for addmission")
    if marks >=50:
        print("addmission confirm")
    else:
        print("not  eligible ")

else:
    print("addmission not apporved ")