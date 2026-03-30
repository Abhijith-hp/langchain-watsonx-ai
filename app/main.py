from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes

model_id= "meta-llama/llama-3-3-70b-instruct"

parameters = {
    GenParams.MAX_NEW_TOKENS : 256,
    GenParams.TEMPERATURE : 0.7,
}

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
  
}

project_id = "skills-network"

model = ModelInference(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)