import math

def cycle_sort(array) -> int:
    """Sort an array in place and return the number of writes."""
    writes = 0

    # Loop through the array to find cycles to rotate.
    # Note that the last item will already be sorted after the first n-1 cycles.
    for cycle_start in range(0, len(array) - 1):
        item = array[cycle_start]

        # Find where to put the item.
        pos = cycle_start
        for i in range(cycle_start + 1, len(array)):
            if array[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycle_start:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycle_start:
            # Find where to put the item.
            pos = cycle_start
            for i in range(cycle_start + 1, len(array)):
                if array[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            writes += 1

    return writes


def lilysHomework(arr):
    swaps = 0
    arr1 = arr[:]
    swaps1 = 0
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            t = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = t
            swaps += 1

    for i in range(len(arr1) - 1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr1[j] > arr1[max_index]:
                max_index = j
        if max_index != i:
            t = arr1[max_index]
            arr1[max_index] = arr1[i]
            arr1[i] = t
            swaps1 += 1
            if swaps1 >= swaps:
                return swaps

    return min(swaps, swaps1)


def kmerge_sort(a, p, r):
    # if r < p + 4:
    #     insertion_sort(a, p, r)
    # else:
    if p < r:
        mid = (p + r) // 2
        kmerge_sort(a, p, mid)
        kmerge_sort(a, mid + 1, r)
        kmerge(a, p, mid, r)


def kmerge(a, p, mid, r):
    global inv
    left = a[p:mid+1]
    right = a[mid+1:r+1]
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[p+i+j] = left[i]
            i += 1
        else:
            a[p+i+j] = right[j]
            j += 1
            inv += len(left) - i
            # inv += 1

    while i < len(left):
        a[p+i+j] = left[i]
        i += 1
    while j < len(right):
        a[p+i+j] = right[j]
        j += 1


inv = 0
# a = [3, 4, 2, 5, 1]
a = "656085744 592976686 3037922 82266352 17574000 344340000 8406892 591292449 569625472 899357375 251327440 301303036 281400020 77370228 15516426 82859300 88364436 39767760 148417500 306863056 10926174 118195200 310408774 309307894 200852782 82193280 424056750 249277128 180368880 477624006 86748948 7434336 48882310 112635040 6614541 503907132 598034610 160500171 70444416 72752680 271416096 30521205 529365648 399367584 129849984 263500556 76737948 464269640 613416088 162724716 163420800 720512988 1217212920 727647624 383190420 8350904 3456024 289141064 123384024 158867856 82005504 36225521 533012608 54370440 17671500 53627000 26597644 855638940 55343960 57828624 108025344 21431808 1182600 265643950 30054300 219553915 74203500 658061160 7502400 931691763 295769136 107345925 80109000 130922055 33544944 65280 452996453 301655430 7828912 425016000 297635898 26861016 739961600 928116 19645470 8691456 5123880 596100015 2735436 25596483 173620720 202797504 161748972 30122300 11082820 574006860 426732182 71136825 105659136 1808140278 450779280 286831620 104683008 938781480 175050736 255681692 67096152 119518575 15449840 25273458 165048960 5642130 85199958 354920488 446786340 131214816 41533296 25766518 90782304 59007600 700369740 122021794 56982366 238027920 434370816 223677580 72463156 355858300 144914616 145950 13822570 19914930 11072100 21450528 124958730 105156800 20843784 781192188 448358850 6139822 95694780 78713888 677177472 9963972 366432768 181113408 725292862 473528052 12864000 518355540 55832070 318508876 89963781 1796290329 844308846 428627693 276255100 123609720 440449488 27589680 426614166 110068200 408846096 620309228 186565236 49051552 561738897 650114105 32646556 7174400 275364045 945364797 3674160 66314292 11073770 14885370 245088324 669628848 33110250 971699976 324099072 259496060 492110802 52206516 508725376 1534995792 148078816 57993375 121071195 381960195 12496176 23728250 159836835 712982980 160098622 909675852 110400300 485423372 30637838 339925836 285371600 13618242 80809650 92375040 265612788 1151909241 234661320 16962144 213417000 269646860 1015650090 117439476 53164566 6946134 89506800 305469360 13406432 292353000 9969642 43982198 23887296 67730660 16384192 218824704 1082660306 1679473908 136336179 39265884 1077096020 464272368 87048192 56752487 156212388 360621525 8472816 17613600 62143172 82696127 79939536 155805468 159499963 262072360 39827904 179532360 2455040 327280740 148409340 73738980 3394872 3082560 225009981 188912256 179487784 340340 315171072 96680664 621206280 536379504 391714074 65055960 105570465 365721408 106712025 286764660".split(" ")
a = list(map(int, a))
b = a[:]
c = a[:]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            inv += 1
print("inversions", inv)
print("len", len(b))
inv = 0
print("cycle  swaps", cycle_sort(a))
print("swaps", lilysHomework(c))
kmerge_sort(b, 0, len(b)-1)
# print(a)
# print(b)
print("inversions", inv)