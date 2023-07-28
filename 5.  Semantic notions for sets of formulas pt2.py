def implication(formula1, formula2):
  """Returns the implication of formula1 and formula2."""
  return "not " + formula1 + " or " + formula2

def equivalence(formula1, formula2):
  """Returns the equivalence of formula1 and formula2."""
  return implication(formula1, formula2) + " and " + implication(formula2, formula1)

def main():
  formulas = ["P", "not P", "P or Q", "P and Q"]
  print(implication("P", "Q"))
  print(equivalence("P", "Q"))

if __name__ == "__main__":
  main()
