import math
R, X, Y = map(int, input().split())

distance = math.sqrt(X*X + Y*Y)


if distance < R:
    """
    一歩の距離が目標地点の距離より大きいとき2回
    """
    print(2)
else:
    """
    目標地点の距離を一歩の距離で割って切り上げした
    """
    print(math.ceil(distance/R))
