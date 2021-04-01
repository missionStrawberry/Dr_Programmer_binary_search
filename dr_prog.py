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
	
inp3 = input()
in_ar3 = inp3.split(" ")
y_pts = []
for i in range(M):
	y_pts.append(int(in_ar3[i]))	
y_pts.sort()

for i in range(Q):
    inp_q = input()
    q = inp_q.split(" ")


    Z = int(q[0])
    XL = 0
    XR = 10**13
    YL = 0
    YR = 10**13

    
    if q[1] == "A" or q[1] == "C":
        XL = int(q[2])
        XR = int(q[3])
        
    if q[1] == "C":
        YL = int(q[4])
        YR = int(q[5])
    elif q[1] == "B":
        YL = int(q[2])
        YR = int(q[3])

    

    counter = 0
    for j in x_pts:
        if j >= XL and j <= XR:
            for l in y_pts:
                if (j + l) <= Z and l >= YL and l <= YR:
                    counter += 1
        
    print(counter)
	
	