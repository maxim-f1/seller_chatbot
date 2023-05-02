import os

import config
from utils import reconnect_decorator

import openai

from gpt_index import LLMPredictor, PromptHelper, SimpleDirectoryReader, ServiceContext, GPTSimpleVectorIndex
from langchain import OpenAI


class GPT3interface:
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in GPT3interface.__instance:
            GPT3interface.__instance[cls] = super().__new__(cls)
        return GPT3interface.__instance[cls]

    def __init__(self):
        if not config.OPENAI_API:
            exit('OPENAI_API no token provided')
        openai.api_key = config.OPENAI_API
        self.construct_index()

    @staticmethod
    def construct_index():
        if os.path.isfile(config.PROMPT_DATA_PATH):
            documents = SimpleDirectoryReader(config.PROMPT_DATA_PATH).load_data()
            service_context = ServiceContext.from_defaults(
                llm_predictor=LLMPredictor(llm=OpenAI(temperature=0.5, model_name='text-davinci-003', max_tokens=300)),
                prompt_helper=PromptHelper(max_input_size=4096,
                                           num_output=300,
                                           max_chunk_overlap=20,
                                           chunk_size_limit=600)
            )
            index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
            index.save_to_disk(config.PROMPT_INDEX_PATH)

    @staticmethod
    @reconnect_decorator.reconnect
    def response_from_gpt(query: str) -> str:
        index = GPTSimpleVectorIndex.load_from_disk(config.PROMPT_INDEX_PATH)
        return index.query(query, response_mode='compact').response
