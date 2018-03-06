import stimela

INPUT="input"
OUTPUT="output"
MSDIR="msdir"

recipe = stimela.Recipe("Concatenate ms files using CASA concat", ms_dir=MSDIR)
recipe.add("cab/casa_concat", "casa_concat",
{
"msname": ["1504823274.ms","1504834284.ms","1504846207.ms"],
"output-msname": 'fa2_conc',
},
input=INPUT, output=OUTPUT,
label="Concatenate multiple datasets")

recipe.run()
