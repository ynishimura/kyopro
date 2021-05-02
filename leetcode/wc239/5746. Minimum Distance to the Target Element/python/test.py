def binary_search_find_closest(data, target):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    min_diff = float('inf')
    imin = 0
    imax = len(data) - 1
    closest_num = None
    while imin <= imax:
        # min_diff_left = 1
        imid = imin + (imax - imin) // 2
        #　中心の左右の値と目標との差を計算する。
        if imid + 1 < len(data):
            min_diff_right = abs(data[imid+1] - target)
        if imid >= 0:
            min_diff_left = abs(data[imid-1] - target)
        # 最初の差と最も最小に近い値を更新する。
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[imid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[imid+1]
        # 2分探索する。
        if data[imid] < target:
            imin = imid + 1
        elif data[imid] > target:
            imax = imid -1
        else:
            return data[imid]
    return closest_num

def binary_search(array, item):
    head = 0
    tail = len(array) - 1

    while head <= tail:
        center = (head + tail) // 2
        if array[center] == item:
            return center
        elif array[center] < item:
            head = center + 1
        else:
            tail = center - 1

    return None
# 15が表示される。

list_given = [1,4]
# list_given = [1, 3, 5, 6, 6, 8, 9, 11, 15, 16]
# list_given = [3, 1, 4, 6, 5, 0, 2]
list_given.sort()
print(binary_search_find_closest(list_given, 2))
