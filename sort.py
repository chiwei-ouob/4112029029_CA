def bubble_sort(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # print (arr)
    return arr

def insertion_sort(arr): 
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        # print (arr)
    return arr

def quick_sort(arr):  # to move the numbers that is smaller than pivot, the first number in the (sub-)array
    if len(arr) <= 1:
        return arr  # stop sorting when the (sub-)array is empty or has only one element.
    pivot = arr[0]
    # print ("pivot = {}, (sub)array = {}".format(pivot, quick_sort([x for x in arr[1:] if x < pivot]) + [pivot] + quick_sort([x for x in arr[1:] if x >= pivot])))  # test how much times it had tried
    return quick_sort([x for x in arr[1:] if x < pivot]) + [pivot] + quick_sort([x for x in arr[1:] if x >= pivot])
    # elements less than pivot will be on the left side, greater on the right

def merge_sort(arr): 
    from math import ceil as roundup  # 向上取整
    if len(arr) <= 1: 
        return arr
    arr_l = merge_sort(arr[:roundup(len(arr)/2)])
    arr_r = merge_sort(arr[roundup(len(arr)/2):])
    merged_arr = []
    l_index = r_index = 0
    while l_index < len(arr_l) and r_index < len(arr_r): # 條件在任一子陣列取盡時不成立
        if arr_l[l_index] <= arr_r[r_index]: 
            merged_arr.append(arr_l[l_index])
            l_index += 1
        else: 
            merged_arr.append(arr_r[r_index])
            r_index += 1
    merged_arr.extend(arr_l[l_index:])  # 將後者清單延續在前者的尾巴 (也可以直接清單相加) (原本用 append 導致清單連同中括號一起加進去)
    merged_arr.extend(arr_r[r_index:])  # 將兩個子清單中剩餘的元素抓進去 (其中一個已取盡)
    # print (merged_arr)
    return merged_arr

def main():
    # 目標皆為由小到大排列
    best_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    worst_list = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print (f"泡沫排序法(最佳情況): {best_list} -> {bubble_sort(best_list)}")
    print (f"泡沫排序法(最壞情況): {worst_list} -> {bubble_sort(worst_list)}")

    best_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    worst_list = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print (f"插值排序法(最佳情況): {best_list} -> {insertion_sort(best_list)}")
    print (f"插值排序法(最壞情況): {worst_list} -> {insertion_sort(worst_list)}")

    worst_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    best_list = [6, 3, 9, 7, 1, 8, 2, 5, 11, 4, 10]
    print (f"快速排序法(最佳情況): {best_list} -> {quick_sort(best_list)}")
    print (f"快速排序法(最壞情況): {worst_list} -> {quick_sort(worst_list)}")

    best_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    worst_list = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print (f"合併排序法(最佳情況): {best_list} -> {merge_sort(best_list)}")
    print (f"合併排序法(最壞情況): {worst_list} -> {merge_sort(worst_list)}")  # 合併排序法並無最佳或最壞情況

if __name__ == "__main__":
    main()