N, H, M, T = map(int, input().split())

sleep_count = N
first_alarm_hour = H
first_alarm_min = M
alarm_interval = T

total_min = 60 * first_alarm_hour + first_alarm_min
add_min = (sleep_count - 1) * alarm_interval
total_min += add_min
total_min %= (60 * 24)

# 切り捨て除算
result_hour = total_min // 60
# 割った余り
total_min = total_min % 60


print(result_hour)
print(total_min)
