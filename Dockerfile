FROM continuumio/miniconda
SHELL ["/bin/bash","-c"]
WORKDIR /usr/project/met_forecast
COPY . ./
RUN conda update -n base -c defaults conda -y &&\
    conda env create -f environment.yml &&\ 
    conda init bash
    # echo "conda activate ops-api" > ~/.bashrc
RUN ./run.sh
ENTRYPOINT ["tail", "-f", "/dev/null"]