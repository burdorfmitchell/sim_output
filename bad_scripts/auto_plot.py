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

auto1 = uv1.get_data((0,0,"xx"))
auto3 = uv3.get_data((0,0,"xx"))
auto10 = uv10.get_data((0,0,"xx"))
auto30 = uv30.get_data((0,0,"xx"))

jd_time = [Time(t, format="jd", scale="utc") for t in np.unique(uv1.time_array)[::int(510/12)]]
time = [t.strftime("%H:%M") for t in jd_time]
jd_time = np.unique(uv1.time_array)[::int(510/12)]

times = np.unique(uv1.time_array)

plt.plot(times, np.abs(auto1), label="1 MHz")
plt.plot(times, np.abs(auto3), label="3 MHz")
plt.plot(times, np.abs(auto10), label="10 MHz")
plt.plot(times, np.abs(auto30), label="30 MHz")
plt.scatter(times[np.argmax(auto1)], np.abs(np.max(auto1)), s=50)
plt.scatter(times[np.argmax(auto3)], np.abs(np.max(auto3)), s=50)
plt.scatter(times[np.argmax(auto10)], np.abs(np.max(auto10)), s=50)
plt.scatter(times[np.argmax(auto30)], np.abs(np.max(auto30)), s=50)

plt.title("Abs of (0,0, \"xx\") for 1, 3, 10, 30 MHz")

plt.xticks(jd_time, time, fontsize=8.5)
plt.xlabel("Time (HH:MM)", fontsize=11)

plt.ylabel("Abs of \"xx\" Polarization for Baseline (0,0)", fontsize=11)

plt.legend()

plt.savefig("xx_auto_plot.png")
