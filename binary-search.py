# Binary search is the search technique which works efficiently on the sorted lists. Hence, in order to search an element into some list by using binary search technique, we must ensure that the list is sorted.


def binarySearch(array,left,right,search):
	if(left <= right):
		mid = left+(right-1)//2

		if(array[mid] == search):
			return mid
		elif(array[mid] > search):
			return binarySearch(array,left,mid-1,search)
		else:
			return binarySearch(array,mid+1,right,search)
	else:
		return -1

array = [3,5,7,20,22]
search= 20
result = binarySearch(array,0,len(array)-1,search)
if(result == -1):
	print('Element is not present in array')
else:
	print("Element is present at index : ",result)