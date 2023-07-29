def intension_and_extension(term):
  """
  This function takes a term as input and returns a tuple of the intension and
  extension of the term.

  The intension of a term is the set of properties that the term denotes.
  The extension of a term is the set of objects that the term denotes.

  Args:
    term: The term to be analyzed.

  Returns:
    A tuple of the intension and extension of the term.
  """

  intension = set()
  extension = set()

  # Intension

  for word in term.split(" "):
    intension.add(word)

  # Extension

  for object in intension:
    if object == term:
      extension.add(object)
    else:
      extension.add(object.lower())

  return intension, extension

term = "The cat is on the mat."

print(intension_and_extension(term))
