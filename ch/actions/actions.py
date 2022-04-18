# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Action


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = {
            "intent": "greet",
            "endOfChat": True
        }
        # dispatcher.utter_message(format(msg))
        dispatcher.utter_custom_json(format(msg))
        return []


class ActionSuggestionPass(Action):
    def name(self) -> Text:
        return "action_suggest_review_pass"

    def run(self, dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = {
            "intent": "suggest_review_pass",
            "reviewResult": True,
            "endOfChat": True
        }
        # dispatcher.utter_message(format(msg))
        dispatcher.utter_custom_json(format(msg))
        return []


class ActionSuggestionFail(Action):
    def name(self) -> Text:
        return "action_suggest_review_fail"

    def run(self, dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = {
            "intent": "suggest_review_fail",
            "reviewResult": False,
            "endOfChat": True
        }
        # dispatcher.utter_message(format(msg))
        dispatcher.utter_custom_json(format(msg))
        return []


class ActionPersonalScoreQuery(Action):
    def name(self) -> Text:
        return "action_personal_score_query"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity = next(tracker.get_latest_entity_values(
            "score_query_target"), "None")
        msg = {
            "intent": "personal_score_query",
            "entity": entity,
            "endOfChat": True
        }
        # dispatcher.utter_message(format(msg))
        dispatcher.utter_custom_json(format(msg))
        return []


class ActionClassmapSearch(Action):
    def name(self) -> Text:
        return "action_classmap_search"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity = next(tracker.get_latest_entity_values(
            "search_target"), "None")
        msg = {
            "intent": "classmap_search",
            "entity": entity,
            "endOfChat": True
        }
        # dispatcher.utter_message(format(msg))
        dispatcher.utter_custom_json(format(msg))
        return []


class ActionClassmapPpt(Action):
    def name(self) -> Text:
        return "action_classmap_ppt"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity = next(tracker.get_latest_entity_values(
            "ppt_query_target"), "None")
        msg = {
            "intent": "classmap_ppt",
            "entity": entity,
            "endOfChat": True
        }
        # dispatcher.utter_message(format(msg))
        dispatcher.utter_custom_json(format(msg))
        return []
