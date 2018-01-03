import random
import copy
puzzle = [[None,None,6,None,None,None,None,None,None],\
	[None,None,None,None,None,3,5,None,9],\
	[None,None,None,None,8,None,2,None,None],\
	[None,None,None,None,None,None,None,3,7],\
	[7,None,None,None,5,9,None,None,None],\
	[None,None,None,2,None,None,9,None,None],\
	[2,7,None,None,4,None,3,None,None],\
	[None,4,None,6,None,None,None,5,None],\
	[None,6,None,3,1,None,None,9,None]]
valid = [x+1 for x in range(len(puzzle[0]))]
def check_valid(pzl):
	pzl2 = copy.deepcopy(pzl)
	tried = []
	while any(None in sub for sub in pzl2):
		pzl2 = copy.deepcopy(pzl)
		for ri, row in enumerate(pzl2):
			for ci, cell in enumerate(row):
				if not cell == None:
					continue
				random.shuffle(valid)
				#print valid
				for i in valid:
					#check row
					if i in row:
						continue
					#check col
					if i in [x[ci] for x in pzl2]:
						continue
					#check square
					mr = ri//3
					mr *= 3
					mxr = ri//3 + 1
					mxr *= 3
					mc = ci//3
					mc *= 3
					mxc = ci//3 + 1
					mxc *= 3
					sqr = [x[mc:mxc] for x in pzl2[mr:mxr]]
					fltsqr = []
					for y in sqr:
						fltsqr += y
					if i in fltsqr:
						continue
					#if all else succeeds? add:
					pzl2[ri][ci] = i
		if pzl2 not in tried:
			tried.append(pzl2)
			for r in pzl2:
				print r
			print
	return pzl2
p = check_valid(puzzle)
print "Solution: "
print
for r in p:
	print r
print
