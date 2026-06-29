def minimumIndex(capacity: list[int], itemSize: int) -> int:
    i = 0
    smallest_capacity = []
    while i < len(capacity):
        if capacity[i] >= itemSize:
            smallest_capacity.append(capacity[i])
        
        i += 1

    if len(smallest_capacity) == 0:
        return -1

    smallest_capacity = sorted(smallest_capacity)



    return capacity.index(smallest_capacity[0])


print(minimumIndex(capacity = [1,5,3,7], itemSize = 3))