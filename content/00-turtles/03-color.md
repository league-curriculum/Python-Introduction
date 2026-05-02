---
title: 'Colors'
uid: hoMRN9Qf
---

## Student Content

<!-- curik:body:start -->
Tina can change into lots of colors!  We can tell her to change into blue by typing `tina.color("blue")`.  

Click run to see:


{{< trinket >}}
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.left(90)
tina.forward(20)
tina.write("What color am I now?")

tina.forward(20)
tina.color("blue")
tina.write("What color am I now?")

tina.forward(20)
tina.color("purple")
tina.write("What color am I now?")

tina.forward(20)
tina.color("green")
tina.write("What color am I now?")
{{< /trinket >}}

Each color segment in the picture is created by three lines of code:

```python
tina.forward(20)
tina.color("blue")
tina.write("What color am I now?")
```

Add two more colors to her list by adding another three lines like this but with `"blue"` replaced with your favorite color.  `"pink"`? `"yellow"`? `"cyan"`?  It's up to you.



---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.
<!-- curik:body:end -->

{{< instructor-guide >}}

Instructor guide content goes here.

{{< /instructor-guide >}}
