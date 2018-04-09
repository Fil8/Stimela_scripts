import stimela

INPUT="input"
OUTPUT="output"
MSDIR="msdir"

recipe = stimela.Recipe("wsclean_psf_only", ms_dir=MSDIR)
recipe.add("cab/wsclean", "wsclean_psf_only",
{
  "msname"    : ['fa1_conc.ms'],
  "name"	  : 'tmp',
  "column"    : 'DATA',
  "weight"    : 'natural',
  "npix"      : 10000,
  "trim"      : 8192,
  "scale"     : 1.3,
  "make-psf-only": True,
  "niter"     : 1,
  "pol"       : 'xx',
  "channelsout"     : 1,
  "joinchannels"    : False,
},
input=INPUT, output=OUTPUT, shared_memory="250gb",
label="PSF ONLY")

recipe.run()
