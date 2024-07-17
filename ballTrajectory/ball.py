import matplotlib.pyplot as plt

def ball_trajectory(x):
  vx = 0.99
  vy = 9.9
  a = -9.81
  #position = ((vy / vx) * x ) + ((a / 2 * vx**2)*(x**2))
  position = 10*x - 5*(x**2)
  return(position)

xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]
xs2 = [0.1, 2]
ys2 = [ball_trajectory(0.1),0]
xs3 = [0.2, 2]
ys3 = [ball_trajectory(0.2),0]
xs4 = [0.3, 2]
ys4 = [ball_trajectory(0.3),0]
xs5 = [0.3, 0.3]
ys5 = [0, ball_trajectory(0.3)]
xs6 = [0.3, 2]
ys6 = [0,0]
plt.plot(xs, ys, xs4, ys4, xs5, ys5, xs6, ys6)
plt.title('Ball trajectory with sight lines, tangent calculation')
plt.xlabel('Horizontal position')
plt.ylabel('Vertical position')
plt.text(0.31, ball_trajectory(0.3)/2, 'A', fontsize=16)
plt.text((0.3 + 2)/2,0.05, 'B', fontsize=16)
#plt.axhline(y=0)
plt.show()