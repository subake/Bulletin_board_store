FROM python:3.6-stretch

# Create a no-root user
RUN adduser --system --group --no-create-home app

# Copy app inside container
COPY . /app

# Make the working directory
WORKDIR /app

# Install  requirements.txt
RUN pip install -r requirements.txt

# Hand everything over to the user 'app'
RUN chown -R app:app /app

# Run all subsequent commands as user 'app'
USER app
