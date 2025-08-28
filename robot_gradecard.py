#Robot Grade Card:


#Task 1: Obstacle Avoidance

proximity = 10  
obstacle_Task = "" 

while proximity > 2:
    proximity -= 2
    print("Moving forward... Proximity:", proximity)

    if proximity <= 2:
        print("Obstacle detected! Stopping")
        obstacle_Task = "Stopped by obstacle"
        break


    else:
        obstacle_Task = "Completed"

print("Obstacle Task Result:",obstacle_Task)


#Task 2: Target Approach

distance = 20
speed = 10
target_Task = " "

while distance > 0:
    
    distance -= speed


    if distance <= 0:
        target_Task = "completed"
        print("Target reached!", target_Task)
        break


    elif distance <= 2:
        print("Target very close! Slowing down")

    else:
         print("Approaching target... distance left: ",distance)

print("target_Task result: ",target_Task)
   
#Task 3: Package Delivery
packages = 5
battery = 100
task_status = " "

while packages > 0 and battery > 30:
    packages -= 1
    battery  -= 15
    print(f"Package delivered. Remaining: {packages}, Battery: {battery}%")

    if packages == 0:
       task_status = "completed"
    else:
        task_status = "Stopped (Battery low)"

print("the package delivery has been ", task_status)

#Task 4: Temperature Monitoring
tempt = 40
Warning = 70
task_tempt =" "

while tempt < 100:
    tempt += 15
    if tempt < Warning:
        print("Temperature normal:", tempt)
        task_tempt = "normal"

    elif Warning <= tempt < 100:
        print("Warning! High temperature: ",tempt)
        task_tempt = "warning"

    else:
        print("Critical temperature! Shutting down")
        task_tempt = "critical"
        break

print("task status :", task_tempt)


results = {
    "Obstacle Task": obstacle_Task,
    "Target Task": target_Task,
    "Delivery Task": task_status,
    "Temperature Task": task_tempt}



print("-----------------------------------------------")
print("              ROBOT GRADE CARD                 ")   
print("-----------------------------------------------")
for task, status in results.items():
    print(f"{task:20}: {status}")
print("-----------------------------------------------")