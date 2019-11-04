def isSorted(list1):
    print(list1)
    list2 = list1.copy()
    list2.sort()
    if (list1 == list2):
        print("The list is sorted")
        return True
    else:
        print("The list is not sorted")
        return False


def main():
    x = [1,2,3,4,5]
    y = [45,12,54,23,76]
    z = [65,23,545,24,432]
    a = [2,3,4,5,6,7,8]
    isSorted(x)
    isSorted(y)
    isSorted(z)
    isSorted(a)

main()