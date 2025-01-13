# Use Python 3.12 slim image as the base
FROM python:3.12.0-slim-bookworm

# Set environment variables
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# Set working directory
WORKDIR $APP

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc libpq-dev musl-dev

# Copy requirements file and install Python dependencies
COPY requirements.txt $APP
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . $APP

# Expose port for the application
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Define entrypoint and default command
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
