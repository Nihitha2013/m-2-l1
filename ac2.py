unit=int(input("Enter number of consumed unit of electricity:"))
if unit<50:
    a=unit*2.60
    tax=25
elif unit<100:
    a=130 +((unit-50)*3.25)
    tax=35
elif unit<200:
    a=130 +162+((unit-100)*5.26)
    tax=45
else:
    a=130 +162+526+((unit-150)*8.26)
    tax=60

total=a+tax
print("Electricity bill:",total)

