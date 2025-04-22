# **Microservices CI/CD Pipeline**

This project demonstrates the use of **GitHub Actions** for a **CI/CD pipeline** to automate the building, pushing, and deployment of Docker images to **Amazon Elastic Container Registry (ECR)**, followed by deployment to **Amazon Elastic Kubernetes Service (EKS)**. The pipeline handles three services: **User Service**, **Order Service**, and **Payment Service**.

## **Overview**

This project provides a fully automated pipeline for:

- **Dockerizing the services.**
- **Pushing Docker images to Amazon ECR.**
- **Deploying to Amazon EKS using Kubernetes.**

The entire pipeline is triggered on every push to the `master` branch, ensuring that the latest code is automatically built, tested, and deployed.

## **Technologies Used**

- **GitHub Actions**: Automates the CI/CD pipeline.
- **Docker**: Containerizes microservices.
- **Amazon ECR**: Hosts Docker images in a private repository.
- **Amazon EKS**: Deploys the services to a Kubernetes cluster.
- **Kubernetes**: Manages deployments on EKS.

## **Setup and Configuration**

### **Prerequisites**

- **AWS Account**: Ensure you have an AWS account with ECR and EKS set up.
- **GitHub Repository**: Your repository should contain the code for **User Service**, **Order Service**, and **Payment Service** within the `microservices-project` directory.
- **AWS Credentials**: Store your `AWS_ACCESS_KEY` and `AWS_SECRET_ACCESS_KEY` in GitHub Secrets for access within the pipeline.
- **EKS Cluster**: A working EKS cluster with `kubectl` configured to interact with the cluster.

### **Configuration**

1. **Create an ECR Repository**: Create repositories in ECR for **user-service**, **order-service**, and **payment-service**.
2. **Set up GitHub Secrets**: In your GitHub repository, configure the following secrets:
   - `AWS_ACCESS_KEY`
   - `AWS_SECRET_ACCESS_KEY`
3. **Pipeline Configuration**: The `.github/workflows/ci-cd.yml` file configures the CI/CD pipeline. Ensure it is present and correctly configured.

## **CI/CD Pipeline Workflow**

The **GitHub Actions** pipeline is defined in the `ci-cd.yml` file. Here's a breakdown of the steps:

1. **Checkout Code**: The latest code is checked out from the repository.
2. **Set up AWS Credentials**: AWS credentials are configured using GitHub secrets.
3. **Log in to Amazon ECR**: Authenticates Docker to Amazon ECR using the provided credentials.
4. **Build & Push Docker Images**:
   - For each microservice (**user-service**, **order-service**, **payment-service**), a Docker image is built and pushed to the respective ECR repository.
5. **Set up kubectl for EKS**: Configures `kubectl` to interact with the EKS cluster.
6. **Deploy to EKS**: The services are deployed to EKS using Kubernetes manifests (`user-deployment.yaml`, `order-deployment.yaml`, and `payment-deployment.yaml`).


## **File Structure**

/.github /workflows ci-cd.yml 
# GitHub Actions workflow file for CI/CD /microservices-project    
 / user-service Dockerfile 
# Dockerfile for user service 
/order-service Dockerfile 
# Dockerfile for order service 
/payment-service Dockerfile 
# Dockerfile for payment service 
/k8s 
user-deployment.yaml 
# Kubernetes deployment for user service 
order-deployment.yaml 
# Kubernetes deployment for order service 
payment-deployment.yaml 
# Kubernetes deployment for payment service


## **Example Code**

Here are the basic `main.py` files for each service (**User**, **Order**, and **Payment**) to demonstrate the entry points of the microservices.

### **/user-service/main.py**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "User Service is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

## Example Dockerfile
Here is an example of a Dockerfile for one of the services (User Service):

# dockerfile

```python
# Use Python 3.8 as the base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy the requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Run the application
CMD ["python", "main.py"] 
```

Here’s an example Kubernetes deployment file (user-deployment.yaml) for one of the services:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
        - name: user-service
          image: 717279687729.dkr.ecr.us-east-1.amazonaws.com/user-service:latest
          ports:
            - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer 
```

## How to Contribute
Fork the repository.
Create a feature branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-name).
Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


