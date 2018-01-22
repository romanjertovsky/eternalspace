"""

from universe import Universe


U = Universe()

for i in range(10):
    a = U.get_planet(i*1000, i*11)
    print(a)

"""

G = 6.67408e-11     # Universal Gravitational Constant

# Earth
M = 5972000000000000000000000        # Kg
r = 6371000         # meters

g = round((G * (M / (r**2))), 2)
print('g: {0}'.format(g))
print('M: {0} Yg'.format(M / 1e21))

print('========')
# Mars
M = 639000000000000000000000         # Kg
r = 3390000         # meters

g = round((G * (M / (r**2))), 2)
print(g)


# Moon
M = 0.07350e24      # Kg
r = 1737000         # meters

g = round((G * (M / (r**2))), 2)
print(g)

# Jupiter
M = 1.8986e27        # Kg
r = 69911000        # meters

g = round((G * (M / (r**2))), 2)
print(g)

# Saturn
M = 5.683e26        # Kg
r = 58232000        # meters

g = round((G * (M / (r**2))), 2)
print(g)
