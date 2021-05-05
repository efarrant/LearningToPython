distance_km = input("1st April 2021: Please enter distance in km:  ")

distance_mi = float(distance_km) * 0.6214

duration = input("Please enter time taken in minutes, as a decimal. (e.g. 61 minutes and 15 seconds = 61.25) ")
pace = float(duration) / float(distance_mi)
minutes = int(pace)
seconds = 60 * (pace - int(pace))
miles_left = 100 - (distance_mi)
print("Your pace today was: " , minutes,":",int(seconds),"min/mi, which means", minutes , "minutes and ", round(seconds,2) , "seconds per mile")
print("You ran" , round(distance_mi, 2) , "miles." , "You have" , miles_left ,"miles left of your 100 mile target")
print(f"{minutes}:{int(seconds)} min/mi")
if float(distance_km) > 4.9:
    print ("Woo!")
April_1 = distance_mi

distance_km = input("5th April 2021: Please enter distance in km:  ")
distance_mi = float(distance_km) * 0.6214
miles_left = 100 - (distance_mi) - April_1
print("You have" , miles_left ,"miles left of your 100 mile target")
if float(distance_km) > 4.9:
    print ("Woo!")
April_5 = distance_mi + April_1

distance_km = input("6th April 2021: Please enter distance in km:  ")
distance_mi = float(distance_km) * 0.6214
miles_left = 100 - (distance_mi) - April_5
print("You have" , miles_left ,"miles left of your 100 mile target")
if float(distance_km) > 4.9:
    print ("Woo!")
April_6 = distance_mi + April_5


