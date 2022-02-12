# ChatbotSS21

## Setup of chatbot in Docker image
1. Go to the app folder and execute ```sudo docker build -t app .```
2. Go to the upper folder and run ```docker-compose up```

### Communicate with bot directly
3. When everything is up and running you can communicate with the bot via 
    ```curl -XPOST http://localhost:5005/webhooks/rest/webhook \
            -H "Content-type: application/json" \
            -d '{"sender": "test", "message": "hello"}'``` (!use a linux terminal)

### Communicate with bot via Telegram
3. Look at ID of container image rasa
4. Run ```docker run --rm -it --net Netzwerk_des_Docker_compose --Rasa_container_ID shkoliar/ngrok ngrok http Rasa_container_ID:5005```
5. Stop container image rasa and Add the https link provided by ngrok into the credentials file under      telegram webhook_url: "https://<link>.ngrok.io/webhooks/telegram/webhook"
6. Start container image rasa
7. Chat with GreenBuddy_bot on Telegram


## Local setup
1. clone git repository
3. run ```rasa train```
4. in a different terminal run ```run rasa actions```
5. when model is trained, run ```rasa shell``` for shell view

### for Telegram integration
4. download ngrok and start ngrok terminal; run ```ngrok http 5005```
5. Add the https link provided by ngrok into the credentials file under telegram webhook_url: "https://<link>.ngrok.io/webhooks/telegram/webhook"
6. run ```rasa run```
7. go to Telegram and chat with GreenBuddy_bot

## Airtable access
To check the export function enter your own Airtable credentials when asked.
Otherwise use the given credentials, the access to that table is given through this link: https://airtable.com/invite/l?inviteId=inv6ypvqlvFIi6v4o&inviteToken=b59433dea6fa8639fbdb0da97961123e67ae80eec589f962b86c159fc804e6cd&utm_source=email

## Changes to data base
When making changes in the data base, run ```python3 Dropbox.py``` before training the bot
Be aware: the local path to the pictures in the file have to be adopted
