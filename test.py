from universe import Universe

U = Universe()

a = U.get_planet(-32, 4864)

print(a)

# change for git test

'''
G = 6.67408e-11     # Universal Gravitational Constant

# Mars
M = 6.39e23         # Kg
r = 3390000         # meters

g = round((G * (M / (r**2))), 2)
print(g)

# Earth
M = 5.972e24        # Kg
r = 6371000         # meters

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
'''
