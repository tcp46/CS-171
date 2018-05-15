#Tess Porter
#tcp46
#CS 171-C (lab 070)
print('Welcome to the Student Loan Calculator')
#take input values for the principle and number of years on the loan
p = int(input('Enter the amount of the loan in dollars with (no commas):\n'))
y = int(input('Enter the number of years the loan will be for:\n'))
t = 12
print('------------------------------')
print('Subsidized Federal Direct Loan')
print('Principle:',p)
sub_i = 0.034
print('Interest Rate:',round(100*sub_i,2))
print('Years:',y)
#Below is where I set up the calculations for monthy payment
sub_mp = (p * sub_i) / (t * (1 - (1 + (sub_i/t)) ** (-y * t)))
print('Monthly Payment', round(sub_mp,2))
sub_total_paid_on_loan = sub_mp * t * y
print('Total Paid on Loan:', round(sub_total_paid_on_loan,2))
sub_total_i = sub_total_paid_on_loan - p
print('Total Interest Paid:', round(sub_total_i,2))
sub_fees = p * 0.01051
print('Additional Fees Paid:', round(sub_fees,2))
sub_costs_over_p = sub_total_i + sub_fees
print('Total Costs Over Principle:', round(sub_costs_over_p,2))
print('------------------------------')
print('Unsubsidized Federal Direct Loan')
print('Principle:',p)
unsub_i = 0.068
print('Interest Rate:',round(100*unsub_i,2))
print('Years:',y)
#Unsubsidized loans have a special principle as calculated below
unsub_p = p * (1 + unsub_i * 4.25)
#For the monthly payment I use the special unsubsidize principle
unsub_mp = (unsub_p * unsub_i) / (t * (1 - (1 + (unsub_i/t)) ** (-y * t)))
print('Monthly Payment', round(unsub_mp,2))
unsub_total_paid_on_loan = unsub_mp * t * y
print('Total Paid on Loan:', round(unsub_total_paid_on_loan,2))
unsub_total_i = unsub_total_paid_on_loan - p
print('Total Interest Paid:', round(unsub_total_i,2))
unsub_fees = p * 0.01051
print('Additional Fees Paid:', round(unsub_fees,2))
unsub_costs_over_p = unsub_total_i + unsub_fees
print('Total Costs Over Principle:', round(unsub_costs_over_p,2))
print('------------------------------')
print('Federal Plus Loan')
print('Principle:',p)
plus_i = 0.079
print('Interest Rate:',round(100*plus_i,2))
print('Years:',y)
#Plus loans also have a special principle - calculated below
plus_p = p * (1 + plus_i * 4.25)
#For the monthly payment I use the special plus principle to calculate
plus_mp = (plus_p * plus_i) / (t * (1 - (1 + (plus_i/t)) ** (-y * t)))
print('Monthly Payment', round(plus_mp,2))
plus_total_paid_on_loan = plus_mp * t * y
print('Total Paid on Loan:', round(plus_total_paid_on_loan,2))
plus_total_i = plus_total_paid_on_loan - p
print('Total Interest Paid:', round(plus_total_i,2))
plus_fees = p * 0.04204
print('Additional Fees Paid:', round(plus_fees,2))
plus_costs_over_p = plus_total_i + plus_fees
print('Total Costs Over Principle:', round(plus_costs_over_p,2))






