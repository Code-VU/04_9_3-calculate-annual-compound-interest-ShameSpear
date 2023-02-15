# def print_math_compound_interest(principle, rate, time):
#     totalAmount = principle*(1+(rate/100))**time
#     print("Compound Interest: "+ str(round(totalAmount - principle,2)))

# def collect_inputs_and_convert_to_float():
#     client_principal = float(input("Principle (amount): "))
#     client_time =      float(input("Time:               "))
#     client_rate =      float(input("Rate:               "))
#     return client_principal, client_time, client_rate

def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
 #print("Compound Interest: "+str(intrest))
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))

    client_one_amount = client_one_principal*(1 + client_one_rate/100)**client_one_time
    client_one_ci = client_one_amount - client_one_principal
    print("Compound Interest: " + str(round(client_one_ci, 2)))
    print("---")
    client_two_principal = float(input("Principle (amount): "))
    client_two_time =      float(input("Time:               "))
    client_two_rate =      float(input("Rate:               "))

    client_two_amount = client_two_principal*(1 + client_two_rate/100)**client_two_time
    client_two_ci = client_two_amount - client_two_principal
    print(f"Compound Interest: " + str(round(client_two_ci, 2)))
    print("---")        
    client_three_principal = float(input("Principle (amount): "))
    client_three_time =      float(input("Time:               "))
    client_three_rate =      float(input("Rate:               "))

    client_three_amount = client_three_principal*(1 + client_three_rate/100)**client_three_time
    client_three_ci = client_three_amount - client_three_principal
    print(f"Compound Interest: " + str(round(client_three_ci, 2)))
    # print("---")
    # end assignment
    #
    #Solution from dashboard
    # line_break = "---"

    # client_principal_1, client_time_1, client_rate_1 = collect_inputs_and_convert_to_float()
    # print_math_compound_interest(client_principal_1, client_rate_1, client_time_1)
    # print(line_break)
    # client_principal_2, client_time_2, client_rate_2 = collect_inputs_and_convert_to_float()
    # print_math_compound_interest(client_principal_2, client_rate_2, client_time_2)
    # print(line_break)
    # client_principal_3, client_time_3, client_rate_3 = collect_inputs_and_convert_to_float()
    # print_math_compound_interest(client_principal_3, client_rate_3, client_time_3)
    
## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
