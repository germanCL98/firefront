PHONY: test

test: examples/custom/fuels.ff examples/custom/elevation4326.tif examples/custom/landcover4326.tif
	python py3_tools/coord_to_ff.py	examples/custom/landcover4326.tif examples/custom/elevation4326.tif examples/custom/landscape.nc examples/custom/result.ff