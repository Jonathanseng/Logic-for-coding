def quantity(proposition):
  """
  This function takes a categorical proposition as input and returns the quantity
  of the proposition.

  The four quantities of a categorical proposition are:
    * Universal: All or Every.
    * Particular: Some.

  Args:
    proposition: The categorical proposition to be analyzed.

  Returns:
    The quantity of the proposition.
  """

  if proposition.startswith("All"):
    return "Universal"
  else:
    return "Particular"

def quality(proposition):
  """
  This function takes a categorical proposition as input and returns the quality
  of the proposition.

  The two qualities of a categorical proposition are:
    * Affirmitive: Is or Are.
    * Negative: Is not or Are not.

  Args:
    proposition: The categorical proposition to be analyzed.

  Returns:
    The quality of the proposition.
  """

  if proposition.endswith("are"):
    return "Affirmative"
  else:
    return "Negative"

def distribution(proposition):
  """
  This function takes a categorical proposition as input and returns the
  distribution of the proposition.

  The two distributions of a categorical proposition are:
    * Universal: Refers to all members of the subject class.
    * Particular: Refers to some members of the subject class.

  Args:
    proposition: The categorical proposition to be analyzed.

  Returns:
    The distribution of the proposition.
  """

  if proposition.startswith("All"):
    return "Universal"
  else:
    return "Particular"

proposition = "All men are mortal."

print(quantity(proposition))
print(quality(proposition))
print(distribution(proposition))
