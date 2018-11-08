import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(7, GPIO.IN)



while(1):
	if GPIO.input(12):
			print("input 1 OK")
	if GPIO.input(5):
			print("input 2 OK")
	if GPIO.input(3):
			print("input 3 OK")
	if GPIO.input(7):
			print("input 4 OK")
