import copy
import os
from multiprocessing import *
threadct = 0
maxthreadct = 1
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
	global threadct
	global maxthreadct
	if not any(None in sl for sl in pz):
		print("true")
		return pz
	#puzzle, values list, current iteration, max iteration
	p = copy.deepcopy(pz)
	print
	puzzle_print(p)
	if n == m:
	    return p
	indx, indy = _2dIndex(p, None)
	vld = [i for i in v if valid_move(p,indx,indy,i)]
	if len(vld) == 0 and any(None in sl for sl in p):
		print("false")
		return False
	for i in vld:
		p[indx][indy] = i
		if threadct < maxthreadct:
			threadct += 1
			tpool.apply_async(check, args=(p,v,n+1,m), callback=done)
		else:
			w = check(p,v,n+1,m)
			if w == False:
				continue
			else:
				print("true")
				done(w)
	print("false")
	return False
dn = False
def done(p):
    if type(p) is list:
    	tpool.terminate()
    	puzzle_print(p)
    	print "Solved"
    	dn = True
    	quit()
if maxthreadct > 0:
	tpool = Pool(maxthreadct)
else:
	tpool = Pool(1)
def solve(p):
    valid = [x+1 for x in range(len(p[0]))]
    count = sum(n.count(None) for n in p)
    print count
    check(p,valid,0,count)

solve(puzzle)
while dn == False:
	pass
