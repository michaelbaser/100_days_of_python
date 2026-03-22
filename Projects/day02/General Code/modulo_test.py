print(f"10 / 2 = {10 / 2}\n10 % 2 = {10 % 2}\n\n"
      
      f"10 / 3 = {10 / 3}\n10 % 3 = {10 % 3}\n\n"
      
      f"11 / 5 = {11 / 5}\n11 % 5 = {11 % 5}\n\n"
      
      f"12 / 5 = {12 / 5}\n12 % 5 = {12 % 5}\n\n"      
      
      f"13 / 5 = {13 / 5}\n13 % 5 = {13 % 5}\n\n"
      
      f"14 / 5 = {14 / 5}\n14 % 5 = {14 % 5}\n\n"
      
      f"15 / 5 = {15 / 5}\n15 % 5 = {15 % 5}\n\n"
      )


top_number = int(input("Please enter your numerator/dividend ('top number'):\n"))
bottom_number = int(input("Please enter your denominator/divisor ('bottom number'):\n\n"))

division_result = top_number / bottom_number

subtraction_result = top_number - bottom_number

floor_division_result = top_number // bottom_number  

multiplication_result = floor_division_result * bottom_number 

subtraction_final_result = top_number - multiplication_result

modulo_result = top_number % bottom_number

print(f"\n-----------------------------------------------------------\n"
      f"Remember... Your top number = {top_number} and your bottom number = {bottom_number} !!!\n"
      f"-----------------------------------------------------------\n\n"
      f"The division result of {top_number} / {bottom_number} = {division_result}\n"
      f"The subtraction result of {top_number} - {bottom_number} = {subtraction_result}\n"
      f"The floor division result of {top_number} // {bottom_number} = {floor_division_result}\n"
      f"The multiplication result of {floor_division_result} (floor division result) * {bottom_number} = {multiplication_result}\n"      
      f"The subtraction final result of {top_number} - {multiplication_result} (multiplication result) = {subtraction_final_result}\n"
      f"The modulo result of {top_number} % {bottom_number} = {modulo_result}")
