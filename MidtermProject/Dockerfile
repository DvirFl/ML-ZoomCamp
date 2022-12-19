FROM continuumio/miniconda3

# Create the environment:
COPY midprojenv.yml .
# RUN conda env create -f midprojenv.yml 

# Override default shell  and use bash
SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]
 
# Activate the environment, and make sure it's activated:
# RUN conda activate env

# RUN echo "Make sure flask is installed:"
# RUN python -c "import flask"

# The code to run when container is started:
COPY ["train.py", "predict.py", "model.bin", "./"]


EXPOSE 5000

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "predict:app"]

