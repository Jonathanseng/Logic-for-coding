def truth_value(structure, interpretation):
  """Returns the truth value of structure under interpretation."""
  if structure == "True":
    return True
  if structure == "False":
    return False
  if len(structure) == 2 and structure[0] in ["x", "f"]:
    return interpretation[structure[0]]
  if len(structure) == 3 and structure[0] == "and":
    return truth_value(structure[1], interpretation) and truth_value(structure[2], interpretation)
  if len(structure) == 3 and structure[0] == "or":
    return truth_value(structure[1], interpretation) or truth_value(structure[2], interpretation)
  if len(structure) == 3 and structure[0] == "not":
    return not truth_value(structure[1], interpretation)
  return False

def main():
  interpretation = {"x": True, "y": False}
  structures = [
    ["True"],
    ["False"],
    ["x", "y"],
    ["and", ["x", "y"], ["z", "w"]],
    ["or", ["x", "y"], ["z", "w"]],
    ["not", ["x", "y"]]
  ]
  for structure in structures:
    print(truth_value(structure, interpretation))

if __name__ == "__main__":
  main()
