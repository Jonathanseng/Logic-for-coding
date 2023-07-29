def is_valid(premises, conclusion):
  if all(premise in premises for premise in conclusion):
    return True
  else:
    return False

def is_invalid(premises, conclusion):
  if not is_valid(premises, conclusion):
    return True
  else:
    return False

def is_contradiction(premises):
  for premise in premises:
    if premise == "not" + premise:
      return True
  return False

premises = ["All men are mortal.", "Socrates is a man.", "Socrates is not mortal."]
conclusion = "Socrates is mortal."

print("Is invalid:", is_invalid(premises, conclusion))
print("Is contradiction:", is_contradiction(premises))
