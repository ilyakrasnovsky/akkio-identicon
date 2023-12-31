"""
This module contains scratchwork, messy experiments used at arriving towards
my solution in main.py.
"""
import matplotlib.pyplot as plt
import numpy as np
import hashlib

def show_identicon(pixel_grid: np.ndarray) -> None:
  _ = plt.imshow(pixel_grid, cmap='Blues', interpolation='nearest', origin='upper')
  # plt.axis("off")  
  ax = plt.gca()
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  plt.show()

def md5_hash() -> None:
  # print(int("A1", 16))
  # 1baad9235021178dc28a5948f83e6cce
  print(hashlib.md5("John1".encode()).hexdigest())
  # print(hashlib.md5(b"John1").digest())
  # print(hashlib.md5(b"Jon").hexdigest())

def plt_test() -> None:
  polygon = np.array([
    [0.0, 0.0],
    [0.0, 2.0],
    [1.0, 3.0],
    [1.0, 0.0]
  ])
  plt.plot(polygon[:, 0], polygon[:, 1], "o")
  plt.axis("off")
  # ax = plt.gca()
  # ax.get_xaxis().set_visible(False)
  # ax.get_yaxis().set_visible(False)
  plt.show()

def pixel_plot_test() -> None:
  # data = np.arange(0, 64).reshape(8, 8) 
  data = np.zeros((8,8))
  for i in range(0, 32):
    data[i // 8][i % 8] = i
  for i in range(63, 32, -1):
    data[i // 8][i % 8] = 64 -i
  data[5][5] = None
  data[7][7] = None
  identicon = plt.imshow(data, cmap='twilight_shifted', interpolation='nearest', origin='upper')
  plt.axis("off")
  plt.show()

def regular_hash() -> None:
  a = hash("John")
  b = hash("Jon")
  print (a)
  print (b)

if __name__ == "__main__":
  plt_test()
  regular_hash()
  # hexdigest produces a 128 bit value. There will be 32 hex numbers (4 bits each)
  pixel_plot_test()