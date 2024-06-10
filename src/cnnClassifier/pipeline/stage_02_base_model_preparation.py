from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.base_model_preparation import BaseModelPreparation
from cnnClassifier import logger


STAGE_NAME = "Prepare base model"


class BaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_preparation_config = config.get_base_model_preparation_config()
        base_model_preparation = BaseModelPreparation(config=base_model_preparation_config)
        base_model_preparation.get_base_model()
        base_model_preparation.update_base_model()


    
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = BaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e