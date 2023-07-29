def fallacies(argument):
  """
  This function takes an argument as input and returns a list of the fallacies
  that are present in the argument.

  The fallacies that are checked for are:
    * Ad hominem: Attacking the person instead of the argument.
    * Ad populum: Appealing to the majority.
    * Ad nauseam: Repeating an argument over and over again.
    * Ad ignorantiam: Arguing from ignorance.
    * Straw man: Creating a false version of the opponent's argument and then attacking that version.
    * Red herring: Introducing an irrelevant topic into the argument.
    * Weak induction: Drawing a conclusion from a small sample size.

  Args:
    argument: The argument to be analyzed.

  Returns:
    A list of the fallacies that are present in the argument.
  """

  fallacies = []

  # Ad hominem

  if "you" or "your" in argument:
    fallacies.append("Ad hominem")

  # Ad populum

  if "most people" or "everyone" in argument:
    fallacies.append("Ad populum")

  # Ad nauseam

  if argument.endswith(".") * 3:
    fallacies.append("Ad nauseam")

  # Ad ignorantiam

  if "we don't know" or "there is no evidence" in argument:
    fallacies.append("Ad ignorantiam")

  # Straw man

  if "but that's not what I said" in argument:
    fallacies.append("Straw man")

  # Red herring

  if "but what about" in argument:
    fallacies.append("Red herring")

  # Weak induction

  if "a few" or "some" in argument:
    fallacies.append("Weak induction")

  return fallacies

argument = "Most people believe that the earth is flat, so it must be flat."

print(fallacies(argument))
