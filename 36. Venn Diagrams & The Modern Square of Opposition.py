import random

def create_venn_diagram(proposition):
  """
  This function takes a categorical proposition as input and creates a Venn diagram
  for the proposition.

  Args:
    proposition: The categorical proposition to be analyzed.

  Returns:
    A Venn diagram for the proposition.
  """

  subject = proposition.split(" ")[0]
  predicate = proposition.split(" ")[1]
  quantity = proposition.split(" ")[2]
  quality = proposition.split(" ")[3]

  diagram = []
  for i in range(3):
    row = []
    for j in range(3):
      row.append(" ")
    diagram.append(row)

  if quantity == "All":
    diagram[0][0] = subject
    diagram[2][2] = predicate

  elif quantity == "Some":
    diagram[0][2] = subject
    diagram[2][0] = predicate

  if quality == "Affirmative":
    diagram[1][1] = " "

  else:
    diagram[1][1] = predicate

  return diagram

def modern_square_of_opposition(proposition):
  """
  This function takes a categorical proposition as input and returns a
  representation of the proposition in the modern square of opposition.

  Args:
    proposition: The categorical proposition to be analyzed.

  Returns:
    A representation of the proposition in the modern square of opposition.
  """

  subject = proposition.split(" ")[0]
  predicate = proposition.split(" ")[1]
  quantity = proposition.split(" ")[2]
  quality = proposition.split(" ")[3]

  if quality == "Affirmative":
    if quantity == "All":
      return "A"
    else:
      return "I"

  else:
    if quantity == "All":
      return "E"
    else:
      return "O"

proposition = "All men are mortal."

print(create_venn_diagram(proposition))
print(modern_square_of_opposition(proposition))
