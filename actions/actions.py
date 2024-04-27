<<<<<<< Updated upstream
=======
# actions.py

>>>>>>> Stashed changes
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

<<<<<<< Updated upstream

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_default_fallback"
=======
class ActionAskAge(Action):
    def name(self) -> Text:
        return "action_ask_age"
>>>>>>> Stashed changes

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
<<<<<<< Updated upstream
        dispatcher.utter_message(
            text="Sorry, I can not answer this question. Find more information here: https://www.mercedes-benz.de/")
        return []
=======
        dispatcher.utter_message("How old are you?")
        
        return []

class ActionAskGender(Action):
    def name(self) -> Text:
        return "action_ask_gender"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("What is your gender?")
        return []


class ActionDetermineClientType(Action):
    def name(self) -> Text:
        return "action_determine_client_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        age = tracker.get_slot("age")
        print(age)
        # Determine client type based on age
        if int(age) < 30:
            client_type = "student"
        else:
            client_type = "working_professional"


        print(client_type)
        return [SlotSet("client_type", client_type)]

class ActionTailorResponse(Action):
    def name(self) -> Text:
        return "action_tailor_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        client_type = tracker.get_slot("client_type")
        gender = tracker.get_slot("gender")
        # Generate a response tailored to the determined client type
        print(gender)
        
        if client_type == "student":
            if gender =="male":
                dispatcher.utter_message("You're the user Pedro the student")
            else:
                dispatcher.utter_message("You're the user Lucía the student")

        if client_type == "working_professional":
            if gender =="male":
                dispatcher.utter_message("You're the user José the engineer")
            else:
                dispatcher.utter_message("You're the user Rosa the doctor")

        return []
>>>>>>> Stashed changes
