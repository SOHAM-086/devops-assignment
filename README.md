# **Flask with Redis - Dockerized Application**

## **Overview**
This is a simple Flask web application that uses Redis to keep track of the number of visits to the homepage.  
The application is containerized using Docker, and it utilizes Docker Compose to run both the Flask web service and Redis service in isolated containers.  
This setup allows for a scalable and easy-to-deploy application with minimal configuration.

The project includes the following components:
- Flask web server running in a Docker container.
- Redis service running in a separate Docker container.
- Docker Compose configuration to bring up both services together.

---

## **Instructions for Building and Running the Application Locally**

### **Prerequisites**
Ensure that the following are installed on your machine:
1. Docker
2. Docker Compose
3. Terraform ( for provisioning infrastructure)

☛​̳𝙎​̳𝙩​̳𝙚​̳𝙥​̳𝙨​̳ ​̳𝙩​̳𝙤​̳ ​̳𝙍​̳𝙪​̳𝙣​̳ ​̳𝙇​̳𝙤​̳𝙘​̳𝙖​̳𝙡​̳𝙡​̳𝙮 ̳☚
1. Clone the repository:
   ### git add https://github.com/SOHAM-086/devops-assignment.git
   ### cd devops-assignment
2. Build the Docker images:
   Build the Flask app image and the Redis image:
   ### docker-compose build
3. Start the containers:
   ### docker-compose up
4. Access the application:
   ### The Flask application should now be accessible at http://localhost:5000/. Visit the homepage to see the number of visits tracked by Redis
5. To Reset the Visit Count:
   ### docker-compose exec redis redis-cli flushdb

☛​̳𝘿​̳𝙚​̳𝙥​̳𝙡​̳𝙤​̳𝙮​̳𝙢​̳𝙚​̳𝙣​̳𝙩​̳ ​̳𝙎​̳𝙩​̳𝙚​̳𝙥​̳𝙨 ̳☚
 ̲𝖣̲𝗈̲𝖼̲𝗄̲𝖾̲𝗋̲ ̲𝖣̲𝖾̲𝗉̲𝗅̲𝗈̲𝗒̲𝗆̲𝖾̲𝗇̲𝗍͢
1. Build the images:
   ### docker-compose build
2. Run the application in detached mode:
   ###  docker-compose up -d
3. Monitor the application:
   ###  docker-compose ps
4. Access the application:
   ### Visit http://localhost:5000/ to view the Flask app running on your machine.

☛​̳𝙐​̳𝙨​̳𝙚​̳ ​̳𝙏​̳𝙚​̳𝙧​̳𝙧​̳𝙖​̳𝙛​̳𝙤​̳𝙧​̳𝙢​̳ ​̳𝙛​̳𝙤​̳𝙧​̳ ​̳𝙡​̳𝙤​̳𝙘​̳𝙖​̳𝙡​̳ ​̳𝙞​̳𝙣​̳𝙛​̳𝙧​̳𝙨​̳𝙩​̳𝙧​̳𝙪​̳𝙘​̳𝙩​̳𝙪​̳𝙧​̳𝙚​̳ ​̳𝙥​̳𝙧​̳𝙤​̳𝙫​̳𝙞​̳𝙨​̳𝙞​̳𝙤​̳𝙣​̳𝙞​̳𝙣​̳𝙜 ̳☚
   To automate the provisioning of the Docker environment (Flask app and Redis service), you can use Terraform.
   Navigate to the directory containing your main.tf file and run:
1. Initialize the Terraform environment
   ### terraform init
2. Check the execution plan
   ### terraform plan
3. Apply the plan to create infrastructure
   ### terraform apply
   
☛​̳𝙈​̳𝙤​̳𝙣​̳𝙞​̳𝙩​̳𝙤​̳𝙧​̳𝙞​̳𝙣​̳𝙜​̳ ​̳𝙄​̳𝙣​̳𝙨​̳𝙩​̳𝙧​̳𝙪​̳𝙘​̳𝙩​̳𝙞​̳𝙤​̳𝙣​̳𝙨 ̳☚
Basic Monitoring: You can monitor the resource usage of your Docker containers using the following command
1. Docker stats: To view CPU and memory usage for your containers
   ### docker stats
2. Logs: To check logs for the Flask container
   ### docker logs <container-id-or-name> i.e. docker logs flask_app
   
   
