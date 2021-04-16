# config.py

from pathlib import Path  

#change path according to user's properties:
#data_dir = Path('/path/to/some/logical/parent/dir')

raw_data_dir = Path("D:/Users/Syrine.benaziza/Documents/Project/interoperability-anomaly-detection/data/raw/v1")
raw_data_v2 = Path("D:/Users/Syrine.benaziza/Documents/Project/interoperability-anomaly-detection/data/raw/v2")

proc_data_dir = Path("D:/Users/Syrine.benaziza/Documents/Project/interoperability-anomaly-detection/data/processed")
results_data_dir = Path("D:/Users/Syrine.benaziza/Documents/Project/interoperability-anomaly-detection/data/results")

#Saas Data paths 
raw_saas_v1 = raw_data_dir / 'saas.csv'   
raw_saas_v2 = raw_data_v2 / 'consolesaasevents.csv'

##V1
proc_saas_min_v1 = proc_data_dir / 'saas_min_v1.csv'  
proc_saas_sec_v1 = proc_data_dir / 'saas_sec_v1.csv' 

##V2
proc_saas_min_v2 = proc_data_dir / 'saas_min_v2.csv'  
proc_saas_sec_v2 = proc_data_dir / 'saas_sec_v2.csv' 
 

#----------------------------------------------

#RabbitMQ paths
raw_evts_v1 = raw_data_dir / 'evts.csv'   
raw_evts_v2 = raw_data_v2 / 'rabbitmqeventsprod.csv'

##V1 DATASET
min_evts_v1 = proc_data_dir / 'evt_min_v1.csv' #rabbitmq events regrouped by minute ,initial dataset
sec_evts_v1 = proc_data_dir / 'evt_sec_v1.csv' #rabbitmq events regrouped by sec ,initial dataset


##V2 DATASET 
min_evts_v2 = proc_data_dir / 'evt_min_v2.csv' #rabbitmq events regrouped by minute ,initial dataset
sec_evts_v2 = proc_data_dir / 'evt_sec_v2.csv' #rabbitmq events regrouped by sec ,initial dataset



#----------------------------------------------
# Then, in notebooks, import these variables using this line
    #from config import *

#Paths defined in Config file python:

    #Saas Paths
        ##V1
            #raw_saas_v1         csv file containing original saas data V1 (not modified)    
        
            #proc_saas_min_v1    csv file containing processed saas data V1 (grouped by the min)
            #proc_saas_sec_v1    csv file containing processed saas data V1 (grouped by the sec)

        ##V2
            #raw_saas_v2         csv file containing original saas data V2 (not modified)  
                    
            #proc_saas_min_v2    csv file containing processed saas data V2 (grouped by the min)
            #proc_saas_sec_v2    csv file containing processed saas data V2 (grouped by the sec)
        
    #RabbitMQ paths         
        ##V1
            #raw_evts_v1
            
            #min_evts_v1 
            #sec_evts_v1 
            
        ##V2
            #raw_evts_V2  
            
            #min_evts_v2 
            #sec_evts_v2 