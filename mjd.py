import time
import numpy as np
from astropy.time import Time

astropy_now = Time.now()
now = time.time()

print("AstroPy MJD:", astropy_now.mjd)

mjd = now / 86400.0 + 40587
print("Python MJD: ", mjd) 

