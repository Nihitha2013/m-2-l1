m= input("Any medical cause for absentee? (y/n):")
a=int(input("Enter attendance:"))
if m=="y":
    print("Allowed for exam")
else:
    if a>75:
        print("allowed for exam")
    else:
        print(" not allowed for exam")