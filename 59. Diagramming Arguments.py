def diagram_argument(premises, conclusion):
    diagram = ""
    for premise in premises:
        diagram += "(" + premise + ")"
    diagram += " --> " + conclusion
    return diagram


def main():
    premises = ["All dogs are mammals.", "All mammals are warm-blooded."]
    conclusion = "All dogs are warm-blooded."
    print(diagram_argument(premises, conclusion))


if __name__ == "__main__":
    main()
