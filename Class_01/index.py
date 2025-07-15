print("Hello World")

# applicantName = input("Enter Applicant Name : ")
# jobAppliedFor = input("Applied Job For : ")
# expectedSalary = int(input("Enter Expected Salary : "))
# AvailableForInterview = input("Available Interview For : ")
#
# print("Applicant Name : ", applicantName , "Job Applied For : " , jobAppliedFor , "Expected Salary is : " , expectedSalary , "Available For Interview : " , AvailableForInterview)
# print(f"Applicant Name : {applicantName}\nJob Applied For : {jobAppliedFor}\nExpected Salary is : {expectedSalary}\nAvailable For Interview : {AvailableForInterview}")

print("MY HALWA PORI SHOP")

puriQuantity = int(input("How Many Poris Do You Want ? : "))
ChulaQuantity = int(input("How Many Chula Plets Do You Want ? : "))
AaluQuantity = int(input("How Many Aalu Plets Do You Want ? : "))
halwaQuantity = int(input("How Many Halwa Plets Do You Want ? : "))

perPori = 50
perChulaPlet = 80
perAaluPlet = 70
perHalwaPlet = 100

totalPoris = perPori * puriQuantity
totalChula = perChulaPlet * ChulaQuantity
totalAalu = perAaluPlet * AaluQuantity
totalHalwa = perHalwaPlet * halwaQuantity

totalBill = totalPoris + totalChula + totalAalu + totalHalwa
payment = input("Do You Want To Pay Card ? : ")

if payment == "yes":
    tax = totalBill * 0.08
else:
    tax = 0

finalBill = totalBill + tax
discount = finalBill * 0.25
pureFinalBill = finalBill - discount

print(
    f"- No Of Poris : {puriQuantity}\n- No Of Chula Plets : {ChulaQuantity}\n- No Of Aalu Plets : {AaluQuantity}\n- No Of Halwa Plets : {halwaQuantity}\n"
    f"-- Total Bill is : Rs.{totalBill}\n-- Tax is : Rs.{tax}\n-- Final Bill is : Rs.{finalBill}\n-- 25% Discount is : Rs.{discount}\n"
    f"-- Gross final Bill is : Rs.{pureFinalBill}"
)
