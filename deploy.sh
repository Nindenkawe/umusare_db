#!/bin/bash

# Set variables
PROJECT_ID="kopee-fe291"
REGION="us-central1"
IMAGE_NAME="kopee:django-l-dev"
SERVICE_NAME="kopee-api-service"
REGISTRY_REPOSITORY="kopee-api-test"
IMAGE_URI="us-central1-docker.pkg.dev/$PROJECT_ID/$REGISTRY_REPOSITORY/$IMAGE_NAME"

docker build -t $IMAGE_URI .
# Tag the image for Artifact Registry (assuming Dockerfile is in the current directory)
docker tag . $IMAGE_URI

# Push the image to Artifact Registry
docker push $IMAGE_URI

# Deploy to Cloud Run (using correct service account flag)
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE_URI \
  --region $REGION \
  --platform managed \
  --allow-unauthenticated \
  --project $PROJECT_ID \
  --service-account=624155180669-compute@developer.gserviceaccount.com