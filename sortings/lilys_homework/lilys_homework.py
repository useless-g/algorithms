def lilysHomework(arr):
    arr_reversed = arr[::-1]
    arr_sorted_map = {j: i for i, j in enumerate(sorted(arr))}
    arr_reversed_sorted_map = {j: i for i, j in enumerate(sorted(arr_reversed))}
    swaps_asc = swaps_desc = 0
    last_swaps = -1
    while swaps_asc != last_swaps:
        last_swaps = swaps_asc
        for i in range(len(arr)):
            if arr_sorted_map[arr[i]] != i:
                t = arr[arr_sorted_map[arr[i]]]
                arr[arr_sorted_map[arr[i]]] = arr[i]
                arr[i] = t
                swaps_asc += 1

    last_swaps = -1
    while swaps_desc != last_swaps:
        last_swaps = swaps_desc
        for i in range(len(arr_reversed)):
            if arr_reversed_sorted_map[arr_reversed[i]] != i:
                t = arr_reversed[arr_reversed_sorted_map[arr_reversed[i]]]
                arr_reversed[arr_reversed_sorted_map[arr_reversed[i]]] = arr_reversed[i]
                arr_reversed[i] = t
                swaps_desc += 1
    return min(swaps_asc, swaps_desc)
