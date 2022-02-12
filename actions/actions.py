# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import time

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from dotenv import load_dotenv
from rasa_sdk.events import SlotSet

load_dotenv()

API_key ='keyLFA5lIHL937joL'
table_name='Table%201'
Base_ID = 'appa1Hc5WRSKLcrzu'


def question_sheet(Qu, Em):

    try: 
        request_url=f"https://api.airtable.com/v0/{Base_ID}/{table_name}"
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {API_key}"
        }
        data={
            "fields": {
                "Question": f"{Qu}",
                "E-Mail Address": f"{Em}"
            }
        }
   
        response= requests.post(
            request_url, headers= headers, data=json.dumps(data)
        )
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
       # raise SystemExit(err)
        print('Invalid request')
    print(response.status_code)
    return(response)

class SubmitQuestions(Action):

    def name(self):
        return "action_submit_questions"
    
    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        em = tracker.get_slot("email")
        qu= tracker.get_slot("question")
        response = question_sheet(qu, em)

        dispatcher.utter_message("Your questions have been submitted.")
        return []

class ActionSleepAction(Action):
    def name(self):
        return "sleep_function"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print ("Start : %s" % time.ctime())
        time.sleep( 5 )
        print ("End : %s" % time.ctime())
        return []

class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("email", None), SlotSet("question", None)]

