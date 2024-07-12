# date = input("Enter today's date: ")
# rate = input("How do you rate your day from 1-10? ")
#
# thoughts = input("Let your thoughts flow: ")
#
# with open(f"{date}.txt", "w") as file:
#     file.write(thoughts + "\n")
#     file.write(rate)


def user_input_check():
   upper_count = 0
   digit_count = 0
   input_text = input("Enter a string value :")
   for i in input_text:
       if i.isdigit():
           digit_count +=1
       elif i.isupper():
           upper_count +=1
   if not (len(input_text) >= 8 and digit_count >= 1 and upper_count >= 1):
       print("input must contains atleast 8 characters, 1 upper case and 1 digit")
   else:
       print("Input successfully entered")




user_input_check()

