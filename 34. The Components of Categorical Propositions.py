def components(proposition):
  """
  This function takes a categorical proposition as input and returns a tuple of the
  four components of the proposition.

  The four components of a categorical proposition are:
    * Subject: The term that is being described.
    * Predicate: The term that is describing the subject.
    * Quantity: The quantifier of the proposition.
    * Quality: The quality of the proposition.

  Args:
    proposition: The categorical proposition to be analyzed.

  Returns:
    A tuple of the four components of the proposition.
  """

  subject = proposition.split(" ")[0]
  predicate = proposition.split(" ")[1]
  quantity = proposition.split(" ")[2]
  quality = proposition.split(" ")[3]

  return subject, predicate, quantity, quality

proposition = "All men are mortal."

print(components(proposition))
