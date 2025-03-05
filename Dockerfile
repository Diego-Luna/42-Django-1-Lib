FROM debian:bullseye-slim

# Evitar interacciones durante la instalación de paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Instalar paquetes necesarios y herramientas adicionales
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    postgresql \
    postgresql-contrib \
    libpq-dev \
    zsh \
    git \
    curl \
    wget \
    vim \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configurar oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Configurar zsh como shell por defecto
RUN chsh -s /usr/bin/zsh root

# Personalizar oh-my-zsh (opcional)
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="bira"/' ~/.zshrc && \
    echo "plugins=(git)" >> ~/.zshrc

# Crear directorio de trabajo
WORKDIR /app

# Dar permisos de ejecución al script
# RUN chmod +x my_script.sh

# Comando por defecto al iniciar el contenedor
CMD ["zsh"]