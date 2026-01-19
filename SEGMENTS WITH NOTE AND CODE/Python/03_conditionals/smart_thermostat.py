device_status = "active"

temp = 38

if device_status=="active":
    if temp>35:
        print(f"high temp alert!")
    else:
        print(f"Temp is normal!")
else:
    print(f"device is offline!")