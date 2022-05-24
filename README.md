# KGISL-SIH-RV6-google-search-RPA
                                    Google search Using Robotic process automation (RPA)
              
In recent framework, with huge development in the classic information retrieval system and use of the internet, searching and retrieving accurate information from the web still challenging task to research users. Our proposed system uses Robotic process automation (RPA) methods for searching information from Google and present the information in user requested format. Numerous RPA system was exist in the world which was used for different automation process.  The proposed system consist of three different components such as, Finding the user requested information, building the model using python standard URL Libraries function  and Regular Expression and presenting the information in user requested formats (Table format, CSV,Tex).


Prerequisites
Python 3.0 IDLE.   

Installing
Python Library Flies to be install       
Googel search 
pip install google (use Command promt to install)
url: https://pypi.org/project/google  

Running the Source Code:

Step1 :First Run the Google_search_Module.py

Google_search_Module.py(It retrive URL of Top 20 links from  google Pages and it is saved in urlresults.doc files then it will process the reterived each  URL links saved in that file and result saved in Hotel details.CSV files.)
Step 2 : 

Tag_and_URL_Process.py (This file is automatically process the each URL retreived from the previous results and it open the sublink of the each URLS according to the user input)

Step 3:

Regular_Expression.py ( This file used to fetch the desired output (Such as Name,contact Number,Address, Email ID) by processing the URL links

Sample RPA  APllication 

Sample _RPA _Apllication.py ( This files  will automatically give the Sensex result of Top company by using RPA Techniques) 

Future Work: 
        In Future work our team is working towards integrating Machine learning and Artificial intelligence algorithm into RPA Techniques.  


