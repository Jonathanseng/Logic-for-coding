def arguments_premises_conclusions(arguments):
  premises = []
  conclusions = []
  for argument in arguments:
    for sentence in argument:
      if sentence.startswith("Premise"):
        premises.append(sentence)
      elif sentence.startswith("Conclusion"):
        conclusions.append(sentence)
  return premises, conclusions

premises, conclusions = arguments_premises_conclusions([
  "Premise 1",
  "Premise 2",
  "Conclusion",
])

print("Premises:")
print(premises)

print("Conclusions:")
print(conclusions)
