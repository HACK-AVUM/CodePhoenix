from crewai import LLM

import os

from app.config.config_services import get_ollama_llama2_model, get_chatgpt3_5_model, get_chatgpt4_model
from app.config.config_services import get_ollama_url,get_chatgpt3_5_url,get_chatgpt4_url
from app.config.config_services import get_chatgpt3_5_api_key,get_chatgpt4_api_key


#################################################### MODEL SERVICE CONFIG ######################################################

################## GET LLM MODEL  #####################

"""
get_LLM() - create LLM model with 

@:parameter model_used - model used for this work

@:return - LLM model with url and model name 
"""
def get_LLM(model_used):
    if(model_used == os.getenv('MODEL_CHATGPT4')):
        return get_chatgpt4_llm()
    elif(model_used == os.getenv('MODEL_CHATGPT3_5')):
        return get_chatgpt3_5_llm()
    else:
        return get_Llama2_llm()

####################################################


################## GET LLM LLAMA2  #####################
"""
get_Llama2_llm() - create LLM model with 

@:parameter model - model name LLAMA2
@:parameter url_ollama - url of localhost ollama API
 
@:return - LLM model with url and model name 
"""
def get_Llama2_llm():

    # TODO : Temperature modality 

    model = get_ollama_llama2_model()
    url_ollama = get_ollama_url()

    return LLM(
        model= model,
        base_url= url_ollama
    )
####################################################


################## GET LLM CHATGPT4  #####################
"""
get_Llama2_llm() - create LLM model with 

@:parameter model - model name LLAMA2
@:parameter url_ollama - url of localhost ollama API

@:return - LLM model with url and model name 
"""

def get_chatgpt4_llm():
    model = get_chatgpt4_model()
    url_chatgpt4 = get_chatgpt4_url()
    api_key = get_chatgpt4_api_key()

    return LLM(
        model=model,
        base_url=url_chatgpt4,
        api_key = api_key
    )
####################################################


################## GET LLM CHATGPT3.5  #####################
"""
get_Llama2_llm() - create LLM model with 

@:parameter model - model name LLAMA2
@:parameter url_ollama - url of localhost ollama API

@:return - LLM model with url and model name 
"""
def get_chatgpt3_5_llm():
    # Model Chatgpt
    model = get_chatgpt3_5_model()
    # URL ChatGPT
    url_chatgpt3_5 = get_chatgpt3_5_url()
    # API KEY
    api_key = get_chatgpt3_5_api_key()

    return LLM(
        model=model,
        base_url=url_chatgpt3_5,
        api_key = api_key
    )

####################################################