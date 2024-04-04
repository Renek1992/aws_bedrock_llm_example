import os


class AppConfig:
    def __init__(self):
        self.file_bucket = os.environ.get("BUCKET_NAME")
        self.file_prefix = os.environ.get("FILE_PREFIX")
        self.bedrock_modelId = os.environ.get("MODEL_ID")
        self.bedrock_accept = os.environ.get("ACCEPT")
        self.bedrock_contentType = os.environ.get("CONTENTTYPE")

    def __repr__(self) -> str:
        return f"""AppConfig(
            file_bucket = {self.file_bucket}, 
            file_prefix = {self.file_prefix}, 
            bedrock_modelId = {self.bedrock_modelId}, 
            bedrock_accept = {self.bedrock_accept}, 
            bedrock_contentType = {self.bedrock_contentType}, 
        )"""