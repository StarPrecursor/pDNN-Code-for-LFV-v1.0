import numpy as np
import ROOT

import lfv_pdnn_code_v1.common.common_utils

# root_vector_double = vector('double')()
# _length_const = 24

def get_lumi(run_number):
  """gets luminosity according to given run number.
  
  Args:
    run_number: float, run number of the event

  """
  if run_number == 284500.0:
    return 36.07456
  elif run_number == 300000.0:
    return 44.30
  elif run_number == 310000.0:
    return 58.4501
  else:
    print_warning("unknown run_number, luminosity set to zero")
    return 0