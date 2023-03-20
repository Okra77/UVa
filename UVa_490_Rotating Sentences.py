while True:
    try:
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        max_len = max(len(line) for line in lines)

        lines.reverse()
        for i in range(max_len):
            for line in lines:
                if i < len(line):
                    print(line[i], end="")
                else:
                    print(" ", end="")
            print()
    except EOFError:
        break