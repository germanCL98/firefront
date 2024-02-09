PHONY: test

# test en coordenadas dentro de las capas de dem y landcover de examples/custom
test: examples/custom/fuels.ff examples/custom/elevation.tif examples/custom/landcover.tif
	python py3_tools/coord_to_ff.py --lat 38.089620 --lon -4.231540 --crsout 25830 examples/custom/landcover.tif examples/custom/elevation.tif examples/custom/landscape.nc examples/custom/result.ff
