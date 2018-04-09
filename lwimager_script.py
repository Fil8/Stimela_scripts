import stimela

INPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/input"
OUTPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/output"
MSDIR="/home/maccagni/FornaxA/data/MeerKAT/fa1/msdir"

calmodel ='fa1_fast_tmp_1-model.fits'
recipe = stimela.Recipe("Test clean mask making", ms_dir=MSDIR)

recipe.add("cab/lwimager", "lwimager_model",
{
	"msname"        : 'fa1_conc-corr.ms', 
	"simulate_fits" : calmodel+":output",
	"column"        : 'MODEL_DATA',
	"img_nchan"     : 1,
	"img_chanstep"  : 1,
	"nchan"         : 175,
	"cellsize"      : 2.6,
},
input=INPUT, 
output=OUTPUT,
label="Update model_data column")

recipe.run()
