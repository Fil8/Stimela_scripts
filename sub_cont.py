import stimela

INPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/input"
OUTPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/output"
MSDIR="/home/maccagni/FornaxA/data/MeerKAT/fa1/msdir"

ms = MSDIR + '/fa1_conc_csub-corr.ms'
toutname = MSDIR + '/fa1_conc_tmp-corr.ms'
recipe = stimela.Recipe("Subtract model of continuum", ms_dir=MSDIR)

recipe.add("cab/msutils", "sub_model",
{
     "command"	  : 'addcol',
     "msname"      : 'fa1_conc_csub-corr.ms', 
 	"subtract"    : True, 
 	"col1" 		  : 'CORRECTED_DATA',
 	"col2"        : 'MODEL_DATA',
},
input=INPUT, 
output=OUTPUT,
label="Subtract model_data column")

recipe.run()


import pyrap.tables as tables




print ''
print '--- Working on file {0:s} ---'.format(ms)

t=tables.table(ms)
tout = t.copy(toutname)
tout.close()
t.close()
t=tables.table(toutname, readonly = False)

model = t.getcol('MODEL_DATA')
data = t.getcol('CORRECTED_DATA')

subdata = data - model

t.putcol('CORRECTED_DATA', subdata)

t.close()

print '--- Subtracted MODEL DATA column in file ---'.format(toutname)

print '--- NORMAL TERMINATION --- '




