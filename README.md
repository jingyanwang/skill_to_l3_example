# Vectice-Examples
A set of examples for using Vectice.com software. The notebooks are seperated into two categories, being either Vanilla or MLflow. Vanilla notebooks use the Vectice App and SDK without any third party integrations. Whereas, Mlflow uses the MLflow integration offered by Vectice. In the future more integration examples will be added.

The Vectice SDK documentation can be found [here](https://storage.googleapis.com/sdk-documentation/sdk/index.html)

# Getting Started

```
pip install vectice
```
The following code is just an example to test that the Vectice SDK is working as it should be. You can use an IDE or a notebook to execute this code. It's intializing a vectice object that connects to vectice. If everything is working as it should be you'll recieve no errors. 
```python3
from vectice import Vectice
vectice = Vectice(project_token="PROJECT_TOKEN")
```
The Vectice SDK leverages runs as the terminology used when capturing metadata from the work you do. Thus, if you want to clean data for example and capture what you've done, you would create the inputs of the data that will be cleaned, create a run and then start it. Then you'd perform the data cleaning. 

```python3
ds_version = [vectice.create_dataset_version().with_parent_name("DATASET_NAME_IN_VECTICE_APP")]
run = vectice.create_run("RUN_NAME")
vectice.start_run(run, inputs = ds_version)
```
Once you've performed the data cleaning or any other actions you end the run by simple creating outputs and then calling the end_run method.
```python3
outputs = [vectice.create_dataset_version().with_parent_name("DATASET_NAME_IN_VECTICE_APP")]
vectice.end_run(outputs)
```
