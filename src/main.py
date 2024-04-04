"""
main file for model orchestration + execution
"""

from src.config import AppConfig
from src.model.langchain import DataLoader
from src.model.bedrock import BedrockModel


data_loader = DataLoader()
docs = data_loader.load()

bedrock_runtime = BedrockModel()


def main(prompt):
    mod_prompt = f"""
        \n\nHuman: {prompt}
        {docs}
        
        Assistant:
    """
    print(repr(AppConfig()))
    print(f"Execute prompt")
    resp = bedrock_runtime.invoke_model(mod_prompt)

    return f"Result: {resp}"


