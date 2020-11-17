# Cognitive Speech Services

 1. Intro

 	Speech-to-text (or speech recognition) enables trancripts audio streams into text by means of AI and ML. Service can be consumed by REST API or dedicated Speech SDK. Services are designed for real-time translation.
 	The speech-to-text service falls on default, Microsofts language model, but customizations are allowed.

 	Text-to-speech (or voice synthesizing) generates spoken words from input text. User can choose from collection of synthesized voiced.

 	Speech Translation provides ML and AI backed services focusing specifically on the real-time multi-language translation of speech.


2. Use cases
	- classifying audio content as inappropriate for children by converting speech-to-text and forwarding to content moderator
	- working as recognition/sythesization layer in voice interfaces

3. Usage

	To access your Speech Service you need subscription key and the endpoint where service is exposed.
	Use sdk and sample snippets to verify connection. Package `azure.cognitiveservices.speech` contains helper wrapper classes for communication with API.

	Keep in mind that FileInput option is fragile for now and does not work
	`audio_input = speechsdk.AudioConfig(filename = audio_filname)` so it's more convenient to verify service with real-time microphone input.
	In case of recognition/sythesizing use SpeechRecognizer and SpeechSynthesizer. For transaltion there is specified `translation` sub-package containing tranlsation classes.
	
4. Pricing (Region: West Europe)

Q&A
speech-to-text
	F0 - free (5h of audio per month) (1 simultanous req)
	S0 - Standard (€0,844 per hour audio) (20 simultanous req)

text-to-speech
	F0 - free (5/0.5 mln chars per month) (1 simultanous req)
	S0 - Standard (€3,374 per 1 mln characters)

Speech translation:
	F0 - 5h of audio
	S0 - €2,11 per audio hour
