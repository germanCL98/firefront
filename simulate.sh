#!/bin/bash
echo "====== Ejecutando Simulación ========"

# el archivo landscape.nc debe estar en el mismo directorio en el que se ejecuta forefire
cd examples/custom
CUSTOM_DIR=$(pwd)

# ejecuta la simulación y crea el ffgeojson
forefire -i result.ff

# vuelve a la carpeta raiz
cd ../../
python py3_tools/ff_to_geojson.py -input_dir "$CUSTOM_DIR"
