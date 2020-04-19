from vehicle import Vehicle

# Electric motorcycle
class Zero():
    def __init__(self, battery, color, occupancy):
        self.battery_kwh = 0
        self.main_color = ""
        self.maximum_occupancy = 0

    def charge_battery(self):
        pass

    def drive(self):
        print(f"The {self.main_color} Zero drives past... WUHSHHHH!")