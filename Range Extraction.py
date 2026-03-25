def solution(args):
    x, output = 0,''
    while x < len(args):
        if x == len(args)-1:
            output += f"{args[x]},"
        else:
            first = args[x]
            tail = False
            while x < len(args)-1 and args[x+1] == args[x]+1:
                tail = args[x+1]
                x += 1
            
            if tail == False:
                output += f"{first},"
            elif tail - first == 1:
                output += f"{first},{tail},"
            else:
                output += f"{first}-{tail},"
        x += 1
    return output.rstrip(',')
