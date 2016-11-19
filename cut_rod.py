
def MemorizeCutRod(p, n):
	r = list()
	for i in range(0, n):
		r[i] = -10000
	return MemorizeCutRodAux(p, n, r)


def MemorizeCutRodAux(p, n, r):
	if r[n] >= 0:
		return r[n]
	if n == 0:
		q = 0
	else:
		q = -10000
		for i in range(0, n):
			q = max(q, p[i] + MemorizeCutRodAu(p, n -i, r))
	r[n] = q
	return q

def BottomUpCutRod(p, n):
	r = list()
	r[0] = 0
	for j in range(0, n):
		q = -10000
		for i in range(0, n):
			q = max(q, p[i] + r[j-i])
		r[j] = q
	return r[n]
