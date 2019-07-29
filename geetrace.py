import random

def get_trace(distance):
    u = 187
    a = 452.3177185058594
    c = 1.0000401423527645
    r2 = 496.6467504426631
    r1 = 230.65741262170448
    n = 1.0000401423527645
    track = [
        [int(round(u / c - r1)),
         int(round(a / c - r2)), 0],
    ]
    track.append([0, 0, 0])
    count = r1
    y = 1
    t = 0
    scale = [0.2, 0.5, random.randint(6, 8) / 10]
    distance = distance + r1
    while count < distance:
        if count < distance * scale[0]:
            x = random.randint(1, 2)
        elif count < distance * scale[1]:
            x = random.randint(3, 4)
        elif count < distance * scale[2]:
            x = random.randint(5, 6)
        elif count < distance * 0.9:
            x = random.randint(2, 3)
        elif count < distance:
            x = 1
        count += x
        t += random.randint(10, 30)
        r = count / n - r1
        y += random.randint(0, 1)
        track.append([int(round(r)), y, t])
    track.append([track[-1][0], track[-1][1], t + random.randint(90, 300)])
    replace_y(track)
    return track


def replace_y(arr):
    n = len(arr)
    count1 = 1
    count2 = 1
    tmp = []
    while True:
        size = random.randint(1, 6)
        if count1 + size > n:
            break
        if count2 <= 13:
            for i in range(count1, count1 + size):
                arr[i][1] = count2
            count2 += 1
        else:
            count2 += random.randint(-1, 0)
            for i in range(count1, count1 + size):
                arr[i][1] = count2
        count1 += size
    for i in range(count1, n):
        arr[i][1] = count2


if __name__ == "__main__":
    print(get_trace_normal(58))
