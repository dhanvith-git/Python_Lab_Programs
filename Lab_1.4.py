consumer_name = input("enter a name:")
consumer_id = int(input("enter a ID:"))
previous_meter_reading = int(input("enter a PMR:"))
current_meter_reading = int(input("enter a CMR:"))
cost_per_unit = int(input("cost per unit:"))
units_consumed = current_meter_reading - previous_meter_reading
energy_charge = units_consumed * cost_per_unit 
electrical_duty = 0.05 * energy_charge
Fixed_meter_change = 100
netbill = energy_charge + electrical_duty + Fixed_meter_change
print("\n Calculation of Bill")
print(f"units consumed: {units_consumed}")
print(f"Energy_charge: {energy_charge}")
print(f"Electric_duty: {electrical_duty}")
print(f"Net-bill: {netbill}")
