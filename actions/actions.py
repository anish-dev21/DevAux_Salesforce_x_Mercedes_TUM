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
        dispatcher.utter_message("""Hello, I am Mercedes Text Assistant. I will help you
find your perfect car. Lets get started, would you prefer more of a compact SUV or a sedan""")
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
        dispatcher.utter_message("""Are you more into Tech, looking for something more Luxurious or 
you see your car more as a means of transport""")

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
        dispatcher.utter_message("""Is vehicle range important for you?
*vehicle range is how much fuel your car uses""")
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
        dispatcher.utter_message("""Is your budget low, medium or high?""")
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


class ActionBudgetLittle(Action):
    def name(self) -> Text:
        return "action_budget_little"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        points[3] += 4
        return []

    
class TailorResponse(Action):
    def name(self) -> Text:
        return "tailor_response"

    @staticmethod
    def find_index_of_highest(arr):
        if not arr:
            return None  # Return None if the array is empty

        max_value = max(arr)  # Find the maximum value in the array
        max_index = arr.index(max_value)  # Find the index of the maximum value
        return max_index

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        persona = self.find_index_of_highest(points)    
        if persona == 0:
            dispatcher.utter_message("You should have a look at the models: Mercedes-Maybach EQS SUV and Mercedes G-Class"
)
        if persona == 1:
            dispatcher.utter_message("You should have a look at the Mercedes EQS SUV and the Mercedes-EQE SUV")
        if persona == 2:
            dispatcher.utter_message("You should have a look at the EQE Saloon and the Mercedes EQS Saloon")
        if persona == 3:
            dispatcher.utter_message("You should have a look at the Mercedes EQA and EQB")
        return[]

class Alternative(Action):
    def name(self) -> Text:
        return "alternative"

    @staticmethod
    def find_second_largest(arr):
        if len(arr) < 2:
            return None  # Return None if the array has less than 2 elements

        # Find the maximum element
        max_value = max(arr)

        # Find the index of the maximum element and remove it
        arr.remove(max_value)

        # Find the second largest element
        second_largest = max(arr)

        return second_largest



    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        persona = self.find_second_largest(points)    
        if persona == 0:
            dispatcher.utter_message("Yes of course, here are some other options: Mercedes-Maybach EQS SUV and Mercedes G-Class"
)
        if persona == 1:
            dispatcher.utter_message("Yes of course, here are some other options: Mercedes EQS SUV and the Mercedes EQE SUV")
        if persona == 2:
            dispatcher.utter_message("Yes of course, here are some other options: EQE Saloon and the Mercedes EQS Saloon")
        if persona == 3:
            dispatcher.utter_message("Yes of course, here are some other options: Mercedes EQA and EQB")
        return []
    

class Combustion(Action):
    def name(self) -> Text:
        return "combustion"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(""""Electric cars offer a cleaner,
more sustainable alternative to traditional combustion vehicles, 
with lower operating costs and superior performance. For more infos
visit the Mercedes website.""")
        return[]

