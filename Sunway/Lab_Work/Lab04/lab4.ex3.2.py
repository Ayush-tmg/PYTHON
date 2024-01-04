######## EXERCISE 2 ########

def get_data():
    house_counts = []
    for i in range(7):
        prompt = f"Enter the number of houses with {i} occupants: "
        count = int(input(prompt))
        house_counts.append(count)
    count_6plus = int(input("Enter the number of houses with 6 plus occupants: "))
    house_counts.append(count_6plus)
    return house_counts

def cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7):
    house_count = (h0,h1,h2,h3,h4,h5,h6,h7)
    total_houses = sum(house_count)
    percentages = []

    for count in house_count:
        p = (count / total_houses) * 100
        percentages.append(p)

    return percentages

def display_result(h0,h1,h2,h3,h4,h5,h6,h7,p0,p1,p2,p3,p4,p5,p6,p7):
    print(f"{'Occupancy:' :>12}", end='')
    for i in range(0, 8):
        if i == 7:
            print(f"{'>6':>7}")
            break
        print(f"{i:>7}", end='')
    
    print(f"{'No. houses:' :>12}", end='')

    house_counts = (h0,h1,h2,h3,h4,h5,h6,h7)
    percentages = (p0,p1,p2,p3,p4,p5,p6,p7)

    for house in house_counts:
        print(f"{house:>7}", end='')
    
    print()

    print(f"{'Percentage:' :>12}", end=' ')
    for percent in percentages:
        val = round(percent, 1)
        print(f"{val:>6}%", end='')
    print('')

if __name__ == "__main__":
    h0,h1,h2,h3,h4,h5,h6,h7 = get_data()
    p0,p1,p2,p3,p4,p5,p6,p7 = cal_percentage(h0,h1,h2,h3,h4,h5,h6,h7)
    display_result(h0,h1,h2,h3,h4,h5,h6,h7,p0,p1,p2,p3,p4,p5,p6,p7)