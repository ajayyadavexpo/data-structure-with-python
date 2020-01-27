# Insertion sort works in the similar way as we sort cards in our hand in a card game.

# We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put at their right place.

# A similar approach is used by insertion sort.

# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
def insertionSort(array):
	for step in range(1,len(array)):
		key = array[step];
		j = step-1
		while j>=0 and key < array[j]:
			array[j+1] = array[j]
			j = j-1

		array[j+1] = key



data = [3,4,1,2,8]
insertionSort(data)
print("Sorted Data : ",data)