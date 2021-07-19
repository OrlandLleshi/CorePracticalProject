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
##### The brief for this project stated that four services would need to be created for this project. The first would refer to a HTML page and would show the user the outcome of a set of randomly generated objects. Services 2 and 3 would generate these objects for the user and the final service would perform an action based on the initial two. 

##### There are a number of tools to be used in this project including trello boards, databases, version control and cloud configuration.

#### This project follows the CI pipeline which can be seen below. 

![CI Pipeline](https://i.imgur.com/FzomtV1.png)
##### The CI pipeline consists of a development stage, project tracking stage, version control, unit testing, Jenkins, automation, external load balancing and a live environment. This project looks at integrateing multiple services together within the same network. Service 1 interacts directly with the user. Services 2 and 3 generate random objects for the user while service 4 automatically generates the last object which the user will see as these objects are sent back to service 1. 

#### Original Services 
![Original](https://i.imgur.com/sEPUdpu.png)

#### Updated 
![Updated](https://i.imgur.com/yFGBYwn.png)


##### The project that I have chosen to embark on looks at enerating a random character name and background story for the user. Based on these two factors, an ending to the story can be generated and returned to the user.

## Planning Stage
##### Before the building of any project can begin, it is important to go through the planning stage of the project. The planning stage of this project consisted of a trello board with user stories and tasks, a small ERD that shows the tables used in this project and a risk assessment. 


#### ERD
This ERD shows the database that will be used within this project. There will be only one table and hence no relationships can be seen.
![ERD](https://i.imgur.com/UwSJRzf.png)

#### First Trello 
This is the original trello that was created when first approaching the project which looks at the main functionality needed.
![FirsT Trello](https://i.imgur.com/sy7vGnm.png)
#### Final Trello 
This is the finalised trello board at the time of handing in this project. 
![Evolved](https://i.imgur.com/nyA9fdB.png)

#### First Risk Assessment
This is the original risk assessment when first approaching the project.  
![First Risk Assessment](https://i.imgur.com/eXKeq3L.png)

#### Final Risk Assessment
This is the final risk assessment which looks at multiple aspects of the project  
![Evoveld](https://i.imgur.com/jWtkIAh.png)

## **Product**
##### The product in question is a random story generator. This product will generate a random character name, then the third service will generate a random back story for the user. The fouth service will generate and ending based on the random choice of the previous two. These services work concurrently as they are all on the same network and can be connected to one another through the swarm. We can configure these different machines and help to deploy them through the use of ansible. Jenkins would be used to automatically build, update and deploy the application.

![App](https://i.imgur.com/TQA5r7b.png)
![Updated](https://i.imgur.com/XRC9eBU.png)
These images above show the randomly generated story of the project


## Testing
##### Another very important aspect of the development of an application would be the testing section of an application. This needs to be done before the build to ensure that each section of the application, more specifically the backe nd of the application, functions properly with next to no issues. The test coverage of each service can be observed in the section below. 

#### Service 1 
This shows the test coverage run on service 1 which looked at perform get and post requests to other services
![service1](https://i.imgur.com/KLVRMb5.png)
#### Character
This is a simpler test as this involved only testing that the randomly generated name was correct and within the list of names specified
![caharacter](https://i.imgur.com/DQfassv.png)
#### Background 
This much of the same for the background also 

![background](https://i.imgur.com/CPWMBCi.png)
#### Endpoint 
The testing within this looked at testing the other randomly generated objects to generate a good or bad ending for the user.  
![endpoint](https://i.imgur.com/pCGwFdU.png)
## Issues 
##### As with any project, some issues were faced in this project. The most significant of which was Jenkins. The build in Jenkins was fairly successful apart from the deployment stage. At first, Jenkins failed to deploy the product. After some troubleshooting, the product was able to deploy but when trying to access the product through the NGINX IP adress I was met with a 502 error. This could be fixed in the future with further troubleshooting. 