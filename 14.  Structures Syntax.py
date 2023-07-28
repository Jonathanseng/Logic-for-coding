def is_valid_structure(structure):
  """Returns True if structure is a valid structure, False otherwise."""
  if not isinstance(structure, list):
    return False
  if len(structure) == 0:
    return True
  if len(structure) == 1:
    return structure[0] in ["True", "False"]
  if len(structure) == 2:
    return structure[0] in ["x", "f"] and isinstance(structure[1], str)
  if len(structure) == 3:
    return structure[0] in ["and", "or", "not"] and isinstance(structure[1], list) and isinstance(structure[2], list)
  return False

def main():
  structures = [
    ["True"],
    ["False"],
    ["x", "y"],
    ["and", ["x", "y"], ["z", "w"]],
    ["or", ["x", "y"], ["z", "w"]],
    ["not", ["x", "y"]]
  ]
  for structure in structures:
    print(is_valid_structure(structure))

if __name__ == "__main__":
  main()
