# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set working directory for the bot
WORKDIR /bot

# Copy the bot files into the container at /bot
COPY ./bot /bot/

# Set working directory back to /code
WORKDIR /code

# Expose the port for the Django app
EXPOSE 8000

# Command to run both Django app and bot
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 & python /bot/main.py"]