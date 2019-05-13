def convert(number, dic):
    total = 0
    prev = 0
    for i in list(number):
        cur = dic[i]
        # print cur
        if prev < cur:
            total = total - prev
            cur = cur - prev
        total = total + cur
        # print total
        prev = cur
    return total


roman_map = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "m": 1000}
n = raw_input("enter a roman number: ")
print convert(n, roman_map)
