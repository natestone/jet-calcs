import math

altitude               = 12000     # meters
temperature_static_0   = 250       # K
static_pressure_0      = 60000     # Pa
inlet_area_1           = 2.0       # m^2
inlet_area_2           = 2.0       # m^2
airspeed               = 1.8       # mach

fan_pressure_ratio     = 4.0
overall_pressure_ratio = 3.0
turbine_pressure_ratio = 3.5
bypass_ratio           = 1.8

polytropic_compressor_efficiency   = 0.89
polytropic_fan_efficiency          = 0.90
polytropic_turbine_efficiency      = 0.89

latent_heat_value                    = 43000    # J/kg - jet fuel
turbine_inlet_temperature            = 2000     # K
ambient_specific_heat_at_constant_pressure   = 1.005    # J/(g*K)
core_specific_heat_at_constant_pressure      = 1.005    # J/(g*K)
exhaust_specific_heat_at_constant_pressure   = 1.005    # J/(g*K)

gamma = 1.4   # Specific heat ratio

specific_gas_constant_air = 287   # J/(kg * K)



# Total Temperature
total_temperature_1  = temperature_static_0 / ( 1 +  ((gamma - 1)/2) * pow(airspeed, 2))

print(f"Total temperature:  {total_temperature_1}")

total_pressure_1 = static_pressure_0 * pow(1 + ((gamma -1)/2) * pow(airspeed, 2), (gamma/(gamma -1)))

print(f"Total pressure:  {total_pressure_1}")

# Functions
if(airspeed > 1 and airspeed < 5):
  inlet_pressure_recovery_efficiency = 1 - 0.075 * pow((airspeed - 1),1.35)      # F(airspeed - mach)
else:
  inlet_pressure_recovery_efficiency = 1   # F(airspeed - mach)

print(f"Inlet pressure recovery efficiency:  {inlet_pressure_recovery_efficiency}")


# Inlet Mass Flow
inlet_mass_flow_rate_1 = (
        inlet_area_1 / pow(gamma/specific_gas_constant_air, 0.5)
        * total_pressure_1 / pow(total_temperature_1, 0.5)
        * airspeed * pow((1 + ((gamma -1/2) * pow(airspeed, 2))), (-(gamma + 1)/(2 * (gamma - 1))))
    )

print(f"Inlet mass flow rate 1:  {inlet_mass_flow_rate_1}")

inlet_mass_flow_rate_2 = (
        inlet_area_1 / pow(gamma/specific_gas_constant_air, 0.5)
        * total_pressure_1 / pow(total_temperature_1, 0.5)
        * airspeed * pow((1 + ((gamma -1/2) * pow(airspeed, 2))), (-(gamma + 1)/(2 * (gamma - 1))))
)

print(f"Inlet mass flow rate 2:  {inlet_mass_flow_rate_2}")



