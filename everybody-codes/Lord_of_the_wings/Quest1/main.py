import bisect
import sys

if sys.argv[2] == "1":
    sqrs = [i*i for i in range(1, 1000+1)]
elif sys.argv[2] == "2":
    sq_frame = lambda i, n: n - (i - 2) * (i - 2)
    sqrs = [sq_frame(i, i*i) for i in range(3, 10000+1)]
else: 
    sqrs = [i*i-1 for i in range(3, 10000000) if i*i%2 != 0]

with open(sys.argv[1]) as f:
    outposts = f.read().strip().split(',')

outposts = list(map(int, outposts))
must_collct = []
for i, ench_cones in enumerate(outposts):
    ench_cones = int(ench_cones)
    idx = bisect.bisect_left(sqrs, ench_cones)
    closest_sqr = 0

    if idx == 0:
        closest_sqr = sqrs[0]
    elif idx == len(outposts):
        closest_sqr = sqrs[outposts[len(outposts) - 1]]
    else:
        closest_sqr = sqrs[idx]

    must_collct.append((closest_sqr - ench_cones))

print(sum(must_collct))