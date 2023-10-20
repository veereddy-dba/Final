                                                         ------------------  **Capstone Project Overview**  ------------------  

                                                             

Final project of Cloud DevOps Engineer Courses to apply our skills/knowledge on various Cloud DevOps topics which we learned throughout this course. , The purpose of the Cloud DevOps capstone project is to give you a chance to combine what we have
learned throughout the program. This project helps us an important part of individuals portfolio that will help to achieve our cloud development-related career goals.

In My Final Capstone project, I have created - Continuous deployment pipeline to deploy a simple flaskapp Application on AWS EKS cluster using CircleCI 

Major Components I used for this Project as below.

- CircleCI
- AWS EKS (Kubernetes)
- Dockerhub
- Github

1.	Create the CircleCI account,addd following AWS credentials as environment variables to Configure
    
    **AWS_ACCESS_KEY_ID**
  	**AWS_SECRET_ACCESS_KEY**
  	**AWS_DEFAULT_REGION**
  	**Docker user**
  	**Docker pass**

  	as CircleCI project or context environment variables.

3.	Create a GitHub repository.

High level Implementation steps of this projects is.

A.	Create a flaskapp app.py file and ensure it is working.

B.	Create a Docker File

C.	Build and tag the image.

D.	Push the image to Docker Hub

E.	Create EKS cluster.

F.	Create Deployment and Service for EKs cluster.

