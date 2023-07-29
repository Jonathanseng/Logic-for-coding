import re

def standard_form(premises):
  """Returns the standard form of the categorical syllogism."""
  
  # Check if the premises are in standard form.
  if not all(re.match(r"(A|E)I|O", premise) for premise in premises):
    return None
  
  # Identify the major, minor, and conclusion terms.
  major_term = premises[0][0]
  minor_term = premises[1][0]
  conclusion_term = premises[2][0]
  
  # Identify the mood of the syllogism.
  mood = ""
  for premise in premises:
    if premise[1] == "A":
      mood += "A"
    elif premise[1] == "E":
      mood += "E"
    elif premise[1] == "I":
      mood += "I"
    elif premise[1] == "O":
      mood += "O"
  
  # Identify the figure of the syllogism.
  figure = 1
  if major_term in premises[1]:
    figure += 1
  if minor_term in premises[0]:
    figure += 2
  
  return f"{mood}{figure}"

def main():
  premises = ["All dogs are animals.", "All cats are animals.", "Therefore, all cats are dogs."]
  print(standard_form(premises))

if __name__ == "__main__":
  main()
