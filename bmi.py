def calculate_bmi(height,weight):
    print("Height = "+str(height))
    print ("Weight = "+str(weight))
    bmi=weight/(height*height)
    print(f"BMI value= ",round(bmi,2))
    if bmi< 18.5:
        print("Under weight")
        return -1
    elif bmi>25.0:
        print("Over weight")
        return 1 
    else:
        print("Normal weight")
        return 0
calculate_bmi(weight=37,height=1.73)
