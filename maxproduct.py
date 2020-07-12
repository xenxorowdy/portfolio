def max_pair(n):
	max_pro = 0
	
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			max_pro = max(max_pro,n[i]*n[j])
	return max_pro
	
	
n = int(input())	
m = list(map(int,input().split()))
print(max_pair(m))
	