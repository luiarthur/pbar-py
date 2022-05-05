# pbar-py
[![CI Status][ci-status-img]](https://github.com/luiarthur/pbar-py/actions)

Simple progress bar for python

## Installation
```bash
pip install git+https://github.com/luiarthur/pbar

# Or, to keep track of URL in dependencies.
pip install -e git+https://github.com/luiarthur/pbar#egg=pbar
```

## Usage

```python
from pbar import pbar, pbrange

# Number of iterations.
n = 10000

# Sleep time.
s = 1e-4

# Example 1:
for i in pbrange(n):
    time.sleep(s)

# Example 2: Context and add extra args, using prange.
with pbrange(0, 5 * n, 5) as pb:
    for i in pb:
        pb.extra = {f"{i}^2": i ** 2}
        time.sleep(s)

# Example 3:
for i in pbar(range(n)):
    time.sleep(s)

# Example 4:
pb = pbar(range(n))
for i in pb:
    time.sleep(s)

# Example 5: Context and add extra args.
xs = range(0, 5 * n, 5)
with pbar(xs) as pb:
    for i in pb:
        pb.extra = {f"{i}^2": i ** 2}
        time.sleep(s)

# Example 6: Print to file.
for i in pbrange(10, fname="file.txt"):
    time.sleep(s)
```


[ci-status-img]: https://github.com/luiarthur/pbar-py/workflows/CI/badge.svg
