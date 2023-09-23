#!/user/bin/env python
import time
import argparse
import math
from flyt_python import api

drone = api.navigation(timeout=120000)

time.sleep(3)

parser = argparse.ArgumentParser()
parser.add_argument('side', metavar='sidelength', type=float, help='side length of the triangle')
parser.add_argument('altitude', metavar='height', type=float, help='drone takeoff altitude')
args = parser.parse_args()

sidelength = args.side
height = args.altitude

if drone.arm():
	print 'DRONE ARMED'
else:
	print 'DRONE NOT ARMED'

print 'TAKING OFF TO AN ALTITUDE OF',height,'m'
drone.take_off(height)

print 'MOVING IN A TRIANGLE TRAJECTORY OF SIDE', sidelength, 'm'
time.sleep(10)
pos = drone.get_local_position()
print 'local position of drone', pos.x, pos.y

drone.position_set(sidelength, math.sin(36.87*(math.pi/180))*sidelength, 0, relative=True)
time.sleep(10)
pos = drone.get_local_position()
print 'local position of drone', pos.x, pos.y

drone.position_set(-sidelength/2, (sidelength/2)*math.sqrt(3), 0, relative=True)
time.sleep(10)
pos = drone.get_local_position()
print 'local position of drone', pos.x, pos.y

drone.position_set(-sidelength/2, -(sidelength/2)*math.sqrt(3), 0, relative=True)
time.sleep(10)
pos = drone.get_local_position()
print 'local position of drone', pos.x, pos.y

print 'TRAJECTORY COMPLETED SUCCESSFULLY'
print 'LANDING INITIATED'
drone.land(False)
time.sleep(3)
print 'LANDED SAFELY. CHEERS!!'

if drone.disarm():
	print 'DRONE DISARMED'
else: 
	print 'DRONE STILL ARMED'

drone.disconnect()
