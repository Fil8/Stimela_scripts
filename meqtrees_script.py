import stimela
import os

INPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/input"
OUTPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/output"
MSDIR="/home/maccagni/FornaxA/data/MeerKAT/fa1/msdir"


recipe = stimela.Recipe("Calibrate with meqtrees", ms_dir=MSDIR)


calmodel = 'aaa-nullmodel.txt'
with open(os.path.join(INPUT, calmodel), 'w') as stdw:
    stdw.write('#format: ra_d dec_d i\n')
    stdw.write('0.0 -30.0 1e-99')

msname = 'fa1_conc-corr.ms'

step = 'calibrate_1'
recipe.add('cab/calibrator', step,
   {
     "skymodel"             : calmodel,
     "add-vis-model"        : True,
     "msname"               : msname,
     "threads"              : 9,
     "model-column"			: "MODEL_DATA",
     "column"               : "DATA",
     "output-data"          : 'CORR_DATA',
     "output-column"        : "CORRECTED_DATA",
     "prefix"               : 'fa1-fast_meqtrees',
     "label"                : 'cal_1',
     "read-flags-from-ms"   : True,
     "read-flagsets"        : "-stefcal",
     "write-flagset"        : "stefcal",
     "write-flagset-policy" : "replace",
     "Gjones"               : True,
     "Gjones-solution-intervals" : [10,0],
     "Gjones-matrix-type"   :'GainDiagPhase',
     "Gjones-ampl-clipping"      : True,
     "Gjones-ampl-clipping-low"  : 0.5,
     "Gjones-ampl-clipping-high" : 1.5,
     "make-plots"           : True,
     "tile-size"            : 2995,
   },
   input=INPUT,
   output=OUTPUT,
   label="{0:s}:: Calibrate with meqtrees")

recipe.run()