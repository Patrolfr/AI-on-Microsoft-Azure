
## Conversational bot

Unfortunately I have created only hello-world alike project because I was struggling with technical issues. 
To sum up, information about requirements in Bot Composer instruction is quite misleading.  
There is a info about SDK 3.1 *or later* but.. having installed Dotnet SDK 5.0 and trying to run bot - Bot Composer failes with mysterious message. Diving deeper I ran project from terminal with specific dotnet sdk and there were info about not compatible libraries.

Requirements instruction:  
  
![alt text](https://github.com/Patrolfr/AI-on-Microsoft-Azure/blob/main/pictures/instruction_requirements.png?raw=true)  

Dotnet error: 

![alt text](https://github.com/Patrolfr/AI-on-Microsoft-Azure/blob/main/pictures/dotnet_error.png?raw=true)  

Youtube presentation:  
https://youtu.be/ZQv1yi307z8  

Sources to restore bot:
```
{
  "$kind": "Microsoft.AdaptiveDialog",
  "$designer": {
    "$designer": {
      "name": "talky-ai-bot",
      "description": "",
      "id": "ZWgDxq"
    }
  },
  "autoEndDialog": false,
  "defaultResultProperty": "dialog.result",
  "triggers": [
    {
      "$kind": "Microsoft.OnConversationUpdateActivity",
      "$designer": {
        "id": "Gqkdss"
      },
      "actions": [
        {
          "$kind": "Microsoft.Foreach",
          "$designer": {
            "name": "Loop: for each item",
            "description": "",
            "id": "VI52rl"
          },
          "itemsProperty": "turn.Activity.membersAdded",
          "actions": [
            {
              "$kind": "Microsoft.IfCondition",
              "$designer": {
                "name": "Branch: if/else",
                "description": "",
                "id": "Z8YIdh"
              },
              "condition": "string(dialog.foreach.value.id) != string(turn.Activity.Recipient.id)",
              "actions": [
                {
                  "$kind": "Microsoft.SendActivity",
                  "$designer": {
                    "name": "Send a response",
                    "description": "",
                    "id": "iVRBfn"
                  },
                  "activity": "${SendActivity_iVRBfn()}"
                }
              ]
            }
          ],
          "value": "dialog.foreach.value"
        }
      ]
    },
    {
      "$kind": "Microsoft.OnUnknownIntent",
      "$designer": {
        "id": "Dlvz6S"
      },
      "actions": [
        {
          "$kind": "Microsoft.QnAMakerDialog",
          "$designer": {
            "id": "Pc31Nf"
          },
          "knowledgeBaseId": "=settings.qna.knowledgebaseid",
          "endpointKey": "=settings.qna.endpointkey",
          "hostname": "=settings.qna.hostname",
          "noAnswer": "Sorry, I did not find an answer.",
          "threshold": 0.3,
          "activeLearningCardTitle": "Did you mean:",
          "cardNoMatchText": "None of the above.",
          "cardNoMatchResponse": "Thanks for the feedback.",
          "top": 3,
          "isTest": false
        }
      ]
    }
  ],
  "$schema": "https://raw.githubusercontent.com/microsoft/BotFramework-Composer/stable/Composer/packages/server/schemas/sdk.schema",
  "generator": "talky-ai-bot.lg",
  "recognizer": "talky-ai-bot.lu.qna",
  "id": "talky-ai-bot"
}
```