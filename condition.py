'''a=190
if a>=90 and a<=100:
    print("Grade AA")
elif a>=40 or a<90:
    print("Greater 40")
elif a>60:
    print("Greater 60")
else:
    print("Not Match")'''





  

'''if age>=18 and voterCard.upper()=='Y' and aadharCard.upper()=='Y' and nationality.upper()=='Y':
    print("Yes You Are Eligible")
else:
    print("No You Are Not Eligible")'''
def checkData():
    age=int(input("Enter Age \n"))
    if age>=18:
        voterCard=input("Do You Have Voter Card y/n \n")
        if voterCard.upper()=='Y':
            aadharCard=input("Do You Have Aadhar Card y/n \n")
            if aadharCard.upper()=='Y':
                nationality=input("Are You Indian y/n \n")
                if nationality.upper()=='Y':
                    print("Yes You Are Eligible")
                else:
                    print("You are not Indian")
            else:
                print("You Do not have Aadhar Card")
        else:
            print("You do not have voter card") 
    else:
        print("You Are Under 18")

for i in range(1,11,1):
    checkData()