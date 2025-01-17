import numpy as np

print('**********************************')
print('*** INSERT STATION COORDINATES ***')
print('**********************************')

N_coord = float(input('N: '))
E_coord = float(input('E: '))
Z_coord = float(input('Z: '))

print('\n**********************************')
print('**** INSERT DISTANCE EN ANGLE ****')
print('**********************************')

dist = float(input('DIST (m): '))
azimuth = input('AZIMUTH (DMS): ')
vertical = input('VERTICAL ELEVATION (DMS): ')

print('\n**********************************')
print('**** INSERT DISTANCE EN ANGLE ****')
print('**********************************')

hs = float(input('STATION HEIGHT (m): '))
hp = float(input('PRISM HEIGHT (m): '))

try:
    azimuth = float(azimuth[:3]) + float(azimuth[4:6])/60 + float(azimuth[6:8])/3600
except:
    azimuth = float(azimuth[:2]) + float(azimuth[3:5])/60 + float(azimuth[5:7])/3600

vertical = float(vertical[:2]) + float(vertical[3:5])/60 + float(vertical[5:7])/3600

angle_rad = azimuth*np.pi/180
vertical_rad = vertical*np.pi/180

horizontal_distance = dist*np.sin(vertical_rad)*0.999622723022

delta_x = horizontal_distance*np.sin(angle_rad)
delta_y = horizontal_distance*np.cos(angle_rad)
delta_z = dist*np.cos(vertical_rad) + hs - hp

print("The desired coordinates are:")
print(f"N = {str(N_coord+delta_y)}, E = {str(E_coord+delta_x)}, Z = {str(Z_coord+delta_z)}")