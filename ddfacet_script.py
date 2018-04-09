import stimela

INPUT="input"
OUTPUT="output"
MSDIR="msdir"

recipe = stimela.Recipe("Test DDFacet imaging", ms_dir=MSDIR)
recipe.add("cab/ddfacet", "ddfacet_test",
{
"Data-MS": ["fa1_conc.ms"],
"Output-Name": "test_ddfacet",
"Data-ColName": 'CORRECTED_DATA',
"Selection-Field": 1,
"Data-ChunkHours": 0.5,
"Image-NPix": 8000,
"Image-Cell": 1.6,
"Output-Images": "all",
"Cache-Reset": True,
"Facets-NFacets": 21,
"Freq-NBand": 3,
"Freq-NDegridBand": 6,
"Weight-Mode": 'Briggs',
"Weight-ColName": "WEIGHT",
"Weight-MFS": True,
"Deconv-Mode": "Hogbom",
"Beam-Model": 'FITS',
"Beam-FITSFile": "'MeerKAT_VBeam_10MHz_53Chans_$(xy)_$(reim).fits'",
"Deconv-PeakFactor": 0.4,
"Deconv-FluxThreshold": 3.0e-5,
"Beam-FITSMAxis": "'-Y'",
"Log-Boring": True,
"Log-Memory": True,
},
input=INPUT, output=OUTPUT, shared_memory="250gb",
label="test_image:: Make a clean image using ddfacet")

recipe.run()
