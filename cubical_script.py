import stimela
import os

INPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/input"
OUTPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/output"
MSDIR="/home/maccagni/FornaxA/data/MeerKAT/fa1/msdir"

calmodel = 'fa1_fast_modelcorr.fits'
msname = 'fa1_conc-corr.ms'
recipe = stimela.Recipe("Calibrate with meqtrees", ms_dir=MSDIR)


calmodel = '{0:s}_{1:d}-nullmodel.txt'
with open(os.path.join(INPUT, calmodel), 'w') as stdw:
    stdw.write('#format: ra_d dec_d i\n')
    stdw.write('0.0 -30.0 1e-99')

# step = 'add_bitflag_column'
# recipe.add('cab/msutils', step,
# {
#   "msname"  : msname,
#   "command" : 'copycol' ,
#   "fromcol" : 'FLAG',
#   "tocol"   : 'BITFLAG',
# },
# input=INPUT,
# output=OUTPUT,
# label='Add BITFLAG column ')

step = 'calibrate_cubical'
recipe.add('cab/cubical', step,
{
    "data-ms"          : msname, 
    "data-column"      : 'DATA',
    "model-column"     : 'MODEL_DATA',
    "j2-term-iters"    : 200,
    "data-time-chunk"  : 2295,
    "sel-ddid"         : '0',
    "dist-ncpu"        : 9,
    "sol-jones"        : 'G',
    "model-lsm"        : calmodel,
    "out-name"         : 'fa1_fast_cubical',
    "out-mode"         : 'sc', 
    "out-plots-show"   : True,
    "weight-column"    : 'WEIGHT',
    "montblanc-dtype"  : 'float',
    "j1-solvable"      : True,
    "j1-type"          : 'phase-diag',
    "j1-time-int"      : 10,
    "j1-freq-int"      : 0,
    "j1-clip-low"      : 0.5,
    "j1-clip-high"     : 1.5,

},
   input=INPUT,
   output=OUTPUT,
   shared_memory='100Gb',
   label=" Calibrate with cubical")

recipe.run()
