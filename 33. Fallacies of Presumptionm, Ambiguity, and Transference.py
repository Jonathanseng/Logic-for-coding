def fallacies(argument):
  """
  This function takes an argument as input and returns a list of the fallacies
  that are present in the argument.

  The fallacies that are checked for are:
    * Presumption: Assuming the conclusion in the premises.
    * Ambiguity: Using a word or phrase with multiple meanings.
    * Transference: Shifting the burden of proof to the opponent.

  Args:
    argument: The argument to be analyzed.

  Returns:
    A list of the fallacies that are present in the argument.
  """

  fallacies = []

  # Presumption

  if "must" or "should" in argument:
    fallacies.append("Presumption")

  # Ambiguity

  if "can" or "may" in argument:
    fallacies.append("Ambiguity")

  # Transference

  if "you have to prove" or "you must show" in argument:
    fallacies.append("Transference")

  return fallacies

argument = "Since all humans are mortal, and Socrates is a human, Socrates must be mortal."

print(fallacies(argument))
