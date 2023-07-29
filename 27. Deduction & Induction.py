def deduction(premises, conclusion):
  if all(premise in premises for premise in conclusion):
    return True
  else:
    return False

def induction(premises, conclusion):
  if all(premise in conclusion for premise in premises):
    return True
  else:
    return False

premises = ["All men are mortal.", "Socrates is a man."]
conclusion = "Socrates is mortal."

print("Deduction:", deduction(premises, conclusion))
print("Induction:", induction(premises, conclusion))
