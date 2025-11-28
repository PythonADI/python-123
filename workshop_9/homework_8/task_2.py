class SmartIrrigator:
    def __init__(self, name, daily_limit):
        self.name = name
        self.water_reserve = 30
        self.daily_limit = daily_limit
        self.capacity = 100
    
    def refill(self, amount):
        new_volume = self.water_reserve + amount
        if new_volume > self.capacity:
            print(f"You exceeded capacity of {self.capacity}")
            new_volume = self.capacity

        self.water_reserve = new_volume

    def sprinkle(self, volume):
        new_volume = self.water_reserve - volume
        if new_volume < 0:
            raise ValueError(f"You cannot sprinkle that amount! ({self.water_reserve}/{self.capacity})")
        self.daily_limit -= volume
        self.water_reserve = new_volume

    @property
    def status(self):
        has_water = not self.needs_refill
        if self.daily_limit < 0:
            return "done"

        if has_water and self.daily_limit:
            return "irrigation required"
        if not has_water and self.daily_limit:
            return "reffilment required"
            
        if not self.daily_limit:
            return "done"

    @property
    def needs_refill(self):
        return (self.water_reserve / self.capacity) <= 0.2



ir1 = SmartIrrigator("test", 100)

ir1.refill(50)
print(ir1.water_reserve)

while ir1.status != "done":
    if ir1.status == "reffilment required":
        print("Refilling...")
        ir1.refill(100)
    print(f"{ir1.water_reserve}/{ir1.capacity} | {ir1.daily_limit}")
    if ir1.status == "irrigation required":
        print("Irrigating...")
        # we have 100l in reserve and we need to sprinkle 10l
        if ir1.daily_limit < ir1.water_reserve:
            ir1.sprinkle(ir1.daily_limit)
        else:
            ir1.sprinkle(ir1.water_reserve)
    

# print(ir1.status())
# ir1.sprinkle(78)
# print(ir1.status())
# ir1.refill(110)
# print(ir1.status())
# ir1.sprinkle(100)
# print(ir1.status())
