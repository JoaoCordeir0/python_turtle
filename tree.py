import turtle

t = turtle.Turtle()
t.screen.bgcolor('black')

t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(200)
t.shape('turtle')

def tree(index):
    if index < 10:
        return
    else:
        t.forward(index)
        t.color('orange')
        t.circle(2)
        t.color('brown')
        t.left(30)
        tree(3*index/4)
        t.right(60)
        tree(3*index/4)
        t.left(30)
        t.backward(index)

tree(100)
turtle.done()