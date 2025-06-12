import matplotlib.pyplot as plt


def assignment(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def merge_sort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        merge_sort(left)
        merge_sort(right)

        length_l = 0
        r = 0
        i = 0

        while length_l < len(left) and r < len(right):
            if left[length_l] <= right[r]:
                assignment(new_list=list_to_sort_by_merge,
                           i=i, old_list=left, j=length_l)
                length_l += 1
            else:
                assignment(new_list=list_to_sort_by_merge, i=i, old_list=right,
                           j=r)
                r += 1
            i += 1

        while length_l < len(left):
            list_to_sort_by_merge[i] = left[length_l]
            length_l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
merge_sort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
