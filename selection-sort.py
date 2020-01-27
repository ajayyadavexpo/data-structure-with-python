# Selection sort is an algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.


def selectionSort(array):
	size = len(array)
	for step in range(size):
		min_index = step
		for element in range(min_index+1,size):
			if(array[element] < array[min_index]):
				min_index = element

		(array[step],array[min_index]) = (array[min_index],array[step])


data = [4,2,5,6,3]
selectionSort(data)
print("Sorted Data with selection sort : ",data)