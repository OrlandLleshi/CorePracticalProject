# **CorePracticalProject**

## **Table of contents**

1. [Project](#project) 
    - [Aims](#aims) 
    - [Project sections](#project-sections)

2. [Planning stages](#planning-stage)
    - Trello
    - ERD
    - Risk Assessment

3. [Product](#product)

4. [Testing](#testing)

5. [Issues](#issues)

## **Project**
### Aims
##### The aim of this project is to create a multi service product that can randomly generate two random values for a user and based upon these values, a final value will be generated.

### Project sections 
##### This project follows the CI pipeline which can be seen below. 

##### The CI pipeline consists of a development stage, project tracking stage, version control, unit testing, Jenkins, automation, external load balancing and a live environment. This project looks at integrateing multiple services together within the same network. Service 1 interacts directly with the user. Services 2 and 3 generate random objects for the user while service 4 automatically generates the last object which the user will see as these objects are sent back to service 1. 

## Planning Stage
##### Before the building of any project can begin, it is important to go through the planning stage of the project. The planning stage of this project consisted of a trello board with user stories and tasks, a small ERD that shows the tables used in this project and a risk assessment. 

## **Product**
##### The product in question is a random story generator. This product will generate a random character name, then the third service will generate a random back story for the user. The fouth service will generate and ending based on the random choice of the previous two. These services work concurrently as they are all on the same network and can be connected to one another through the swarm. We can configure these different machines and help to deploy them through the use of ansible. Jenkins would be used to automatically build, update and deploy the application.

## Testing
##### Another very important aspect of the development of an application would be the testing section of an application. This needs to be done before the build to ensure that each section of the application, more specifically the backe nd of the application, functions properly with next to no issues. The test coverage of each service can be observed in the section below. 

## Issues 
##### As with any project, some issues were faced in this project. The most significant of which was Jenkins. The build in Jenkins was fairly successful apart from the deployment stage. At first, Jenkins failed to deploy the product. After some troubleshooting, the product was able to deploy but when trying to access the product through the NGINX IP adress I was met with a 502 error. This could be fixed in the future with further troubleshooting. 