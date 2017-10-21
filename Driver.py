import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def kalman_filter(process_variance, state_var,  # R, P
                  process_noise,  # Q
                  noisy_measurement):
    """Takes in noisy array, and returns filtered result"""
    # POSTERI_ESTIMATE intial guesses, doesn't matter on large scale, use
    # reasonable estimate
    # process_variance = 1e-5 initial value, it changes
    #posteri_error_estimate = 10
    # estimate of measurement variance, change to see effect true value estimate variance
    #ESTIMATED_MEASUREMENT_VARIANCE = 0.05 ** 2
    posteri_estimate = (np.max(noisy_measurement[0:10]) +np.min(noisy_measurement[0:10]))/2
    posteri_estimate_for_graphing = []
    for iteration in range(0, len(noisy_measurement)):
        # time update
        priori_estimate = posteri_estimate
        priori_error_estimate = state_var + process_variance
        # measurement update
        blending_factor = priori_error_estimate / \
            (priori_error_estimate + process_noise)
        posteri_estimate = priori_estimate + blending_factor * \
            (noisy_measurement[iteration] - priori_estimate)
        state_var = (1 - blending_factor) * priori_error_estimate
        posteri_estimate_for_graphing.append(posteri_estimate)
    return posteri_estimate_for_graphing

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
sandp = pd.read_csv("^GSPC.csv")

q = 500
coal = kalman_filter(4, .001, q, emissions.get(coal))
natural_gas = kalman_filter(4, .001, q, emissions.get(natural_gas))
distillate = kalman_filter(4, .001, q, emissions.get(distillate))
hydrocarbon = kalman_filter(4, .001, q, emissions.get(hydrocarbon))
jet_fuel = kalman_filter(4, .001, q, emissions.get(jet_fuel))
motor_gasoline = kalman_filter(4, .001, q, emissions.get(motor_gasoline))
sp = kalman_filter(4, .001, q, sandp.get("Adj Close")) #/ np.max(sandp.get("Adj Close"))
#kerosene = kalman_filter(4, .001, q, emissions.get(kerosene))
#aviation = kalman_filter(4, .001, q, emissions.get(aviation))
#lubricants = kalman_filter(4, .001, q, emissions.get(lubricants))

ab, =plt.plot(coal,label="Coal")
ac, =plt.plot(natural_gas,label="Natural Gas")
#ad, =plt.plot(aviation,label="Aviation")
ae, =plt.plot(distillate,label="Distillate Fuel Oil")
#af, =plt.plot(hydrocarbon,label="Hydrocarbon Liquids")
ag, =plt.plot(jet_fuel,label="Jet_Fuel")
#ah, =plt.plot(kerosene,label="Kerosene")
#ai, =plt.plot(lubricants,label="Lubricants")
aj, =plt.plot(motor_gasoline,label="Motor Gasoline")
ak, =plt.plot(sp, label="S&P 500")
plt.legend(handles=[ab, ac, ae, ag, ak])
plt.show()