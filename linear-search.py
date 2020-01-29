# Linear search is a very simple search algorithm. In this type of search, a sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.


def linear_search(array,len,search):
	for index in range(0,len):
		if(array[index] == search):
			return index

	return -1

array = [2,4,6,3,90,7]
search = 90
n = len(array)
result = linear_search(array,n,search)
if(result == -1):
	print("Element is not present in the Array")
else:
	print("Element is present at index : ",result)