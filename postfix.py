from LinkedStack import LinkedStack as Stack




def infix_to_postfix(expression):
    """Convert an infix expression with parentheses to a postfix expression."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    op = Stack()

    for token in expression.split():
        if token.isnumeric():  # If token is an operand, add it to output
            output.append(token)
        elif token == '(':  # If token is '(', push it onto the stack
            op.push(token)
        elif token == ')':  # If token is ')', pop until '(' is found
            while not op.is_empty() and op.top() != '(':
                output.append(op.pop())
            op.pop()  # Pop the '(' from the stack
        else:  # If token is an operator
            while (not op.is_empty() and op.top() != '(' and
                   precedence[token] <= precedence[op.top()]):
                output.append(op.pop())
            op.push(token)

    # Pop any remaining operators in the stack
    while not op.is_empty():
        output.append(op.pop())

    return " ".join(output)


def postfix(expression):
    """Evaluate a postfix expression."""
    S = Stack()
    for token in expression.split():
        if token.isnumeric():  # If token is an operand, push it onto the stack
            S.push(int(token))
        else:  # If token is an operator, pop operands and apply the operator
            b = S.pop()
            a = S.pop()
            if token == '+':
                S.push(a + b)
            elif token == '-':
                S.push(a - b)
            elif token == '*':
                S.push(a * b)
            elif token == '/':
                S.push(a / b)
            elif token == '^':
                S.push(a ** b)
    return S.pop()
infix_exp = "( ( 5 + 2 ) ∗ ( 8 − 3 ) ) / 4"
postfix_exp = infix_to_postfix(infix_exp)
print("Infix Expression: ", infix_exp)
print("Postfix Expression: ", postfix_exp)




