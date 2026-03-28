# Decision Tree Logic for Playing Outside
print("--- Activity Decision Maker ---")

weather = input("Is it sunny, rainy, or cloudy? ").strip().lower()

if weather == "sunny":
    hot = input("Is it too hot? (yes/no): ").strip().lower()
    if hot == "yes":
        print("Result: Do not play outside (Risk of heatstroke).")
    else:
        print("Result: Play outside! It's a great day.")
        
elif weather == "rainy":
    heavy_rain = input("Is it raining heavily? (yes/no): ").strip().lower()
    if heavy_rain == "yes":
        print("Result: Do not play outside (Stay dry!).")
    else:
        print("Result: You can play if you have a raincoat.")
        
elif weather == "cloudy":
    print("Result: Play outside! The weather is perfect.")
    
else:
    print("Result: Unknown weather condition. Stay safe indoors.")