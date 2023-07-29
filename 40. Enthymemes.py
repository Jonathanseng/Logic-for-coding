import re

def enthymeme(premises):
  """Returns the enthymeme in standard form."""
  
  # Check if the premises are in standard form.
  if not all(re.match(r"(A|E)I|O", premise) for premise in premises):
    return None
  
  # Identify the major, minor, and conclusion terms.
  major_term = premises[0][0]
  minor_term = premises[1][0]
  conclusion_term = premises[2][0]
  
  # Identify the missing premise.
  if major_term not in premises[1]:
    missing_premise = f"All {major_term} are {conclusion_term}."
  else:
    missing_premise = f"All {minor_term} are {major_term}."
  
  # Return the enthymeme in standard form.
  return f"{premises[0]} {premises[1]} {missing_premise} {premises[2]}"

def main():
  premises = ["Socrates is a man.", "All men are mortal.", "Therefore, Socrates is mortal."]
  print(enthymeme(premises))

if __name__ == "__main__":
  main()
