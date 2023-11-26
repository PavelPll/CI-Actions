# Run two CICD pipelines for the given Project: on Github VM using Actions and on AWS cloud using Jenkins. 
I installed Jenkins on my Laptop (Built-In Node) and I configured Jenkins agent to run all jobs in AWS cloud (for technical details see **Jenkins_configuration.txt**). CICD pipelines were deveveloped in the following order.
* Define the project for CICD. The code with a short description see in the folder theProject, here in a nutshell: (i) The class is defined in **vendingmachine.py**; (ii) The first version of the Unit testing is in **test_vendingmachine.py**; (iii) The API is givent by **run.py**.
* Write the first CICD pipeline using Github, trigered by each "git push" to the Current repository to keep track of all Code changes in a real time. The steps are (for details see **.github/workflow/control_tests.yaml**): (i) Get access to **theProject** from the Github VM; (ii) Set up Python environment; (iii) Run the first test for all *.py files of **theProject** in order to check for errors, styles and Code complexity; (iiii) Run the second test, **Unit test** only for **test_vendingmachine.py** in **theProject**. This whole pipeline is trigered by each "git push" to the Current repository.
* Write the second CICD pipeline (for details see **Jenkinsfile**). Three stages are included: (i) Build - to launch the AWS instance (if it does not exist) and set up the working environment. I need Python and Docker (this is because latter I will use one Docker image to compile the API to the single binary file); (ii) Test - to run Unit testing and pass the result to Jenkins to be able to see it in a real time using Jenkins UI; (iii) Deliver - to compile the project to sigle binary file and its automatic upload to my laptop from AWS cloud.


cluster on AWS cloud and showed some its important functionalities. 
or






triggered by each git push request to the given project
Unit Testing is done using pytest. Code is checked by flake8.  
maxAllowedNumberOfDrinksInside

> [!NOTE]
> Each project is accompained by intsruction how to run it on Spark cluster in Scala, Java or in Python environment (see the corresponding **How_to_run.txt** files).
