FROM python
WORKDIR /app
RUN pip install --no-cache-dir -r requirement.txt
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
