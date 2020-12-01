import turtle
k = turtle.Turtle()
k.penup()
k.goto(-170,100)
k.pensize(10) #kalemin boyutunu ayarladik
k.pendown()
k.pencolor("blue") #kalemin rengini ayarladik
k.circle(70)


k.penup()
k.pencolor("yellow")
k.goto(-90,20)
k.pendown()
k.circle(70)  #burada 70 birimlik bir daire çizdirdik


k.penup()
k.pencolor("black")
k.goto(-10,100)  #istenilen noktaya gitmesini sagladik.
k.pendown()  
k.circle(70)


k.penup()
k.pencolor("green")
k.goto(70,20)
k.pendown()
k.circle(70)


k.penup()
k.pencolor("red")
k.goto(150,100)
k.pendown()
k.circle(70)

mainloop()

