str = input("Enter the string: ")
def char(str):
  upper_case = 0
  lower_case = 0
  for i in str:
      if i >= 'a' and i <= 'z':
       lower_case += 1

      if i >='A' and i<='Z':
       upper_case += 1

  print("LowerCase letter in the String",lower_case)
  print("UpperCase letter in the String",upper_case)
char(str)