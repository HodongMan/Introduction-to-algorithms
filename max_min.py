def Minimum(a):
	m = a[1]
	for i, num in enumerate(a):
		if m > num:
			m = num
	return m