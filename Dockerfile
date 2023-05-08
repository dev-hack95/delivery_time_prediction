FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python src/pipeline/training_pipeline.py
EXPOSE 8501
CMD python app.py