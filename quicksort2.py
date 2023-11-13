def partition(arr,low,high):
	pivot = arr[high]
	j=low -1 
	#Assuming starting from position j+1, all values were greater than pivot.
	#If the current value is not geater, swap position j+1 and current position, update j
	for i in range(low,high+1):
		if arr[i] <= pivot:
			j = 1 + j
			arr[j],arr[i] = arr[i], arr[j]
	return j

def qsort(arr,low,high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr,low,high)
		qsort(arr,low,pi-1)
		qsort(arr,pi+1,high)

#test
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
qsort(arr, 0, n-1)
print("Sorted array is:")
print(arr)