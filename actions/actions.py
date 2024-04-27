from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

points = [0, 0, 0, 0]

class ActionVehicleBody(Action):
    def name(self) -> Text:
        return "action_vehicle_body"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("""
        Have you thought about the electric vehicle lineup and what 
        body type might best fit your lifestyle? Are you envisioning
        yourself in a sleek sedan, a versatile SUV, or perhaps a stylish 
        compact model?
        """)
        return []
class ActionVehicleBodySuv(Action):
    def name(self) -> Text:
        return "action_vehicle_body_suv"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[0] += 2
        points[3] += 1
        return []
    
class ActionVehicleBodySaloon(Action):
    def name(self) -> Text:
        return "action_vehicle_body_saloon"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[1] += 1
        points[2] += 1
        return []
    
class ActionFeaturesTech(Action):
    def name(self) -> Text:
        return "action_features_tech"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[1] += 1
        points[2] += 2
        return []

    
class ActionFeatures(Action):
    def name(self) -> Text:
        return "action_features"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("""
        What features are you looking forward to the most? Do you prioritize
        more advanced technology, premium materials or do you see your car more
        as just a transportation method?
        """)

class ActionFeaturesTransport(Action):
    def name(self) -> Text:
        return "action_features_transport"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[3] += 3
        return []
    
class ActionFeaturesLuxus(Action):
    def name(self) -> Text:
        return "action_features_luxus"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[0] += 2
        points[1] += 2
        return []

class ActionRange(Action):
    def name(self) -> Text:
        return "action_range"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("""Do you give a lot of importance to the vehicles range?
        (A vehicles range is how long you can drive it without filling the tank)""")
        return []
    
class ActionRangeVery(Action):
    def name(self) -> Text:
        return "action_range_very"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[0] += 2
        points[3] += 2
        return []
    
class ActionRangeLittle(Action):
    def name(self) -> Text:
        return "action_range_little"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[1] +=1
        points[2] +=1
        return []
    
class ActionBudget(Action):
    def name(self) -> Text:
        return "action_budget"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("""Budget is important, and electric vehicles offer exceptional 
        value. What's your comfortable range for investing in a high-quality electric car that
        provides long-term savings and luxury?""")
        return []
    

class ActionBudgetHigh(Action):
    def name(self) -> Text:
        return "action_budget_high"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[0] += 2
        points[1] += 2
        points[2] += 1
        return []
    
class ActionBudgetMedium(Action):
    def name(self) -> Text:
        return "action_budget_medium"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[2] += 1
        points[3] += 1
        return []


class ActionBudgetLow(Action):
    def name(self) -> Text:
        return "action_features_low"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[3] += 4
        return []

    
class ActionValue(Action):
    def name(self) -> Text:
        return "action_value"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("""What do you value the most from your car? 
        Tell us what is important to you and what you would like to see in your
        future car""")
        return []
    
class TailorResponse(Action):
    def name(self) -> Text:
        return "tailor_response"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("""This is the car for you""")
        return []



    
    

    
