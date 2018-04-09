import stimela

INPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/input"
OUTPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/output"
MSDIR="/home/maccagni/FornaxA/data/MeerKAT/fa1/msdir"

mask_clean = 'masking/sofia_4_mask.fits'

recipe = stimela.Recipe("wsclean_image", ms_dir=MSDIR)

step = '2'
image_opts = {                   
"msname"    : "fa1_conc-corr.ms",
"column"    : 'DATA',
"weight"    : 'briggs -1.5',
'field'     : 1,
"npix"      : 4500,
"trim"      : 3000,
"scale"     : 2.6,
"prefix"    : 'fa1_fast_stim',
"niter"     : 500000,
"mgain"     : 0.9,
"pol"       : 'I',
"channelsout"     : 1,
"joinchannels"    : False,
"fit-spectral-pol": False,
"verbose"     : True,
"auto-threshold": 0.1,
'no-update-model-required': False,
"multiscale" : False,
#"multiscale-scales" : [10,50],
"fitsmask": mask_clean+':output',
"local-rms": True,
"minuvw-m"  : 50,
"dft-prediction": True,
"predict": True,
}

recipe.add('cab/wsclean', step,
        image_opts,
        input=INPUT,
        output=OUTPUT,
        label='Make image')

recipe.run()
