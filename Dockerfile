FROM continuumio/miniconda3:23.10.0-1

WORKDIR /app

COPY ./multipage_app multipage_app
RUN conda env create -f ./multipage_app/environment.yml

COPY ./.streamlit .streamlit

CMD [ "conda", "run", \
      "--no-capture-output", \
      "-n", "bbba-flowers", \
      "python", "-m", "streamlit", "run", "./app.py", \
      "--server.port", "80" \
    ]
