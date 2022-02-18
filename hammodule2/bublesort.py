def bubleSort(arr):
        n = len(arr)
        swapped = True
        while swapped:
            swapped = False
            for i in range(n - 1):
                if(arr[i] > arr[i+1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True


if __name__ == "__main__":
    myList = [12, 34, 5, 67, 69, 99]
    bubleSort(myList)
    print("My List after sort:", myList)
