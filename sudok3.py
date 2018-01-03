import copy
import os
import multiprocessing
dn = False
tpool = multiprocessing.Pool(3)
puzzle = [[None,None,6,None,None,None,None,None,None],\
	[None,None,None,None,None,3,5,None,9],\
	[None,None,None,None,8,None,2,None,None],\
	[None,None,None,None,None,None,None,3,7],\
	[7,None,None,None,5,9,None,None,None],\
	[None,None,None,2,None,None,9,None,None],\
	[2,7,None,None,4,None,3,None,None],\
	[None,4,None,6,None,None,None,5,None],\
	[None,6,None,3,1,None,None,9,None]]

def puzzle_print(p):
	os.system('cls' if os.name == 'nt' else 'clear')
	for ri,r in enumerate(p):
		if (ri % 3) == 0:
			print " ----------------------"
		for ci, c in enumerate(r):
			if (ci % 3) == 0:
				print "|",
			if c == None:
				print "*",
			else:
				print c,
		print "|",
		print
	print " ----------------------"
def _2dIndex(l,i,o=0):
	counter = 0
	for ri,r in enumerate(l):
		for ci,c in enumerate(r):
			if c == i:
				if counter == o:
					return (ri, ci)
				else:
					counter += 1

def valid_move(p,x,y,i):
	row = p[x]
	if i in row:
		return False
	#check col
	if i in [r[y] for r in p]:
		return False
	#check square
	mr = x//3
	mr *= 3
	mxr = x//3 + 1
	mxr *= 3
	mc = y//3
	mc *= 3
	mxc = y//3 + 1
	mxc *= 3
	sqr = [r[mc:mxc] for r in p[mr:mxr]]
	fltsqr = []
	for y in sqr:
		fltsqr += y
	if i in fltsqr:
		return False
	return True

def check(pz,v,n,m):
	#puzzle, values list, current iteration, max iteration
	p = copy.deepcopy(pz)
	puzzle_print(p)
	if n == m:
		return p
	indx, indy = _2dIndex(p, None)
	for i in v:
		if valid_move(p,indx,indy,i):
			p[indx][indy] = i
			w = check(p,v,n+1,m)
			if w == False:
				continue
			else:
				return w
	return False

def done(p):
	tpool.terminate()
	puzzle_print(p)
	print "Solved"
	dn = True
	quit()
def solve(p):
	valid = [x+1 for x in range(len(p[0]))]
	count = sum(n.count(None) for n in p)
	indx, indy = _2dIndex(p, None)
	for i in valid[::-1]:
		if valid_move(p,indx,indy,i):
			pz = copy.deepcopy(p)
			pz[indx][indy] = i
			tpool.apply_async(go, args=(pz,valid,count), callback=done)
def go(p,valid,count):
	x = check(p,valid,1,count)
	while x == False:
		x = check(p,valid,1,count)
	return x

solve(puzzle)
while dn == False:
	pass
