def compactness(formulas):
  """Returns True if formulas is satisfiable, False otherwise."""
  for n in range(len(formulas) + 1):
    for subset in itertools.combinations(formulas, n):
      if is_satisfiable(subset):
        return True
  return False

def main():
  formulas = ["P", "not P", "P or Q", "P and Q"]
  print(compactness(formulas))

if __name__ == "__main__":
  main()
