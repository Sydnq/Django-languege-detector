# Django-languege-detector
A simple implementation of language detector using Django and scikit-learn

The following apps are in this package:

	* detector: responsible for language detection. The detector uses scikit-learn language assigment model to the detect language for more info see: 
		- https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html (Exercise 1: Language identificatio)
 
	Using manage.py the model can ben trained. In addition, more data can be supplied to for instance add a new language. of course when adding new data to the dataset the model must be retrained. 
	* Events: at the moment as simple event detector, which keeps track of how the detector is used, which langauges are detected and what kind of text is commonly supplied. This will be expanded and more features will ben added.

	TODOS:
		- add user management
		- add error logging 
		- add Apis 
