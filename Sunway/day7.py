def find_max(l):
    return max(l)

print(find_max([1,2,3,4,5]))

def find_avg(l):
    sum = 0
    for item in l:
        sum = sum + item
    avg = sum / len(l)
    return avg

print(find_avg([1,2,3,4,5]))