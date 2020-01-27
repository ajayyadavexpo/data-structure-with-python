# Bubble sort is an algorithm that compares the adjacent elements and swaps their positions if they are not in the intended order. The order can be ascending or descending.


def bubbleSort(array):
	n = len(array)
	for i in range(0,n):
		for j in range(0,n-i-1):
			if(array[j]> array[j+1]):
				# swap the element
				(array[j],array[j+1]) = (array[j+1],array[j])



array = [3,5,7,2,1]
bubbleSort(array)
print("Sorted array : ",array)
		