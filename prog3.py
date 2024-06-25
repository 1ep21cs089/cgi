from vpython import canvas, box, cylinder, vector, color, rate, radians

# Create a 3D canvas
scene = canvas(width=800, height=600, background=color.white)

# Define a function to draw a cuboid
def draw_cuboid(pos, length, width, height, color):
    cuboid = box(pos=vector(*pos), length=length, width=width, height=height, color=color)
    return cuboid

# Define a function to draw a cylinder
def draw_cylinder(pos, radius, height, color):
    cyl = cylinder(pos=vector(*pos), radius=radius, length=height, color=color)
    return cyl

# Define a function to translate a 3D object
def translate(obj, dx, dy, dz):
    obj.pos += vector(dx, dy, dz)

# Define a function to rotate a 3D object
def rotate(obj, angle, axis):
    obj.rotate(angle=angle, axis=vector(*axis), origin=obj.pos)

# Define a function to scale a 3D object
def scale(obj, sx, sy, sz):
    obj.size = vector(obj.size.x * sx, obj.size.y * sy, obj.size.z * sz)

# Draw a cuboid
cuboid = draw_cuboid((-2, 0, 0), 2, 2, 2, color.blue)

# Translate the cuboid
translate(cuboid, 4, 0, 0)

# Rotate the cuboid
rotate(cuboid, angle=radians(45), axis=(0, 1, 0))

# Scale the cuboid
scale(cuboid, 1.5, 1.5, 1.5)

# Draw a cylinder
cyl = draw_cylinder((2, 2, 0), 1, 1, color.red)

# Translate the cylinder
translate(cyl, 0, -2, 0)

# Rotate the cylinder
rotate(cyl, angle=radians(30), axis=(1, 0, 0))

# Scale the cylinder
scale(cyl, 1.5, 1.5, 1.5)

# Animation loop to keep the 3D scene interactive
while True:
    rate(30)  # Set the frame rate to 30 frames per second
