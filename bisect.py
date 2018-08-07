import scipy.optimize
def bisect(f, a, b, tol=1e-11, n=100):
	fmt = '{:2} {:>13.10f} {:>13.10f} {:>13.10f} {:>13.10f}'
	i=1
	while abs(a-b) > tol and i <= n:
		p = a + (b-a)/2.0
		print fmt.format(i, a,b,p,f(p))
		if f(a) * f(p) < 0:
			b =p
		else:
			a =p
		i += 1
	return p

def f(x):
	return x**3 + 4* x**2 -10

if __name__ == '__main__':
	r1 = bisect(f,1,2)
	print ' root = {:.10f}'.format(r1)
	r2 = scipy.optimize.bisect(f,1,2,xtol=1e-11)
	print 'root = {:.10f}'.format(r2)
