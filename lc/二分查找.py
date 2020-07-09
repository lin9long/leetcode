def binarySearch(target_list, target):
    left = 0
    right = len(target_list) - 1

    while left < right:
        mid = (left + right) // 2
        if target < target_list[mid]:
            right = mid - 1
        elif target > target_list[mid]:
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    target_list = [500, 222, 400, 108,108,108, 300, 101, 200, 111, 100]
    target_list = sorted(target_list)
    idx = binarySearch(target_list, 108)
    print(idx,target_list[idx])
