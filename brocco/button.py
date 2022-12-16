import RPi.GPIO as GPIO

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 16 as an input pin
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define a function to be called when the button is pressed
def button_pressed(channel):
    print("Hi")



# Create an infinite loop to keep the program running
try:
    while True:
        # Set an event detector on pin 16 to trigger the button_pressed function when the button is pressed
        GPIO.add_event_detect(16, GPIO.FALLING, callback=button_pressed, bouncetime=200)
finally:
    GPIO.cleanup()