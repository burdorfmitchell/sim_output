# coding: utf-8
from pyuvdata import UVData
import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time

uv1 = UVData()
uv3 = UVData()
uv10 = UVData()
uv30 = UVData()

uv1.read("24h_1MHz.uvh5")
uv3.read("24h_3MHz.uvh5")
uv10.read("24h_10MHz.uvh5")
uv30.read("24h_30MHz.uvh5")

print(uv1.history)
print(uv3.history)
print(uv10.history)
print(uv30.history)

auto1xx  = uv1.get_data((0,0,"xx"))
auto3xx  = uv3.get_data((0,0,"xx"))
auto10xx = uv10.get_data((0,0,"xx"))
auto30xx = uv30.get_data((0,0,"xx"))

auto1yy  = uv1.get_data((0,0,"yy"))
auto3yy  = uv3.get_data((0,0,"yy"))
auto10yy = uv10.get_data((0,0,"yy"))
auto30yy = uv30.get_data((0,0,"yy"))

auto1full = np.abs(auto1xx + auto1yy)
auto3full = np.abs(auto3xx + auto3yy)
auto10full = np.abs(auto10xx + auto10yy)
auto30full = np.abs(auto30xx + auto30yy)

jd_time = [Time(t, format="jd", scale="utc") for t in np.unique(uv1.time_array)[::int(510/12)]]
time = [t.strftime("%H:%M") for t in jd_time]
jd_time = np.unique(uv1.time_array)[::int(510/12)]

times = np.unique(uv1.time_array)

plt.plot(times, np.abs(auto1full), label="1 MHz")
plt.plot(times, np.abs(auto3full), label="3 MHz")
plt.plot(times, np.abs(auto10full), label="10 MHz")
plt.plot(times, np.abs(auto30full), label="30 MHz")
plt.scatter(times[np.argmax(auto1full)], np.max(auto1full), s=50)
plt.scatter(times[np.argmax(auto3full)], np.max(auto3full), s=50)
plt.scatter(times[np.argmax(auto10full)], np.max(auto10full), s=50)
plt.scatter(times[np.argmax(auto30full)], np.max(auto30full), s=50)

#plt.title("Abs of (0,0, \"xx\") for 1, 3, 10, 30 MHz")

plt.title(r"|V_{xx} + V_{yy}| of Baseline (0,0) at 1, 3, 10, 30 MHz")

plt.xticks(jd_time, time, fontsize=8.5)
plt.xlabel("Time (HH:MM)", fontsize=11)

#plt.ylabel("Abs of \"xx\" Polarization for Baseline (0,0)", fontsize=11)

#plt.ylabel("Abs of \"yy\" Polarization for Baseline (0,0)", fontsize=11)

plt.ylabel("Visibility Amplitude", fontsize=11)

plt.legend()

#plt.savefig("xx_auto_plot.png")

plt.savefig("full_auto_plot.png")
