import os
from wisdem import run_wisdem
import numpy as np
from wisdem.commonse.mpi_tools import MPI


## File management
mydir = os.path.dirname(os.path.realpath(__file__))  # get path to this file
fname_wt_input = os.path.join(mydir, "IEA-22-280-RWT.yaml")
fname_modeling_options = os.path.join(mydir, "modeling_options_monopile.yaml")
fname_analysis_options = os.path.join(mydir, "analysis_options_monopile.yaml")
wt_opt, modeling_options, analysis_options = run_wisdem(fname_wt_input, fname_modeling_options, fname_analysis_options)


if MPI:
    rank = MPI.COMM_WORLD.Get_rank()
else:
    rank = 0
if rank == 0:
    print("Tower mass (kg) =", wt_opt["towerse.tower_mass"])
    print("Monopile mass (kg) =", wt_opt["fixedse.monopile_mass"])

