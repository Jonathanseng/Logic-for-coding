def least_upper_bound(set, element):
  """Returns the least upper bound of element in set, or None if no such bound exists."""
  if not isinstance(set, list):
    return None
  if element in set:
    return element
  for x in set:
    if x <= element and (x == element or all(x < y for y in set if y > x)):
      return x
  return None

def main():
  set = [1, 2, 3, 4, 5]
  print(least_upper_bound(set, 3))
  print(least_upper_bound(set, 6))

if __name__ == "__main__":
  main()
