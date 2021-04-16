
**Anomaly Detection**
(also known as Outlier Detection) is an exciting yet challenging field, which aims to identify outlying objects that
 are deviant from the general data distribution. 
Outlier detection has been proven critical in many fields, such as credit card fraud analytics, network intrusion detection, and mechanical unit defect detection.


**Interoperability Anomaly Detection**
This repository aims for the implementation of a machine learning process to improve the reliability of a data exchange system with 
the prediction of dysfunction events and the deduction of acceptability thresholds based on an analysis of usual behaviors / unusual exchanges 
among a set of data collected from RabbitMQ and consoleSaasUserAccess.



**Project structure**
Here is the explantation of folder strucure:

    
*  src: Stores source code (python mainly) which serves multiple scenarios. 
    During data exploration and model training, we have to transform data for particular purpose. We have to use same code to transfer data during online prediction as well.
    So it better separates code from notebook such that it serves different purpose(for example: redundant functions for multiple use cases)

    
*  test: In R&D, data science focus on building model but not make sure everything work well in unexpected scenario.
  When deploying model to API,test cases guarantee backward compatible issue but it takes time to implement it.
  
*   model: Folder for storing binary (json or other format) file for local use.
    
*  data: Folder for storing subset data for experiments. It includes both raw data and processed data for temporary use, results for possible temporary results outside of 
the project scope
    
*  notebook: Storing all notebooks including EDA and modeling stage.

