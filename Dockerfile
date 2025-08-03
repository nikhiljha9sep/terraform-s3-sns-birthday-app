# Step 1: Base image
FROM python:3.9

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files
COPY . .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Set environment variables (placeholders for AWS creds)
# These will be overridden when running docker run
ENV AWS_ACCESS_KEY_ID="**********"
ENV AWS_SECRET_ACCESS_KEY="************"
ENV AWS_DEFAULT_REGION="us-east-1"

# Step 6: Expose Flask port
EXPOSE 5000

# Step 7: Start Flask app
CMD ["python", "app.py"]
