"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.


def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def quadratic_multiply(x, y):
  # this just converts the result from a BinaryNumber to a regular int
  return _quadratic_multiply(x, y).decimal_val


def _quadratic_multiply(x, y):

  if len(x.binary_vec) <= 1 and len(y.binary_vec) <= 1:
    return BinaryNumber(
        binary2int(x.binary_vec).decimal_val *
        binary2int(y.binary_vec).decimal_val)
  xvec, yvec = pad(x.binary_vec, y.binary_vec)
  x_l, x_r = split_number(xvec)
  y_l, y_r = split_number(yvec)
  first = _quadratic_multiply(x_l, y_l)
  outer = _quadratic_multiply(x_l, y_r)
  inner = _quadratic_multiply(x_r, y_l)
  last = _quadratic_multiply(x_r, y_r)
  first = bit_shift(first, len(x_r.binary_vec) * 2)
  outer = bit_shift(outer, len(x_r.binary_vec))
  inner = bit_shift(inner, len(x_r.binary_vec))
  last = bit_shift(last, len(x_r.binary_vec) // 2)
  result = first.decimal_val + outer.decimal_val + inner.decimal_val + last.decimal_val
  return BinaryNumber(result)


#$x\cdot y= (2^{n/2} x_L + x_R)(2^{n/2} y_L + y_R)  =2^n (x_L \cdot y_L) + 2^{n/2} (x_L \cdot y_R + x_R \cdot y_L) + (x_R \cdot y_R) $


def test_quadratic_multiply(x, y, f):
  start = time.time()
  f(x, y)
  return (time.time() - start) * 1000


print(_quadratic_multiply(BinaryNumber(20), BinaryNumber(3)))
