list = [2,5,1,3,7,4]
new_list = []

while len(list) != 0:
    num = list[0]
    for i in list:
        if i < num:
            num = i

    new_list.append(num)
    list.remove(num)

print(new_list)


list = [2,5,1,3,7,4]

for i in range(1, len(list)):
    prev = i - 1
    if list[i] < list[prev]:
        while list[i] < list[prev] and prev != 0:
            prev -= 1

        if prev == 0:
             list.insert(prev, list.pop(i))
        else:
            list.insert(prev+1, list.pop(i))

print(list)


list = [2,5,1,3,7,4]
new_list = [2,5,1,3,7,4]

start = 0
end = len(list) - 1

while len(list) != 0:
    min = list[0]
    max = list[0]

    for i in list:
        if i < min:
            min = i
        elif i > max:
            max = i

    new_list[start] = min
    new_list[end] = max

    start += 1
    end -= 1

    list.remove(min)

    if min != max:
        list.remove(max)

print(new_list)


