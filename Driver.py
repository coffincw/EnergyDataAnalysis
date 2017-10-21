import pandas as pd
import matplotlib.pyplot as plt

month = "Month"
coal = "Coal, Including Coal Coke Net Imports"
natural_gas = "Natural Gas, Excluding Supplemental Gaseous Fuels"
aviation = "Aviation Gasoline"
distillate = "Distillate Fuel Oil, Excluding Biodiesel"
hydrocarbon = "Hydrocarbon Gas Liquids"
jet_fuel = "Jet Fuel"
kerosene = "Kerosene"
lubricants = "Lubricants"
motor_gasoline = "Motor Gasoline, Excluding Ethanol"

emissions = pd.read_csv("emissions_by_source_73_17.csv")

ab,=plt.plot(emissions.get(coal), label="Coal")
ac=plt.plot(emissions.get(natural_gas), label="Natural Gas")
ad=plt.plot(emissions.get(aviation), label="Aviation")
ae=plt.plot(emissions.get(distillate), label="Distillate Fuel Oil")
af=plt.plot(emissions.get(hydrocarbon), label="Hydrocarbon Liquids")
ag=plt.plot(emissions.get(jet_fuel), label="Jet_Fuel")
ah=plt.plot(emissions.get(kerosene), label="Kerosene")
plt.plot(emissions.get(lubricants), label="Lubricants")
plt.plot(emissions.get(motor_gasoline), label="Motor Gasoline")
plt.legend(handles=[ab, ac, ad, ae, af, ag, ah])
plt.show()