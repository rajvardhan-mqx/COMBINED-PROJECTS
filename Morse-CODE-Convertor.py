def convert_to_morse_code(code):
  code = code.replace("0","-.")
  code = code.replace("1",".-")
  code = code.replace("2",".--")
  code = code.replace("3",".---")
  code = code.replace("4","..--")
  code = code.replace("5",".---")
  code = code.replace("6","---...")
  code = code.replace("7","...---")
  code = code.replace("8","----....")
  code = code.replace("9","----.....")
  code = code.replace("10","-----.....")
  return code 

default = "7249803897"
print(f"Default code:{default}")

morse = convert_to_morse_code(default)
print(f"Morse code:{morse}")
#Insert the numbers in the default variable to see the change#
  

