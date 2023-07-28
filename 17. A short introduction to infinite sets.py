def is_finite(set):
  """Returns True if set is finite, False otherwise."""
  if not isinstance(set, list):
    return False
  if len(set) == 0:
    return True
  for element in set:
    if not is_finite(element):
      return False
  return True

def main():
  sets = [
    [1, 2, 3],
    ["a", "b", "c"],
    [1, ["a", "b", "c"], 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ]
  for set in sets:
    print(is_finite(set))

if __name__ == "__main__":
  main()
