# predictive_model_grievance-_redressal
Working:

When a citizen logs in on the CPGRAMS website, he/she has to fill up an MCQ form. 
Then the response of the citizen is recorded.
The grievance is extracted from the response and is structurized in the form of a string.
This string is appended to the test set for further process of testing.
Then it is checked if the string exists in the training set. Then the index of the position of the string is returned. 
To predict the timeline of resolution of the grievance, the timeline corresponding to the index is returned as the prediction.
The prediction can be viewed by the citizen on the CPGRAMS website.
This is how our predictive model works along with the website.
