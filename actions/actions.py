# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAskAddress(Action):
    def name(self) -> Text:
        return "action_ask_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Sure, could you please provide your delivery address?")
        return []

class ActionAskPizzaType(Action):
    def name(self) -> Text:
        return "action_ask_pizza_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("What type of pizza would you like to order?")
        return []

class ActionConfirmOrder(Action):
    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pizza_type = tracker.get_slot("pizza_type")
        address = tracker.get_slot("address")
        print(f"Extracted pizza type: {pizza_type}")  # Debug statement
        print(f"Extracted address: {address}")  # Debug statement
        dispatcher.utter_message(f"Sure, I've got your order for {pizza_type} pizza. It will be delivered to {address}.")
        return []
