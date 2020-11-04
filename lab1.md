# Text evaluation with Azure Cognitive Language Services

Modules included in Azure Cognitive Language Services:

## Content Moderator

 1. Intro

	Content Moderator provides machine-assisted content moderation for images, text, and video.
Conntent Moderator offers Text Moderation API. Data is returned from API in json format. Data contains information about text passed to the API. API has three modes:
- extracting blacklisted words from text (Profanity)
- classifing text to one of three predefined categories. In this mode API measures the fit factor for given category. Categories sensitivite changes from identifying sexually explicit phrases to hate speach.
- extracting sensitive data from text like email/ip adresses, hone numbers (Personally identifiable information - PII)

2. Use cases 
	Service may be use to:
	 - prevent from breaking RODO law when texts are published publicly. (PII)
	 - filtering out offensive messages in chats/social media apps/comments (Profanity + Classification)


3. Usage
	Copy the subscription key from Content moderator resource. You can use request builder with gui at: 
	https://westus.dev.cognitive.microsoft.com/docs/services/57cf753a3f9b070c105bd2c1/operations/57cf753a3f9b070868a1f66f

	Sample curl that can be used to verify serivce:
```
curl -v -X POST "https://westus.api.cognitive.microsoft.com/contentmoderator/moderate/v1.0/ProcessImage/Evaluate?CacheImage={boolean}"
-H "Content-Type: application/json"
-H "Ocp-Apim-Subscription-Key: {subscription key}"

--data-ascii "{body}"
```

4. Pricing (Region: West Europe)
F0 - free (1 RPS, 5k transactions per month)
S0 - Standard (10 RPS , 1$ for 1mln transactions; price is getting lower for bigger chunks)


## Language Understanding Intelligent Service (LUIS)

1. Intro
LUIS uses certain aspects of the text to pull out relevant detailed information. LUIS aids the AI algorithm in making comparisons and distinctions. LUIS allows you to map natural language utterances to intents.

2. Use cases:
Everywere were we want to map users input utterances to intents.
 - Registering the support complaint via chat-bot.
 - Booking table/ticket/meal via sms message (service backed with LUIS API).

3. Usage:
Create LUIS resource. Create LUIS app https://eu.luis.ai/. Add intents and entities.
Map search subjects to the facet entity. Train the LUIS model with use of utterances you inserted.
Create a public endpoint for the LUIS service and publish the app. Application can be embedded in
client applications, tested in a browser and connected a bot.

4. Pricing (Region: West Europe)
F0 (free) - (5 RPS; 10k transacations per month)



## Text Analytics API

1. Intro
Text Analytics is about understanding and analyzing unstructured text to discover sentiment, extract key phrases and detect entities from text.

2. Use cases:
	- Analysis of users messages about our app(recognised as entity) to detect users overall feeling about app and detect places to upgrade.
	- Automatically set users locale/i18n based on language recognized in users message.

3. Usage:
 Generate Text Analytic saccess key in Marketplace. Use form to verify api and create sample requests. https://westeurope.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-1-Preview-1/operations/Sentiment/console
API is versioned in url parameter https://tekstalanyticszasob1.cognitiveservices.azure.com/text/analytics/v3.1-preview.1/sentiment.


```
curl -v -X POST "https://westus.api.cognitive.microsoft.com/text/analytics/v3.1-preview.1/sentiment?model-version={string}&showStats={boolean}&opinionMining={boolean}&stringIndexType={string}"
-H "Content-Type: application/json"
-H "Ocp-Apim-Subscription-Key: {subscription key}"

--data-ascii "{body}"
```

