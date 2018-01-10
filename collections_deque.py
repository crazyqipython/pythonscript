import collections
import threading
import time
import random


d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)

d1 = collections.deque()
d1.extend('abcdefg')
print('extend  :', d1)
d1.append('h')
print('append  :', d1)


# Add to the left

d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft :', d2)
d2.appendleft(6)
print('appendleft:', d2)


print('From the right:')
d = collections.deque('abcdefg')
while True:
	try:
		print(d.pop(), end='')
	except IndexError:
		break
print()

print('\nFrom the left:')
d = collections.deque(range(6))
while True:
	try:
		print(d.popleft(), end='')
	except IndexError:
		break
		
print()

candle = collections.deque(range(5))

def burn(directions, nextSource):
	while True:
		try:
			next = nextSource()
		except IndexError:
			break
		else:
			print('{:>8}: {}'.format(directions, next))
	print('{:>8} done'.format(directions))
	return
	
left = threading.Thread(target=burn,
						args=('Left', candle.popleft))
right = threading.Thread(target=burn,
						args=('Right', candle.pop))
	
right.start()	
left.start()


left.join()
right.join()

d = collections.deque(range(10))
print('Normal :', d)

d = collections.deque(range(10))
d.rotate(2)
print('Right rotation:', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Left rotation:', d)

# Set the random seed so we see the same output each time
# the script is run
random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(5):
	n = random.randint(0, 100)
	print('n=', n)
	d1.append(n)
	d2.appendleft(n)
	print('D1:', d1)
	print('D2:', d2)