import matplotlib.pyplot as plt
import numpy as np
import hashlib
import os

def name_to_pixel_grid(name: str) -> np.ndarray:
  """
  Core logic to take in an arbitrary string (conceptually someone's username), and return an 8x8
  grid of integers, where the integer in each cell is representative of a color for that cell, if the
  grid were to be considered as a pixel image. It roughly works as follows:

  1. Produce an MD5 hexdigest of the string. This is a 128-bit number represented as 32 four-bit hex values  
  2. Store the base-10 equivalent of each hex value into a cell in the top-right (4x4) quadrant in row-major
     order. Store None if the hex value 16 places to the right of the one being considered is even (see comment
     below for more discussion).
  3. Mirror the 4x4 quadrant into the other three quadrants 
  """
  hashed_name = hashlib.md5(name.encode(encoding='utf-8')).hexdigest()
  ret = np.zeros((8,8))
  for i in range(16):
    # decimal representation of each hex char in the hashed string, in [0, 16)
    d1 = int(hashed_name[i], base=16)
    d2 = int(hashed_name[i + 16], base=16)

    # color in d1 (after conversion to (i,j) via row-major order) only if d2 (shifted 16 indices) is even.
    # This condenses the information encoded in the hexdigest from 32 values to 16. This is helpful because
    # 16 is a perfect square, which means filling in grid values with it in row-major order will produce a 
    # square (not a rectangle), which is more aesthetically pleasing.
    # There could be other interesting ways of combining d1 and d2 to do the condensing,
    # ex. taking an average.
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

def generate_identicons(names: list[str] =["John", "Jane", "931D387731bBbC988B31220", "Ilya"]) -> None:
  """
  Given a list of names to convert to identicons, output a <name>.png for each one in the tmp/ folder of
  this git repository, along with an all.png including all on one canvas. 
  """
  outpath = os.path.join(os.path.dirname(__file__), "tmp")
  for name in names:
    plt.imshow(name_to_pixel_grid(name), cmap='Blues', interpolation='nearest', origin='upper')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.savefig(os.path.join(outpath, f"{name}.png"))

  fig, subs = plt.subplots(len(names), 1)
  fig.tight_layout()
  for i, sub in enumerate(subs):
    sub.imshow(name_to_pixel_grid(names[i]), cmap='Blues', interpolation='nearest', origin='upper')
    sub.set_title(names[i])
    sub.get_xaxis().set_visible(False)
    sub.get_yaxis().set_visible(False)
  plt.savefig(os.path.join(outpath, "all.png"))

if __name__ == "__main__":
  """
  Entry point.
  """
  generate_identicons()

