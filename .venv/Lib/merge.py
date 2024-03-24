# Eshal_Arif_100865627_Algorithms_Data_Structures
# importing playsound
from playsound import playsound
# creating a mergesort function which takes the array,
# and a variable called step for tracking each step
# if length of the array is <= 1, return the same array (already sorted)
def mergesort(array, step=1):
    if len(array) <= 1:
        return array
    # splitting array to left and right halves
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # printing the steps
        print("Step", step, ":", left, "|", right)

        # recursively sorting both halves, and incrementing the steps
        left = mergesort(left, step=step + 1)
        right = mergesort(right, step=step + 1)

        # merging the sorted halves
        n = i = j = 0
        while n < len(left) and i < len(right):
            if left[n] <= right[i]:
                array[j] = left[n]
                n += 1
            else:
                array[j] = right[i]
                i += 1
            j += 1

        while n < len(left):
            array[j] = left[n]
            n += 1
            j += 1

        while i < len(right):
            array[j] = right[i]
            i += 1
            j += 1
        playsound('../swap.mp3')
        print("Merging:", left, right)
        return array


# creating a main function which is the main which allows for the array to be inputed by a user
def main():
    input_str = input("Please enter an array of n integers, separated by spaces: ")

    array = input_str.split()

    # converts every value from string to int
    for i in range(len(array)):
        array[i] = int(array[i])

    # prints orginal array and sorted array
    print("The original array is:", array)
    print()
    # calls function on array
    sorted_array = mergesort(array)
    print()
    print("The now sorted array is:", sorted_array)


if __name__ == "__main__":
    main()

