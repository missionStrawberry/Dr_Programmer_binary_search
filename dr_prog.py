def bin_search(arr, high, low, key):
	while low <= high:
		mid = (low + high) / 2
		if arr[mid] < key:
			low = mid + 1
		elif a[mid] > key:
			high = mid - 1
		else:
			return mid
		return -1

def query_a(q):
	Z = int(q[0])
	XL = int(q[2])
	XR = int(q[3])
	
	min = bin_search(x_pts, N - 1, 0, XL)
	max = bin_search(x_pts, N - 1, 0, XR)
	
	

inp = input()
in_ar = inp.split(" ")
N = int(in_ar[0])
M = int(in_ar[1])
Q = int(in_ar[2])

inp2 = input()
in_ar2 = inp2.split(" ")
x_pts = []
for i in range(N):
	x_pts.append(int(in_ar2[i]))
x_pts.sort()
print(x_pts)
	
inp3 = input()
in_ar3 = inp3.split(" ")
y_pts = []
for i in range(M):
	y_pts.append(int(in_ar3[i]))	
y_pts.sort()
print(y_pts)

for i in range(Q):
	inp_q = input()
	in_arq = inp_q.split(" ")
	
	