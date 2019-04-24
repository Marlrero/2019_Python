def postfix_to_infix(expression):
    stack = []
    postfix = ""
    for i in expression:
        print(i, "||", len(stack), ">>", stack, "||", postfix)
        if i == '(':  # 열린 괄호는 스택에 들어감
            stack.append(i)
        elif i == ')':  # 닫힌 괄호는 열린 괄호까지 스택에서 빼냄
            while len(stack) > 0 and stack[len(stack) - 1] != '(':
                postfix = postfix + stack.pop()
            if stack[len(stack) - 1] == '(':  # 열린 괄호는 postfix에 집어넣지 않음
                stack.pop()
        elif i == '*' or i == '/':  # 곱하기와 나누기는
            while len(stack) > 0 and \
                    (stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/'):  # 스택에 연산자 우선순위가 같은 것이 있다면
                postfix = postfix + stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':  # 더하기와 빼기는
            if len(stack) > 0 and \
                    (stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/'):  # 스택에 연산자 우선순위가 높은 것이 들어가 있다면
                postfix = postfix + stack.pop()
            stack.append(i)
        else:  # 그 외에는
            postfix = postfix + i

    for i in range(len(stack)):  # 스택에 나머지를 모두 빼냄
        postfix = postfix + stack.pop()

    return postfix

def main():
    #사용자로부터 중위표기식을 입력함
    expression = input("Infix Expression >> ")

    postfix = postfix_to_infix(expression)

    print(postfix)

main()
