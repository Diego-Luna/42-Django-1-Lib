FROM debian:bullseye-slim

# Evitar interacciones durante la instalación de paquetes
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    postgresql \
    postgresql-contrib \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirement.txt .
COPY my_script.sh .

# Dar permisos de ejecución al script
RUN chmod +x my_script.sh

# Comando por defecto al iniciar el contenedor
CMD ["/bin/bash"]