
initial_bill = input("How much is your bill: ")
initial_bill = float(initial_bill)
tip= input("How much tip 10, 12, 15: ")
people= input("Number of people: ")
people=int(people)
tip= float(tip)
tip_per=initial_bill*(tip/100)
after_tip= initial_bill+tip_per

per_head = round(after_tip/people,2)
print(f"The amount per head is {per_head}.")