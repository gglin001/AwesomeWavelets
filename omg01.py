import matplotlib.pyplot as plt
import pywt
import pywt.data

# from https://pywavelets.readthedocs.io/en/latest/index.html

original = pywt.data.camera()

# Wavelet transform of image, and plot approximation and details
LL, (LH, HL, HH) = pywt.dwt2(original, 'bior1.3')

fig, axs = plt.subplots(1, 5, figsize=(12, 3))
axs = axs.ravel()

titles = ['Approximation', ' Horizontal detail', 'Vertical detail', 'Diagonal detail']
for i, x in enumerate([LL, LH, HL, HH]):
    axs[i].imshow(x, interpolation="nearest", cmap=plt.cm.gray)
    axs[i].set_title(titles[i])

axs[-1].imshow(original, interpolation="nearest", cmap=plt.cm.gray)
axs[-1].set_title('raw img')
fig.tight_layout()
plt.show()
