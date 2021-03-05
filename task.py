a = input('Please enter command (Ex-MMSWSMM): ')
constrins = (0, 0, 3, 4)
dirs = ('E', 'W', 'N', 'S')
curr_point = [0, 0, 'S']
for cmd in a:
    if cmd in dirs:
        curr_point[2] = cmd
    elif cmd == 'M':
        if curr_point[2] == 'S' and curr_point[0] != constrins[2]:
            curr_point[0] += 1
        elif curr_point[2] == 'E' and curr_point[1] != constrins[3]:
            curr_point[1] += 1
        elif curr_point[2] == 'N' and curr_point[0] != constrins[1]:
            curr_point[0] -= 1
        elif curr_point[2] == 'W' and curr_point[1] != constrins[0]:
            curr_point[1] -= 1
    else:
        print('Invalid command found')
        break
       
print(curr_point)
