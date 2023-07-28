def application_1(formulas):
  """Returns True if formulas is satisfiable, False otherwise."""
  if not isinstance(formulas, list):
    return False
  if len(formulas) == 0:
    return True
  for subset in itertools.combinations(formulas, len(formulas) - 1):
    if "not" in subset:
      return False
  return True

def application_2(formulas):
  """Returns True if formulas is satisfiable, False otherwise."""
  if not isinstance(formulas, list):
    return False
  if len(formulas) == 0:
    return True
  if "for all x" in formulas or "exists x" in formulas:
    return False
  return True

def main():
  formulas_1 = ["P", "not P", "P or Q", "P and Q"]
  formulas_2 = ["for all x, P(x)", "exists x, Q(x)"]
  print(application_1(formulas_1))
  print(application_2(formulas_2))

if __name__ == "__main__":
  main()
