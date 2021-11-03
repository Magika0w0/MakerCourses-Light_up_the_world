def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

if __name__ == '__main__':

    # for j in range(256):
    #     for i in range(144):
    #         print( i, ":",(i + j) % 255, wheel((i + j) % 255), end='')
    #     print()

    for i in range(10, 0, -1):
        print(i)

