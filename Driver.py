import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Prediction
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
total = "Total Energy"

emissions = pd.read_csv("emissions_by_source_73_17.csv")
sandp = pd.read_csv("^GSPC.csv")

q = 500
coal = kalman_filter(4, .001, q, emissions.get(coal))
natural_gas = kalman_filter(4, .001, q, emissions.get(natural_gas))
distillate = kalman_filter(4, .001, q, emissions.get(distillate))
# hydrocarbon = kalman_filter(4, .001, q, emissions.get(hydrocarbon))
jet_fuel = kalman_filter(4, .001, q, emissions.get(jet_fuel))
total = kalman_filter(4, .001, q, emissions.get(total))
# motor_gasoline = kalman_filter(4, .001, q, emissions.get(motor_gasoline))
sp = kalman_filter(4, .001, q, sandp.get("Adj Close")/10) #/ np.max(sandp.get("Adj Close"))
#kerosene = kalman_filter(4, .001, q, emissions.get(kerosene))
#aviation = kalman_filter(4, .001, q, emissions.get(aviation))
#lubricants = kalman_filter(4, .001, q, emissions.get(lubricants))


def percentChange(a) :
    max = np.max(a)
    for x in range(0,len(a)):
        a[x] = (a[x] / max)

percentChange(coal)
percentChange(natural_gas)
percentChange(distillate)
percentChange(total)
percentChange(jet_fuel)
percentChange(sp)


ab, =plt.plot(coal,'black', label="Coal")
ac, =plt.plot(natural_gas,'gray', label="Natural Gas")
ad, =plt.plot(total,'blue', label="Total Energy")
ae, =plt.plot(distillate,'brown', label="Distillate Fuel Oil")
ag, =plt.plot(jet_fuel,'pink', label="Jet_Fuel")
ak, =plt.plot(sp,'orange', label="S&P 500")
az, =plt.plot(range(533, 654), Prediction.predict(total), 'cyan', label="Predicted Total")
# pc, =plt.plot(range(533, 654), Prediction.predict(coal), label="Predicted Coal")
sk, =plt.plot(range(538, 659), Prediction.predict(sp), 'yellow', label="Predicted S&P 500")
plt.axes().set_xlabel("Months since 1973")
plt.axes().set_ylabel("Percent change")
plt.title("Predicting C02 Emmisions/S&P 500")
plt.gcf().canvas.set_window_title('Energy and Economy Predictions')

plt.legend(handles=[ab, ac, ae, ag, ad, ak, az, sk])
plt.show()