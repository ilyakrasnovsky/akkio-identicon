import matplotlib.pyplot as plt
import numpy as np
import hashlib
from string import ascii_lowercase, digits

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

def name_to_pixel_grid(name: str) -> np.ndarray:
  hashed_name = hashlib.md5(name.encode(encoding='utf-8')).hexdigest()
  ret = np.zeros((8,8))
  for i in range(16):
    # decimal representation of each hex char in the hashed string, in [0, 16)
    d1 = int(hashed_name[i], base=16)
    d2 = int(hashed_name[i + 16], base=16)

    # color in d1 (after conversion to (i,j) via row-major order) only if d2 (shifted 16 indices) is even
    # this condenses the information
    val = d1 if d2 % 2 == 0 else None

    # source (top left quadrant)
    ret[i // 4][i % 4] = val
    # diagonal mirror (bottom right quadrant)
    ret[7-(i // 4)][7-(i % 4)] = val
    # vertical mirror (bottom left quadrant)
    ret[7-(i // 4)][i % 4] = val
    # horizontal mirror (top right quadrant)
    ret[i // 4][7-(i % 4)] = val

  return ret

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

if __name__ == "__main__":
  show_identicon(pixel_grid=name_to_pixel_grid(name="e28rnc288 c3"))
  # plt_test()
  # regular_hash()
  # hexdigest produces a 128 bit value. There will be 32 hex numbers (4 bits each)
  # 
  # pixel_plot_test()
