#!/bin/bash

python3 -m venv django_venv

# * Activar el entorno virtual
source django_venv/bin/activate

# * Instalar los requisitos desde el archivo requirement.txt
# ? se nesesita tener inataldo "postgresql"
pip install -r requirement.txt


# * Mantener el entorno virtual activado
echo "The django_venv virtual environment is now enabled."
echo "--> To deactivate it, type 'deactivate'"
exec $SHELL