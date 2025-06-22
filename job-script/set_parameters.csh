set COMPILE  = 1

# ----------------------------------------------------------
#      INPUT
# ----------------------------------------------------------
# GREB experiment set up exp = 310 -> dynamic equalibrium run for standalone experiment
# GREB experiment set up exp = 311 -> dynamic equalibrium run for transition experiment
set EXP        = 310 # ice sheet standalone run 

# name of experiment
set NAME       = benchmark_pictrl
# set NAME = benchmark_tran

# exp start time of orbital forcing [kyrs before today]
set KYRSTART   = -200
if ($EXP == 311) set KYRSTART = -250

# exp end time of orbital forcing [kyrs before today]
set KYREND     = 0

# acceleration of orbital forcing 1 -> normal 10 -> 10x faster ...
set DTACC      = 1

# length of qflux correction run [yrs]
set TIME_QFLX  = 15

# length of control run [yrs]
set TIME_CTRL  = 3

# length of single GREB model run [yrs]
set TDIM_RUN   = 1000

# number of GREB model run in one job (per restart/newstart)
set NRUN       = 1

# ICE SHEET 
set log_ice_ithk  = 1  # ice thickness initial condition (0=ice free; 1=start from current ice thickness)
set log_ice_topo  = 1  # topogragh coupling control
set log_ice_slv   = 1  # sea level control
set log_ice_ant   = 1


# directories
set WDIR=/home/arindam/GREB-ISM
