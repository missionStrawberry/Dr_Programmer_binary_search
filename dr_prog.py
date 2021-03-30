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

inp3 = input()
in_ar3 = inp3.split(" ")
y_pts = []
for i in range(M):
	y_pts.append(int(in_ar3[i]))


for i in range(Q):

	