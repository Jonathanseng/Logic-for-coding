def halting_problem(program):
  """Returns True if program halts, False otherwise."""
  if not isinstance(program, str):
    return False
  for k in range(1, 100000):
    if is_halting(program, k):
      return True
  return False

def is_halting(program, k):
  """Returns True if program halts in k steps, False otherwise."""
  if program == "halts":
    return True
  if program == "doesn't halt":
    return False
  if k == 0:
    return False
  return halting_problem(program + "halts") or halting_problem(program + "doesn't halt")

def kolmogorov_complexity(program):
  """Returns the Kolmogorov complexity of program."""
  if not isinstance(program, str):
    return False
  return len(program)

def godel_incompleteness(statement):
  """Returns True if statement is undecidable, False otherwise."""
  if not isinstance(statement, str):
    return False
  for k in range(1, 100000):
    if is_provable(statement, k):
      return False
  return True

def is_provable(statement, k):
  """Returns True if statement is provable in k steps, False otherwise."""
  if statement == "true":
    return True
  if statement == "false":
    return False
  if k == 0:
    return False
  return godel_incompleteness(statement + "true") or godel_incompleteness(statement + "false")

if __name__ == "__main__":
  print(halting_problem("halts"))
  print(halting_problem("doesn't halt"))
  print(kolmogorov_complexity("halts"))
  print(godel_incompleteness("true"))
  print(godel_incompleteness("false"))
