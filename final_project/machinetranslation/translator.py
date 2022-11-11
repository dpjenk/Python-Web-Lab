"""Importing Files"""
import os
from ibm_watson import LanguageTranslatorV3 #pylint: disable=E0401
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator #pylint: disable=E0401
from dotenv import load_dotenv #pylint: disable=E0401

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('0zQmgIBmnLvmxxOG_OnzIICz3xX39-vTdYCTfA2juyDD')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url=("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4cca3342-aaa9-44d3-9cbf-fbc0fbac4e64")

def english_to_french(english_text):
    """Function translating Engish to French"""
    french_translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = french_translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """Function translating French to English"""
    english_translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = english_translation["translations"][0]["translation"]
    return english_text