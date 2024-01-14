#Barış Özçimenli - ID: 010210616
#Geo108E Term Project - Electrometric Tacheometry Computation


import math
print(">>>")
print("Program for Electrometric Tacheometry Computation")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

#Input part

Stationary = input("Enter the stationary traverse ID: ")
Referenced = input("Enter the referenced traverse ID: ")
R_y = float(input(f"Enter the Y coordinates of {Referenced} (m): "))
R_x = float(input(f"Enter the X coordinates of {Referenced} (m): "))
Height_r = float(input(f"Enter the height of {Referenced} (m): "))
S_y = float(input(f"Enter the Y coordinates of {Stationary} (m): "))
S_x = float(input(f"Enter the X coordinates of {Stationary} (m): "))
Height_s = float(input(f"Enter the height of {Stationary} (m): "))
Detail_point = input("Enter the point ID of detail point: ")
Horizontal_direction = float(input("Enter the horizontal direction of point {} (grad): ".format(Detail_point)))
Vertical_angle = float(input(f"Enter the vertical angle of point {Detail_point} (grad): "))
Slope_distance = float(input("Enter the slope distance between {} and {} (m): ".format(Stationary, Detail_point)))
Height_instrument = float(input("Enter the height of instrument (m): "))
Height_reflector = float(input("Enter the height of reflector (m): "))
Z = Vertical_angle

#Calculations

angle_degree = float(Z)
angle_radian = angle_degree / 180 * math.pi
angle_grad = angle_radian * 9 / 10

#Azimuth calculation

def azimuth(y,x):
    if x == 0:
        if y>0:
            angle = 100
        else:
            angle = 300
        return angle
    angle = math.atan(abs(y)/abs(x))*200/math.pi

    if y>0 and x<0:
        angle = 200 - angle
    elif y<0 and x<0:
        angle = 200 + angle
    elif y<0 and x>0:
        angle = 400- angle
    return angle


value = azimuth(S_y-R_y,S_x-R_x) + Horizontal_direction
if value<200:
    value += 200
elif value>200 and value<600:
    value -= 200
elif value>600:
    value -= 600


horiztontal_distance = Slope_distance * math.sin(angle_grad)
delta_h = Slope_distance * math.cos(angle_grad) + Height_reflector-Height_instrument
elevation = Height_s + delta_h
coordinate_y = S_y + horiztontal_distance * math.sin(value*math.pi/200)
coordinate_x = S_x + horiztontal_distance * math.cos(value*math.pi/200)


#Output adjustments

b1 = format(horiztontal_distance, ".3f")
b2 = format(delta_h, ".3f")
b3 = format(elevation, ".3f")
b4 = format(coordinate_y, ".3f")
b5 = format(coordinate_x, ".3f")


print(">>>")
print(format("Point ID", "<10s"),format("Point ID", "<10s"),format("Hor. Dist.", "<10s"),format("Delta H", "<10s"),format("Elevation", "<10s"),format("Coordinate (Y)","<10s"),format("Coordinate (X)","<10s"),sep="")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−-")
print(format(Stationary, "<10s"), format(Detail_point, "<10s"),format(b1, "<10s"), format(b2, "<10s"),format(b3,"<10s"),format(b4,"<10s"),format(b5,"<10s"))



