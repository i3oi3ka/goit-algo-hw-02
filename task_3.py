import re

stack = []
open_brackets = {")": "(", "]": "[", "}": "{"}
close_brackets = ")}]"

def is_closed_brackets(text: str) -> bool:
    brackets = list(re.sub(r"[^\(\)\[\]{}]", "", text))
    for bracket in brackets:
        if bracket in close_brackets:
            if open_brackets[bracket] != stack.pop():
                return False
        else:
            stack.append(bracket)
        print(stack)
    return len(stack) == 0

            
print(is_closed_brackets(input("Enter text: ")))