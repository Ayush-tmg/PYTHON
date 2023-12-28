def find_max(l):
    return max(l)

print(find_max([1,2,3,4,5]))

#Write a function that takes list as an arguement and rounds up

def find_avg(l):
    # sum = 0
    # for item in l:
    #     sum = sum + item
    # avg = sum / len(l)

    return round(sum(l) / len(l), 2)
    # return round(avg, 2)

print(find_avg([1,2,3,4,5]))