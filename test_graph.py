from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


# def randrange(n, vmin, vmax):
#     '''
#     Helper function to make an array of random numbers having shape (n, )
#     with each number distributed Uniform(vmin, vmax).
#     '''
#     return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)


# f = open("./output.txt", "r")
xs = []
ys = []
zs = []

# if f.readline() is not None:
# 	print("hyhhh")

with open("./test_final.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [line.strip() for line in content]

i = 0
new_content = []
for line in content:
	tx,ty,tz = line.split('\t')
	# print(tx,ty,tz)
	xs.append(float(tx))
	ys.append(float(ty))
	zs.append(float(tz))
	i += 1
	# if i == 100:
	# 	break

print(i)

# i = 0
# while i <= len(content) - 2:
# 	xs.append(content[i])
# 	ys.append(content[i+1])
# 	zs.append(content[i+2])
# 	i += 3

xs = np.array(xs)
ys = np.array(ys)
zs = np.array(zs)

ax.scatter(xs, ys, zs, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.title('The 3D point generated from VINS-MONO')

print("cp")

plt.show()
