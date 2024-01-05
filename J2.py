#print('+' * 9)

def CodeDecoder(messages):
    
    decoded_messages = []

    for i in messages:
        split_code = i.split(" ")
        n = int(split_code[0])
        c = split_code[1]
        d = c * n
        decoded_messages.append(d)

    return decoded_messages


def main():
    L = int(input().strip())
    messages = []

    for _ in range(L):
        code = input().strip()
        messages.append(code)

    result = CodeDecoder(messages)
    for i in result:
        print(i)


if __name__ == "__main__":
    main()