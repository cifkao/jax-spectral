# jax-spectral

A limited port of [`scipy.signal.spectral`](https://docs.scipy.org/doc/scipy/reference/signal.html) (from SciPy 1.5.4) to [JAX](https://github.com/google/jax).

Contains:
- [`stft`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.stft.html#scipy.signal.stft)
- [`istft`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.istft.html#scipy.signal.istft)
- [`windows`](https://docs.scipy.org/doc/scipy/reference/signal.windows.html)

Note: STFT only works when `nfft == nperseg` and `nperseg` (window size) is a multiple of `nperseg - noverlap` (hop size).

## Installation
```
pip install git+https://github.com/cifkao/jax-spectral.git@main#egg=jax-spectral
```
