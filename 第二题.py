size = 5

# 连锁挖矿
def block(x, y, block_list):
    k = block_list[x][y];
    recursion(x, y, k, block_list)

# 遍历
def recursion(x, y, k, block_list):
    if (x < 0 or x >= len(block_list)):
        return
    if (y < 0 or y >= len(block_list)):
        return
    if (block_list[x][y] != k):
        return
    if (block_list[x][y] == 9):
        return

    block_list[x][y] = 9;
    recursion(x + 1, y, k, block_list)
    recursion(x - 1, y, k, block_list)
    recursion(x, y + 1, k, block_list)
    recursion(x, y - 1, k, block_list)


if __name__ == "__main__":
    block_list = [[0, 2, 0, 2, 0], [0, 0, 2, 2, 1], [2, 2, 2, 0, 0], [2, 0, 0, 2, 2], [0, 1, 0, 1, 1]]

    for i in block_list:
        print(i)

    x = 0
    y = 3

    print("破坏" + str(x) + "," + str(y) + "处的方块，并连锁破坏")

    # block方法
    block(x, y, block_list)

    for i in block_list:
        print(i)
