FROM python
WORKDIR /web
RUN pip install flask
RUN pip install pymongo
COPY app*.py .
EXPOSE 5000
ENTRYPOINT [ "python", "app*.py" ]