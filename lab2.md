# Intelligent Bots with the Azure Bot Service

## QnA Maker and Azure Bot Service

 1. Intro

 	With QnA Maker user can create knowledge bases that can be used later on to power Bot. 
 	QnA Maker lets you create bot for given knowledge base.

 	Knowlede base can be created in varriety of ways: REST API/native SDK library or, as you may expect from Azure, with use of gui in QnA Maker portal. QnA Maker can be provisioned during creation of Knowledge Base, so there is no need to create one beforehand. Questions can be imported from file/data source or inserted manually. Built-in natural language processing matches questions and answers, event if they are not exact as defined in knowleg base.
 	Azure Bot Service is about creation and managing Bots lifecycle.

2. Use cases 
	 - Bot for handling user calls at call centers. Interacting with answering machine by inserting 0-9 numbers on phone allows only one way communication (service gets information from caller). But with use of Bot in such a scenarios, user could also extract information and decide whether there is sens to continue call and if problem that user faced can be resolved.


3. Usage
	
	Prepare machine learning environment:
	- Create machine learning worksapce in Azure portal.
	- Login to machine learning studio at  https://ml.azure.com and create Computing Instance.
	- Ensure you have created notebook. Notebook should be connected with your Computing instance.
	- Create QnA maker resource (with Azure search, App Service)
	- Create Knowledge Base and and connect to QnA service.
	- Populate knowledge base.
	- Create Chat bot with Chat Bot service, you can use autocomplete feature after creating knowledge base.
	- Creat App registration in AAD -> App registrations center for bot.


4. Pricing (Region: West Europe)

Q&A
	F0 - free (3 RPS, 50 000k transactions per month, 100k transactions per month, documents sieze < 1MB)
	S0 - Standard (3 RPS, 100k transactions per month)

Azure search:
	F0 - FREE (3 indexses)



## Bot Framework Composer

1. Intro

	Bot Framework Composer is so called "no code" tool to build conversational bots.
	It has a visual designer that simplify process of creating bot and setting up environment.


2. Usage

	- Install desktop app.
	- Use GUI to create desired bot. Insert questions/inputs/dialogs, assign user responses to properties.


3. Pricing

	Depends on used services.
