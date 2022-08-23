from vectice import Experiment
from vectice.api.json import StageStatus
import os

if __name__ == '__main__':
    experiment = Experiment(
        api_endpoint="app.vectice.com", # The URL of your vectice installation, for SAAS, use https://app.vectice.com
        user_token="", # your user Token. Can be found here: https://app.vectice.com/account/api-keys
        workspace="",  # Workspace name the project belongs to
        project="",  # Project name the lineage should be put
        job="Integrations",  # name of the current job
    )

    ## To create a GCS dataset, you need to set up the credentials to have access to your data in GCS.
    ## You can use the json file provided in the tutorial page: https://app.vectice.com/tutorial
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "readerKey.json"
    dataset = experiment.vectice.create_gcs_dataset(
                        uri=["gs://vectice_tutorial/kc_house_data_cleaned.csv"],##uri = ["bucket_name/folder"]  # Folder level example / 'bucket_name/folder/file.csv' (would be file level)
                        name = "GCS_dataset", # Dataset name
                        description= " GCS dataset"
                        )
   
# To create an s3 dataset, you need to set up the credentials to have access to your data in S3 and you might have to install boto3 (!pip install boto3)
# https://doc.vectice.com/integration/aws.html
#os.environ["AWS_ACCESS_KEY_ID"] = "AWS_ACCESS_KEY_ID"
#os.environ["AWS_SECRET_ACCESS_KEY"] = "AWS_SECRET_ACCESS_KEY"

    #experiment.vectice.create_s3_dataset(
    #            uri=["s3://folder/file"], #S3 uri
    #            name = "S3 dataset", #Dataset name
    #            description = "S3 dataset"
    #)

    model = experiment.add_model_version(
                                model="Regressor", # Model name
                                algorithm = "Decision Tree",
                                metrics = {"RMSE" : 144000, "MAE": 96000},
                                hyper_parameters = {"Tree Depth": 6},
                                #attachment = [], # List of attachments to add to your model version 
                                )

# If you are using your local environment with GIT installed or JupyterLab etc... the code
# tracking is automated and you don't have to create a code version manually.
    input_code = experiment.add_code_version_uri(git_uri="https://github.com/vectice/vectice-examples",
                                             entrypoint="Quick_references/Quickstart.py") 

    experiment.start(inputs = [input_code, dataset, model], run_notes="Run to generate Random Forest")

    experiment.add_model_version(
                                model="Regressor",
                                algorithm = "Random Forest",
                                metrics = {"RMSE" : 116000,"MAE": 73174},
                                hyper_parameters = {"min samples": 30,"nb_trees" : 60},
                                #attachment = [], # List of attachments to add to your model version 
                                )

    experiment.document_run(name="Integrations")
    
   ## All the artifacts that have been created after starting the experiment, and before completing it, will be automatically attached to the run as inputs
    experiment.complete()

## Update the stage status
    experiment.vectice.update_stage(stage="Integrations", status=StageStatus.Completed)