FROM python:alpine
RUN addgroup -S colloquio && adduser -S colloquio -G colloquio 
WORKDIR /app
COPY main.py .
RUN chown colloquio:colloquio main.py && chmod 500 main.py
USER colloquio
CMD python main.py
