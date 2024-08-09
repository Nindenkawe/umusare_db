# Use a smaller, more efficient base image for Cloud Run
FROM python:3.9-slim-buster

# Set environment variables for optimization
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt ./

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port that your Django app will listen on
EXPOSE 8080

# Define the command to run your Django app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "kopee.wsgi:application"]