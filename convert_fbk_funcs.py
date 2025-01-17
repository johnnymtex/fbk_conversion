import numpy as np

def convert_dms_to_deg(str_angle):
    decimal_second = int(str_angle[-1])
    seconds = int(str_angle[-3:-1])
    minutes = int(str_angle[-5:-3])
    degrees = int(str_angle[0:-6])

    if decimal_second >= 5:
        seconds += 1

    deg_angle = int(degrees) + int(minutes)/60 + int(seconds)/3600

    return deg_angle

def convert_deg_to_rad(angle):
    return angle*np.pi/180

def compute_horizontal_distance(dist, vertical_angle, fs=0.9996226):
    return dist*np.sin(vertical_angle)*fs+0.0231

def compute_deltas(dist, azimuth_angle, vertical_angle, hs, hp, fs=0.999626):
    rad_zenith = convert_deg_to_rad(vertical_angle)
    horizontal_dist = compute_horizontal_distance(dist, rad_zenith, fs=fs)

    rad_azimuth = convert_deg_to_rad(azimuth_angle)

    deltax = horizontal_dist*np.sin(rad_azimuth)
    deltay = horizontal_dist*np.cos(rad_azimuth)
    deltaz = dist*np.cos(rad_zenith)+hs-hp

    return deltax, deltay, deltaz

def get_NEZ(azimuth, dist, zenith, station_N, station_E, station_Z, hs, hp):
    azimuth_angle = convert_dms_to_deg(azimuth)+0.02
    zenith_angle = convert_dms_to_deg(zenith)
    dist = float(dist)

    deltax, deltay, deltaz = compute_deltas(dist, azimuth_angle, zenith_angle, hs, hp)

    point_N = station_N + deltay
    point_E = station_E + deltax
    point_Z = station_Z + deltaz

    return point_N, point_E, point_Z