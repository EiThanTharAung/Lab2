print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu(): 
    print("display_main_menu") 
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
def calc_average(stringlist):
    print("calc_average")
    total=0
    for eachstr in stringlist:
        total=total+float(eachstr)
    average=total/len(stringlist)
    return average

def get_user_input():
    print("get_user_input")
    inputstr=input()
    strlist=inputstr.split(",")
    print(strlist)
    return strlist
def find_min_max(stringlist):
    print("find_min_max")
    floatlist=[]
    for eachstr in stringlist:
        floatlist.append(float(eachstr))
    floatlist.sort()
    return(floatlist[0],floatlist[-1])




def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")

def main(): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    temp_list = get_user_input()
    calc_average(temp_list)
    find_min_max(temp_list)

if __name__ == "__main__": 
    main() 