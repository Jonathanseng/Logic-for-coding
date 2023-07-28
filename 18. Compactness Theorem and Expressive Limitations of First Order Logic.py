def compactness(formulas):
  """Returns True if formulas is satisfiable, False otherwise."""
  if not isinstance(formulas, list):
    return False
  if len(formulas) == 0:
    return True
  for subset in itertools.combinations(formulas, len(formulas) - 1):
    if is_satisfiable(subset):
      return True
  return False

def main():
  formulas = ["P", "not P", "P or Q", "P and Q"]
  print(compactness(formulas))

if __name__ == "__main__":
  main()
