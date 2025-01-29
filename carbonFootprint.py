def carbonFootprint(modeOfTransport,distance,fuel):
    modeOfTransport=modeOfTransport.lower()
    if (modeOfTransport == "electric car" or modeOfTransport=="bicycle"):
        print("your carboon foot print is : 0")
    elif(modeOfTransport=="gasoline car"):
        carbonfootprint= distance * fuel
        print("your carbon foot print is :{0}".format(carbonfootprint))
    else: print("Unknown mode of transportation")
print("change is coming")
carbonFootprint("car",20,30)