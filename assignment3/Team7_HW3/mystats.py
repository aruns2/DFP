#Team 7
#Arun Sharma : aruns2@andrew.cmu.edu
#Yuxi Wang: yuxiwang@andrew.cmu.edu
# File: mystats.py
import numpy as np
# define the mean function here

def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter
v1 = {1, 2, 3}     # a set is iterable
print(v1, "is iterable:", is_iter(v1))
v2 = 123
print(v2, "is iterable:", is_iter(v2))

    
def mean(*args):
    t=0
    keys=range(len(args))
    l=0
    t2=0
    l2=0
    l3=[]
    if len(args)>0:
        for i in keys:
            if is_iter(args[i])==True:
                t=sum(args[i])
                l += len(args[i])
            else:
                l3.append(i)
                t2 += args[i]
                l2=len(l3)
        return (t + t2)/(l + l2)
    else:
        return 'FAIL'

# define the stddev function here

def stddev(*args):
    t3=[]
    t4=[]
    m=mean(*args)
    total=0
    l4=0
    keys2=range(len(args))
    lens4=[]
    total1=0
    Lens4=0
    if len(args)>=1:
        for i in keys2:
            if is_iter(args[i])==True:
                for v in args[i]:
                    t3.append(v)
                for x in t3:
                    t4.append((x-m)**2)
                lensg=len(args[i])
                total=sum(t4)
                l4 += lensg
            else:
                lens4.append(i)
                t += (args[i]-m)**2
                l4=len(lens4)
        return ((total+total1)/((l4+Lens4)-1))**0.5
    else:
        return 'FAIL'

# define the median function here

def median(*args):
    wu=[]
    liu=[]
    Lens4=0
    keys=range(len(args))
    l5=[]
    if len(args)>=1:
        for i in keys:
            if is_iter(args[i])==True:
                for v in args[i]:
                    wu.append(v)
                lens4=len(args[i])
            else:
                l5.append(i)
                Lens6=len(l5)
                liu.append(args[i])
        qi=wu+liu
        qi.sort()
        lens7=len(qi)
        if lens7 % 2==0:
            med=int(lens7/2)
            return (qi[med-1]+qi[med])/2
        else:
            med1=int((lens7+1)/2)
            return qi[med1-1]
    else:
        return 'FAIL'


# define the mode function here

def mode(*args):
	final_dict = {}
	for num in args:
		try:
			for i in num:
				if i in final_dict.keys():
					final_dict[i] += 1
				else:
					final_dict[i] = 1
		except:
			if num in final_dict.keys():
				final_dict[num] += 1
			else:
				final_dict[num] = num
		
	return(tuple(([x for x in final_dict.keys() if final_dict[x] == max(final_dict.values())])))
    
if __name__ == '__main__':
# part (a)
  print('The current module is:', __name__)

# part (b)

  print('mean(1) should be 1.0, and is:', mean(1))
  print('mean(1,2,3,4) should be 2.5, and is:', mean(1,2,3,4))
  print('mean(2.4,3.1) should be 2.75, and is:',mean(2.4,3.1))
  print('mean() should FAIL:', mean())

# part (c)

  print('mean([1,1,1,2]) should be 1.25, and is:', mean([1,1,1,2]))
  print('mean((1,), 2, 3, [4,6]) should be 3.2,' + 'and is:', mean((1,), 2, 3, [4,6]))

# part (d)

  for i in range(10):
      print("Draw", i, "from Norm(0,1):", np.random.randn())

  ls50 = [np.random.randn() for i in range(50)]
  print("Mean of", len(ls50), "values from Norm(0,1):", mean(ls50))

  ls10000 = [np.random.randn() for i in range(1000)]
  print("Mean of", len(ls10000), "values from " + "Norm(0,1):", mean(ls10000))

# part (e)

  np.random.seed(0)
  a1 = np.random.randn(10)

  print("a1:", a1)
  print("the mean of a1 is:", mean(a1))

# part (f)

  print("the stddev of a1 is:", stddev(a1))

# part (g)
  print("the median of a1 is:", median(a1))
  print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))
# part (h)
  print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:", mode(1, 2, (1, 3), 3, [1, 3, 4]))
 

