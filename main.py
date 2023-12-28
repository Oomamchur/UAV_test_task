import time
import socket
import exeptions
import math
import argparse
import dronekit_sitl

from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException


class Drone:
    def __init__(self):
        self.drone = None

    def connect_drone(self):
        parser = argparse.ArgumentParser(description="commands")
        parser.add_argument("--connect")
        args = parser.parse_args()

        connection_string = args.connect

        if not connection_string:
            sitl = dronekit_sitl.start_default()
            connection_string = sitl.connection_string()

        self.drone = connect(connection_string, wait_ready=True)

        return self.drone

    def arm_and_takeoff(self, altitude: int) -> None:
        while not self.drone.is_armable:
            print("Waiting for vehicle to be armable.")
            time.sleep(1)
        print("Drone is armable!")

        self.drone.armed = True

        while not self.drone.armed:
            print("Waiting for vehicle to be armed.")
            time.sleep(1)

        print("Drone is taking off!")

        self.drone.simple_takeoff(altitude)

        while True:
            print(f"Current Altitude: {self.drone.location.global_relative_frame.alt}")
            if self.drone.location.global_relative_frame.alt >= altitude * 0.95:
                break
            time.sleep(0.5)

        print("Target altitude reached!")


if __name__ == '__main__':
    height = 100
    drone1 = Drone()
    drone1.connect_drone()
    drone1.arm_and_takeoff(height)

