def validity(premises, conclusion):
  if all(premise in premises for premise in conclusion):
    return True
  else:
    return False

def truth(premises, conclusion):
  for premise in premises:
    if not premise:
      return False
  return conclusion

def soundness(premises, conclusion):
  if validity(premises, conclusion) and truth(premises, conclusion):
    return True
  else:
    return False

def strength(premises, conclusion):
  if validity(premises, conclusion):
    if truth(premises, conclusion):
      return True
    else:
      return False
  else:
    return False

def cogencience(premises, conclusion):
  if strength(premises, conclusion) and truth(premises, conclusion):
    return True
  else:
    return False

premises = ["All men are mortal.", "Socrates is a man."]
conclusion = "Socrates is mortal."

print("Validity:", validity(premises, conclusion))
print("Truth:", truth(premises, conclusion))
print("Soundness:", soundness(premises, conclusion))
print("Strength:", strength(premises, conclusion))
print("Cogency:", cogencience(premises, conclusion))
