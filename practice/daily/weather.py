temperature = int(input())
humidity = int(input())

if temperature < 15 and humidity > 60:
	print ( "Chilly,jacked needed")

elif temperature >= 30 and humidity < 30:
	print("Dry hot,grab an umbrella")


elif temperature >= 20 and temperature <= 30 and humidity >= 35 and humidity <= 50:
	print("fresh,perfect for shorts")

elif temperature >= 30 and temperature <= 40 and humidity >= 50 and humidity <= 70:
	print("Warm,wear light clothes")

else:
	print("Normal weather,wear anything you like") 

