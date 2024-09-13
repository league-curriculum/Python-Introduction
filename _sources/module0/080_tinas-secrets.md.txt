# Tina's Secrets

You might think you know a lot about Tina, but Tina actually has a lot of
secrets. However, they are not very secret, because someone wrote them all down, in
the [Python Turtle Documentation](https://docs.python.org/3.8/library/turtle.html).

If you want to know everything that Tina can do, you should read the
documentation, but here are some of the most interesting things, with links to
parts of the documentation. 

## Circles

See the <a href="https://docs.python.org/3.8/library/turtle.html#turtle.circle" target="_blank">documentation for the `.circle()` function</a>.

The `.circle()` function can make a lot of diferent shapes, because it doesn't
really draw a circle; it draws a polygon with a lot of sides and a hecatontagon
( thats a shape with 100 sides, obviously! ) looks a lot like a circle.  You can
set the number of sides with the `steps=` parameters. You can also set how far
Tina moves around the circle with the `extent=` parameter.


With `steps=6` you can draw a hexagon:

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

#
# Draw a hexagon
#
tina.pendown()
tina.begin_fill()
tina.color('green')

tina.circle(130, steps=6)

tina.end_fill()
tina.penup()
tina.goto(30,-150)

```

And with `extent=180` you can draw a half circle:

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

#
# Draw half a circle
#

tina.penup()
tina.goto(30,-150)

tina.pendown()
tina.begin_fill()
tina.color('green')

tina.circle(130, extent=180)

tina.end_fill()
tina.penup()


```

You can use both `steps` and `extent` at the same time, to make a lot of different shapes. Try something
like `tina.circle(130, steps=3, extent=180)` to see what happens.

 ( Hmmm .... does steps have to be a whole number? What would a decimal number of steps, like 1.4,  do? )

## Heading

You can turn Tina with `.left()` and `.right()`, but you can also set the direction that Tina is facing with the `.setheading()` function. The half circle we did above could have been a smile, if we use `.setheading(90)` before drawing the circle.

See the <a href="https://docs.python.org/3.8/library/turtle.html#turtle.setheading" target="_blank">documentation for the .setheading() function</a>.

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

#
# Draw a smile
#

tina.penup()
tina.goto(-120,0)

tina.pendown()
tina.begin_fill()
tina.color('green')

tina.setheading(270)
tina.circle(130, extent=180)

tina.end_fill()
tina.penup()


```

## Towards

The `.towards()` function can be used to get the angle that Tina needs to turn to be facing another turtle. This can be useful if you want to make Tina follow another turtle.

See the <a href="https://docs.python.org/3.8/library/turtle.html#turtle.towards" target="_blank">documentation for the `.towards()` function</a>.

```python.run:height=400
import turtle
# First make Tina
tina = turtle.Turtle()
tina.shape('turtle')

# Then make Tony
tony = turtle.Turtle()
tony.shape('triangle')
tony.color('red')

tony.penup()
tony.setpos(-200,-150)
tony.pendown()

tina.penup()
tina.setpos(0,200)
tina.pendown()

for x in range(-200,200,10):
  
  tony.goto(x, -150) # Tony moves across bottom of screen
  
  # Get the angle Tina must face to be pointing at Tony
  heading = tina.towards(tony.xcor(), tony.ycor())

  # Turn tina towards Tony
  tina.setheading(heading)
  tina.forward(10) # Tina moves toward Tony

```

## Clicks and Keys


You can use the `.onclick()` function to make Tina do something when you click on the screen. You can also use the `.onkey()` function to make Tina do something when you press a key.

Here is a program that makes Tina move towards the place you click on the screen:

```python.run
import turtle

# First, make Tina
tina = turtle.Turtle()
tina.shape('turtle')

# Set up the screen
screen = turtle.Screen()

# Define the function that moves Tina towards the click
def move_tina(x, y):
    tina.setheading(tina.towards(x, y))
    tina.goto(x, y)

# Bind the click event to the move_tina function
screen.onclick(move_tina)


```

Here is an example of using `.onkey()` to make Tina move with the arrow keys:


```python.run
import turtle

# First, make Tina
tina = turtle.Turtle()
tina.shape('turtle')

# Set up the screen
screen = turtle.Screen()

# Define functions to move Tina in different directions
def move_up():
    tina.setheading(90)
    tina.forward(20)

def move_down():
    tina.setheading(270)
    tina.forward(20)

def move_left():
    tina.setheading(180)
    tina.forward(20)

def move_right():
    tina.setheading(0)
    tina.forward(20)

# Bind the arrow keys to the movement functions
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

```

### Run Away from Tony!

This program will make Tony follow Tina around the screen. You can use the arrow
keys to move Tina, and Tony will try to follow her. The left and right
arrows will turn Tina, and the up arrow will make her move forward. The down
arrow will make her turn around.

```python.run
import turtle

# First, make Tina
tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(9)

# Now, make Tony
tony = turtle.Turtle()
tony.shape('triangle')
tony.color('red')

# Set up the screen
screen = turtle.Screen()

# Define functions to control Tina
def move_forward():
    tina.forward(20)

def turn_left():
    tina.left(10)

def turn_right():
    tina.right(10)

def turn_around():
    tina.right(180)

# Function to move Tony towards Tina continuously
def move_tony():
    tony.setheading(tony.towards(tina.xcor(), tina.ycor()))
    tony.forward(5)
    # Call this function again after 100 milliseconds to keep Tony moving
    screen.ontimer(move_tony, 100)

# Start Tony's movement
move_tony()

# Bind the arrow keys to the movement functions
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(turn_around, "Down")


```