from ArrayStack import ArrayStack as Stack

def is_matched(s):
    stack = []
    for string in s:
        if string in "({[":
            stack.append(string)

        elif string in ")}]":
            if not stack:
                return False

            top = stack.pop()

            if (top == "(" and string != ")") or \
                (top == "{" and string != "}") or \
                    (top == "[" and string != "]"):
                return False


    return len(stack) == 0

user = input("Enter an expression: ")
s = user


if is_matched(s) and ("(" in s or "{" in s or "[" in s):
    print("The balance of Parenthesis, brackets and braces is correct")
else:
    print("The balance of Parenthesis, brackets and braces is incorrect")






