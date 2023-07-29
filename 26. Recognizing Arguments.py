import re

def recognize_arguments(text):
  premises = []
  conclusions = []
  patterns = [
    r"Premise \d+.",
    r"Conclusion.",
  ]
  for sentence in text.split("."):
    for pattern in patterns:
      match = re.match(pattern, sentence)
      if match:
        if pattern == r"Premise \d+.":
          premises.append(sentence)
        elif pattern == r"Conclusion.":
          conclusions.append(sentence)
  return premises, conclusions

premises, conclusions = recognize_arguments("""
Premise 1.
Premise 2.
Conclusion.
""")

print("Premises:")
print(premises)

print("Conclusions:")
print(conclusions)
