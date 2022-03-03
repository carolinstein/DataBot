# DataBot

DataBot has been developed as part of my master thesis at the TU Berlin to involve citizens in the scientific analysis of data. 
It is based on the Rasa open source framework.

## Preparation before execution
1. Insert AirtableAPI in actions.yml file 
2. Insert Telegram credentials in credentials.yml file

### Communicate with bot directly
3. When running for the first time, run ```rasa train``` 
4. Run ```rasa run actions```  to start Rasa Action Server 
5. Run either ```rasa shell``` or ```rasa x```  to communicate with the bot via the terminal or via the RasaX Web Interface
   

### Communicate with bot via Telegram
6. When running for the first time, run ```rasa train``` 
7. Run ```rasa run actions```  to start Rasa Action Server 
8. Run ```ngrok http 5005```  to open Ngrok tunnel 
9. Insert https link provided by Ngrok into the credentials file as https://<```link```>.ngrok.io/webhooks/telegram/webhook 
10. Run either ```rasa run```  or ```rasa x```  
11. Find the chatbot on Telegram under DataBot or  @DataLiteracyBot and chat
