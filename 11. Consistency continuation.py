def consistency_continuation(axioms, theorems):
  """Returns True if continuation is consistent, False otherwise."""
  for formula in theorems:
    if not is_satisfiable([formula] + axioms):
      return False
  return True

def main():
  axioms = ["P implies Q", "Q implies R"]
  theorems = ["P implies R"]
  continuation = ["P"]
  print(consistency_continuation(axioms, theorems))
  print(consistency_continuation(axioms, theorems + continuation))

if __name__ == "__main__":
  main()
