import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('0zQmgIBmnLvmxxOG_OnzIICz3xX39-vTdYCTfA2juyDD')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4cca3342-aaa9-44d3-9cbf-fbc0fbac4e64")

def englishToFrench(englishText):
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return frenchText.get("translations")[0].get("translation")

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    return englishText.get("translations")[0].get("translation")
