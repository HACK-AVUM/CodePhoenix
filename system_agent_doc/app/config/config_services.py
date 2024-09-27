from dotenv import load_dotenv
import os

# Carica il file .env
load_dotenv()


############################################################# CONFIG-SETTING ###############################################################


################## PORT  #####################
"""
get_port() - get port microservice  
@:return PORT
"""
def get_port():
    return os.getenv('PORT')

#############################################


################## DEBUG MODE  #####################
"""
get_debug_mode() - get debug mode microservice  
@:return DEBUG
"""
def get_debug_mode():
    return os.getenv('DEBUG')

#############################################



############################################################# URL ###############################################################



################## URL_OLLAMA  #####################
"""
get_ollama_url() - get Ollama Local Url  
@:return OLLAMA_URL
"""
def get_ollama_url():
    return os.getenv('OLLAMA_URL')

#############################################



################## URL_CHATGPT_4  #####################
"""
get_ollama_url() - get Ollama Local Url  
@:return OLLAMA_URL
"""
def get_chatgpt4_url():
    return os.getenv('OPEN_AI_CHAT4_URL')
#############################################


################## URL_CHATGPT_3_5  #####################
"""
get_chatgpt3_5_url() - get ChatGPT Url  
@:return OPEN_AI_CHAT3_5_URL
"""
def get_chatgpt3_5_url():
    return os.getenv('OPEN_AI_CHAT3_5_URL')

#############################################


############################################################# MODEL ###############################################################


################## MODEL LLAMA2  #####################
"""
get_ollama_llama2_model() - get LLAMA2 model 
@:return MODEL_LLAMA2
"""
def get_ollama_llama2_model():
    return os.getenv('MODEL_LLAMA2')
#############################################


################## MODEL CHATGPT4  #####################
"""
get_chatgpt4_model() - get CHATGPT4 model 
@:return MODEL_CHATGPT4
"""
def get_chatgpt4_model():
    return os.getenv('MODEL_CHATGPT4')
#############################################


################## MODEL CHATGPT3_5  #####################
"""
get_chatgpt3_5_model() - get CHATGPT3.5 model 
@:return MODEL_CHATGPT4
"""
def get_chatgpt3_5_model():
    return os.getenv('MODEL_CHATGPT3_5')
#############################################


############################################################# API KEY ###############################################################


################## API KEY CHATGPT3_5  #####################
"""
get_chatgpt3_5_api_key() - get CHATGPT3.5 api key 
@:return CHATGPT3_5_API_KEY
"""
def get_chatgpt3_5_api_key():
    return os.getenv('CHATGPT3_5_API_KEY')
#############################################


################## API KEY CHATGPT4  #####################
"""
get_chatgpt4_api_key() - get CHATGPT4 api key 
@:return CHATGPT4_API_KEY
"""
def get_chatgpt4_api_key():
    return os.getenv('CHATGPT4_API_KEY')
#############################################

