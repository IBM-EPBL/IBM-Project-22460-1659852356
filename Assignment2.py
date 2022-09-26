import random
def buzzer(temperature):
    if temperature>20:
        print("buzzer-on")
    else:
        print("buzzer-off")

while(1):
    temperature=random.randint(10,99)
    humidity=random.randint(0,100)
    print(temperature)
    print(humidity)
    buzzer(temperature)
print("\n")
