import random

#Global variable to count comparisions
comparision_count_deterministic = 0
comparision_count_randomized = 0

def deterministic_quick_sort(arr):
    #Deterministic Quick Sort algorithm
    global comparision_count_deterministic
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2] #Choose the middle element as the pivot
    left = []
    middle = []
    right =[]

    for x in arr:
        comparision_count_deterministic += 1 #Count comparison
        if x<pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    #Randomized Quick Sort algorithm
    global comparision_count_randomized
    if len(arr)<=1:
        return arr
    pivot = random.choice(arr) #Choose a random pivot
    left = []
    middle =[]
    right = []

    for x in arr:
        comparision_count_randomized += 1 #Count comparision
        if x<pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

if __name__ == "__main__":
    #Generate random data
    array_size = 10000
    test_array = [random.randint(1, 10000) for _ in range(array_size)]

    #Analuze deterministic quick sort
    sorted_deterministic = deterministic_quick_sort(test_array)
    print("Deterministic Quick Sort completed")
    print(f"Deterministic Quick Sort performed {comparision_count_deterministic} comparisions")

    #Analyze randomized quick sort
    sorted_randomized = randomized_quick_sort(test_array)
    print("Randomized Quick Sort completed")
    print(f"Randomized Quick Sort performed {comparision_count_randomized} comparisions")

    #Optionally we can also check if both sorted arrays are equal
    assert sorted_deterministic == sorted_randomized, "Both sorting methods should yeild the same sorted array"