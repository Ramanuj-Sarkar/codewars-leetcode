def interpreter(tape):
    stack = []  #stack will be used for something else first
    output = ''     # this is output at the end
    brackets = {}    # key is one bracket, value is corresponding bracket
    
    # I believe this is faster.
    # It also allows me to change it faster
    # if I suddenly need to account for nested brackets
    for num, char in enumerate(tape):
        if char == '[':
            stack.append(num)
        elif char == ']':
            brackets[num] = stack[-1]
            brackets[stack[-1]] = num
            stack.pop()
    
    stack = [0]     # the stack will be used for the program now
    pointer = 0
    while 0 <= pointer < len(tape):
        char = tape[pointer]
        if char == '+':
            stack[-1] = (stack[-1] + 1) % 256
        elif char == '-':
            stack[-1] = (stack[-1] - 1) % 256
        elif char == '!':
            stack.append(0)
        elif char == '^':
            stack.pop()
        elif char == '*':
            output += chr(stack[-1])
        elif char == '[':
            if stack[-1] == 0:
                pointer = brackets[pointer]
        elif char == ']':
            if stack[-1] != 0:
                pointer = brackets[pointer]
        pointer += 1
    return output
