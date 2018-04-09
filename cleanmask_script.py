import stimela
from astropy.io import fits
import numpy as np

INPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/input"
OUTPUT="/home/maccagni/FornaxA/data/MeerKAT/fa1/output"
MSDIR="/home/maccagni/FornaxA/data/MeerKAT/fa1/msdir"

image = "fa1_fast_tmp_1-image.fits"
model = "fa1_fast_tmp_1-model.fits"
fa1_cleanmask = "masking/xxxx_mask.fits"
fornax_mask = "masking/fornaxa_mask.fits"
merged_mask = "masking/merged_mask.fits"
model_corr = "fa1_fast_modelcorr.fits"


def divide_nonzero(mask):

	maskdata=fits.open(mask, mode = 'update')
	data=maskdata[0].data
	index_num = np.where(data!=0)
	data[index_num] /= data[index_num]
	maskdata[0].data = data
	maskdata.flush()

	return 0

# def chdr(filename):

#     with fits.open(filename, 'update') as mask:

#       mask[0].header['NAXIS'] = '2'
#       mask[0].header['NAXIS3']
#       mask[0].header['NAXIS4']

#       mask.flush()


# step= '0'
#
recipe = stimela.Recipe("Test clean mask making", ms_dir=MSDIR)
# recipe.add("cab/cleanmask", step,
# {
# "image"		: image+":output",
# "output"	: fa1_cleanmask+":output",
# "dilate"	: False,
# "sigma"		: 15,
# "no-negative"   : True,
# },
# input=INPUT, 
# output=OUTPUT,
# label="Make a mask out of clean image clean image")


step = '1'
recipe.add('cab/fitstool', step,
{
"image"         : [fa1_cleanmask+':output',fornax_mask+':output'],
"output"        : merged_mask,
"force"			: True,
"sum"           : True,
},
input=INPUT,
output=OUTPUT,
label="Masks merged")


recipe.add(divide_nonzero, 'normalize masks to values 0,1', 
{ 
'mask' : OUTPUT+'/'+merged_mask,
}, 
input=INPUT, 
output=OUTPUT,
label='Mask normalized')

step = '2'
#recipe = stimela.Recipe("Multiply model with mask", ms_dir = MSDIR)
recipe.add('cab/fitstool', step,
{
"image"         : [model+':output',merged_mask+':output'],
"output"        : model_corr,
"force"			: True,
"prod"          : True,
"sanitize"		: 0,
},
input=INPUT,
output=OUTPUT,
label = "Model corrected")


# recipe.add(chdr, 'correct header of mask',
# {
# "filename"         : merged_mask+":output",
# },
# input=INPUT,
# output=OUTPUT,
# label='Change header of mask')

recipe.run()
