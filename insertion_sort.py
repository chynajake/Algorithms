# Insertion sort

def insertion_sort(array):
    print("initial: %s"%array)
    for j in range(1,len(array)):
        key = array[j]
        i = j - 1
        print("key=%d, j=%d, i=%d"%(key, j, i))
        while i > -1 and array[i] > key:
            print("change")
            print(array)
            array[i+1] = array[i]
            print(array)
            i = i - 1
        array[i+1] = key
        print(array)
        print("-"*20)
    return array

test = [3,9,8,5,1,2] 

insertion_sort(test)
