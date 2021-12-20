# jax-spectral

A limited port of [`scipy.signal.spectral`](https://docs.scipy.org/doc/scipy/reference/signal.html) (from SciPy 1.5.4) to [JAX](https://github.com/google/jax).

Supports:
- [`stft`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.stft.html#scipy.signal.stft)
- [`istft`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.istft.html#scipy.signal.istft)
- [`windows`](https://docs.scipy.org/doc/scipy/reference/signal.windows.html)

Note: STFT only works when `nfft == nperseg` and `nperseg` (window size) is a multiple of `nperseg - noverlap` (hop size).

See also the official [`jax.scipy.signal`](https://jax.readthedocs.io/en/latest/jax.scipy.html#module-jax.scipy.signal) (currently missing an implementation of `spectral`).

## Installation
```
pip install 'git+https://github.com/cifkao/jax-spectral.git@main#egg=jax-spectral'
```
