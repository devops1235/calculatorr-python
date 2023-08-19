FROM python
WORKDIR /app
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
