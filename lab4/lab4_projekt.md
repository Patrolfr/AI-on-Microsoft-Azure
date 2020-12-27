# Feedback Supplier

### Use case
	System (or rather command line app) that automatically resolves feedback from audience.
Given picture with group of people system will resolve faces of all people (e.g. lecture participants) with set of emotions that each person fells. Could be used for content alike measurements where picture of people could be taken.

### Architecture:
- Face API
- Custom Vision Training
- Custom Vision Prediction
- Python for service integration, image processing and html generator

### Run program: `python feedback.py <urlToImage>`  
	Navigate to generated `feedback.html` file to view generated raport.

Youtube: https://youtu.be/pzYHPAlwU7I