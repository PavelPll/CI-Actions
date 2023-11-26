## Run CICD pipeline for the given Project on AWS cloud using Jenkins and githubActions 
I installed Jenkins on my Laptop (Built-In Node) and I configured Jenkins agent to run all jobs in AWS cloud (for technical details see **Jenkins_configuration.txt**). The CICD pipeline was deveveloped in the following order.
* Define the project for CICD. The description of the project, in a nutshell: The class VendingMachine **_(the subclass of the class Drink)_** can be filled by Drinks **_(Jus or Datacola - other child of the class Drink)_** in two kinds of beverageContainer **_(can or bottle)_** with different numbers of days before expiration. The code see in the folder theProject: (i) The class is defined in **vendingmachine.py**; (ii) The first version of the Unit testing is in **test_vendingmachine.py**; (iii) The API is givent by **run.py**.




cluster on AWS cloud and showed some its important functionalities. 







triggered by each git push request to the given project
Unit Testing is done using pytest. Code is checked by flake8.  
maxAllowedNumberOfDrinksInside

# OBJECTIVE: To get familiar with Spark.
I installed Spark cluster on AWS cloud and showed some its important functionalities. 
* The file **spark_installation.txt** describes the installation procedure. This is done on top of a Hadoop YARN cluster, which I installed previously (for details see [Hadoop-Hive](https://github.com/PavelPll/Hadoop-HIVE) project in the current git repository).  
* The folder **./Scala_ETL** contains the example of ETL (Extract Transfer Load) pipeline written in Scala.
* The folder **./Java_ML** contains the example of simple machine learning pipeline in Java.
* The example of data batch processing with Spark (**./Streaming**).
> [!NOTE]
> Each project is accompained by intsruction how to run it on Spark cluster in Scala, Java or in Python environment (see the corresponding **How_to_run.txt** files).
