counter = 0

while True:
    command = input().split()
    
    match command[0]:
        case "zero":
            counter = 0
        case "add":
            counter += int(command[1])
        case "minus":
            counter -= int(command[1])
        case "mul":
            counter *= int(command[1])
        case "div":
            counter //= int(command[1])
        case "result":
            print(counter)
        case "exit":
            break
            