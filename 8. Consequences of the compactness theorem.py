def compactness_consequences(formulas):
  """Returns a list of the consequences of formulas."""
  consequences = []
  for n in range(len(formulas) + 1):
    for subset in itertools.combinations(formulas, n):
      if is_satisfiable(subset):
        for formula in subset:
          if formula not in consequences:
            consequences.append(formula)
  return consequences

def main():
  formulas = ["P", "not P", "P or Q", "P and Q"]
  print(compactness_consequences(formulas))

if __name__ == "__main__":
  main()
