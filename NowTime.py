import turtle, time

turtle1 = turtle.Turtle()

turtle1.up()


enableHour = turtle.textinput('Часы(T/F)', '')


screen = turtle.Screen()
screen.setup(450, 450)

turtle.title('Time now')
    

while True:
    time.sleep(0.1)
    turtle.clearscreen()

    nowtime = [str(time.localtime().tm_hour), str(time.localtime().tm_min), str(time.localtime().tm_sec)]
    tmp = None

    for i in range(0, 3):
        if int(nowtime[i]) < 10:
            tmp = nowtime[i]
            nowtime.pop(i)
            nowtime.insert(i, "0" + tmp)

    if enableHour.lower() == 't':
        turtle1.write(f"{nowtime[0]}:{nowtime[1]}:{nowtime[2]}", False, 'center', font = ('Arial', 56))

    elif enableHour.lower() == 'f':
        turtle1.write(f"{nowtime[1]}:{nowtime[2]}", False, 'center', font = ('Arial', 56))

    else:
        turtle1.pencolor('red')
        turtle1.write('Error', False, 'center', font = ('Arial', 56))
        break

    #turtle1.clear()
    
turtle.exitonclick()