FROM python
WORKDIR /web
RUN pip install flask
COPY app.py .
EXPOSE 5000
ENTRYPOINT [ "python", "app.py" ]
