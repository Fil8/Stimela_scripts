from astropy.io import fits
import sys

def freq_to_vel(filename):
	
	C = 2.99792458e5
	HI = 1.4204057517667
	
	with fits.open(filename, mode='update') as cube:

		headcube = cube[0].header

		if headcube['RESTFREQ']:
			RESTFREQ = float(headcube['RESTFREQ'])
		else:
		 	RESTFREQ = HI

		endfreq = float(headcube['CRVAL3'])+float(headcube['CDELT3'])*float(headcube['NAXIS3'])
		startfreq = float(headcube['CRVAL3'])

		headcube['CDELT3'] = str(C* (endfreq-startfreq)/RESTFREQ/ float(headcube['NAXIS3']))
		headcube['CRVAL3'] = str(C *(1-startfreq/RESTFREQ))

		cube.flush()


if config[key].get('freq_to_vel', False):

	cubename=pipeline.prefix+'_HI.image.fits:output'

	recipe.add(freq_to_vel, 'switch to velocity', 
		{ 
			'filename' : cubename,
		}, 
		input=pipeline.input, 
		output=pipeline.output,     
		label='Convert velocity of {0:s}'.format(cubename))