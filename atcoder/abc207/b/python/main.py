a, b, c, d = map(int, input().split())
add_count = 0

if(b >= c * d):
    print(-1)
else:
    while True:
        blue = a + (b * add_count)
        red = c * d * add_count
        if blue <= red:
            print(add_count)
            break
        add_count += 1
