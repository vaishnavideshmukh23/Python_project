#Tip Calculator Project
print("Welcome to tip calculator")

#Give multiple inputs
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip you want to give? 10 12 15"))
people = int(input("How many people are spliting the bill?"))

#Dividing tip into total number of person
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

#final amount 
final_amount = round(bill_per_person, 3)

print(f"Each person should pay: ${final_amount}")
