"""
Model creation
"""

import json
import os
from pprint import pprint

from src.model.utils.bedrock_client import get_bedrock_client
from src.config import AppConfig



class BedrockModel:
    def __init__(self) -> None:
        self.config = AppConfig()
        self.client = get_bedrock_client(
            region=os.environ.get("AWS_REGION", None),
            runtime=True
        )


    def _validate(self):
        avail_models = self.client.list_foundation_models()
        for model in avail_models['modelSummaries']:
            pprint(model['modelId'])


    def invoke_model(self, prompt):
        body = json.dumps(
            {
                "prompt": prompt,
                "max_tokens_to_sample":4096,
                "temperature":0.5,
                "top_k":250,
                "top_p":0.5,
                "stop_sequences": ["\n\nHuman:"]
            }
        )
        response = self.client.invoke_model(
            body=body, 
            modelId=self.config.bedrock_modelId, 
            accept=self.config.bedrock_accept, 
            contentType=self.config.bedrock_contentType
        )
        response_body = json.loads(response.get('body').read())
        return response_body.get('completion')
        # print(response_body.get('completion'))

