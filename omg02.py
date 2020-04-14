import matplotlib.pyplot as plt
import pywt
from scipy.misc import electrocardiogram

# denoise sample ecg signal using pywavelet

data_raw = electrocardiogram()
data_raw = data_raw[:2000]
w = pywt.Wavelet('sym4')

# select a maxlev or using pywt.dwt_max_level()
maxlev = pywt.dwt_max_level(len(data_raw), w.dec_len)
# maxlev = 2
print(f"maximum level is {maxlev}")

coeffs = pywt.wavedec(data_raw, w, level=maxlev)

threshold = 0.1
plt.figure()
for i in range(1, len(coeffs)):
    plt.subplot(maxlev, 1, i)
    plt.plot(coeffs[i], 'b-')

    # apply threshold
    coeffs[i] = pywt.threshold(coeffs[i], threshold * max(coeffs[i]))

    plt.plot(coeffs[i], 'r-')

data_denoised = pywt.waverec(coeffs, w)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(data_raw)
plt.title("raw")
plt.subplot(2, 1, 2)
plt.plot(data_denoised)
plt.title("denoised")
plt.tight_layout()
plt.show()
