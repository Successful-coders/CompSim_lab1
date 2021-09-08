import bubbleSort


def sort(array):
    bubbleSortArray = array.copy()
    defaultSortArray = array.copy()

    bubbleSort.sort(bubbleSortArray)
    defaultSortArray.sort()

    print("init array = " + array.__str__())
    print('array sorted by bubble method = ' + bubbleSortArray.__str__())
    print('array sorted by default = ' + defaultSortArray.__str__())
