distance_mi = 2
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1 and is_raining == False: 
    print(True)
  
elif distance_mi > 1 and distance_mi <= 6 and has_bike and is_raining == False:
    print(True)

elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(True) 

else:
    print(False)            



