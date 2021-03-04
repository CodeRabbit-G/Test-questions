import random


def relationship(x, y, verts):
    try:
        x, y = float(x), float(y)
    except:
        return False

    # 获取横坐标和纵坐标的值
    vertx = [xyvert[0] for xyvert in verts]
    verty = [xyvert[1] for xyvert in verts]

    # ABCD四个点中，通过其横坐标和纵坐标的最大值和最小值，初步判断目标坐标点是否有可能在这个四边形之内
    if not verts or not min(vertx) <= x <= max(vertx) or not min(verty) <= y <= max(verty):
        return False

    # 进一步判断E的与ABCD点的坐标关系
    nvert = len(verts) - 1
    is_in = False
    j = nvert
    for i in range(nvert):
        if i != 0:
            j = i
            i = i + 1

        if ((verty[i] > y) != (verty[j] > y)) and (
                x < (vertx[j] - vertx[i]) * (y - verty[i]) / (verty[j] - verty[i]) + vertx[i]):
            is_in = not is_in

    print(is_in)
    return is_in


if __name__ == "__main__":
    # 假设ABCD点的二维坐标为
    quadrangle = [(40, 0), (0, 0), (0, 40), (40, 40)]

    # E点的坐标(x,y)
    x = random.randint(0, 50)
    y = random.randint(0, 50)
    print("E点的坐标(%d,%d)" % (x, y))

    if relationship(x, y, quadrangle):
        print("E点在四边形ABCD内")
    else:
        print("E点不在四边形ABCD内")
