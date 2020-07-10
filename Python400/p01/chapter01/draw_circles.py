import turtle

# 为了更美观调整画笔尺寸
turtle.pensize(5)

# 绘制第一个圆形
turtle.penup()
turtle.goto(-60, 0)
turtle.pendown()
turtle.color("blue")
turtle.circle(50)

# 绘制第二个圆形
turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
turtle.color("black")
turtle.circle(50)

# 绘制第三个圆形
turtle.penup()
turtle.goto(160, 0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

# 绘制第四个圆形
turtle.penup()
turtle.goto(-5, -50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

# 绘制第五个圆形
turtle.penup()
turtle.goto(105, -50)
turtle.pendown()
turtle.color("green")
turtle.circle(50)
