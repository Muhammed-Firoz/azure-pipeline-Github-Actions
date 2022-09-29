# Overview

This project is to deploy a flask based ML webapp in the azure webapp serviceand to conduct load test on it using locust. The webapp deployment is automated using azure pipeline.

## Project Plan
Project Plan

*Link to Trello board https://trello.com/b/6E5p4ZVN/project6


*Link to spreadsheet project plan  https://docs.google.com/spreadsheets/d/1-eWv2khCIhTI6tuPomEeAxwZsJ4DZlzss0qTuMlwClc/edit?usp=sharing

## Instructions


* Architectural Diagram (Shows how key parts of the system work)>
![architecture](https://user-images.githubusercontent.com/108992155/192412566-32f24aa5-55db-4a25-9b5e-18af5d30a1ba.PNG)
<p>
1.Clone the Project files to VisualStudio/ Azure cloud CLI.<br>
2.Create virtual environment.<br>
3.Go to directory where files are kept.<br>
4.Run make all.<br>
5.Deploy the webapp using the c<br>ommand 'az webapp up' and name, runtime=python:3.7.<br>
6.Check weather deployment occured without error by checking the GUI using URL and running './make_predict_azure.sh' command in CLI.<br>
7.Run the load test using locust.<br>
8.Create a service connection in azure devops organisation.<br>
9.Create an agent pool and an add agent (if you are using a shared azure service).<br>
10.Create a pipeline in the project.<br>
11.Select github repository.<br>
12.Select existing YAML file.<br>
13.Make changes which are necessary in YAML (like agent pool name, service connection ...).<br>
14.Add any additional steps you want to add in the build or deployment stage.<br>
15.Save the pipeline.<br>
16.Run the Pipeline.<br>
</p>

* Project running on Azure App Service<br>
### Azure app service
![azureappderivice](https://user-images.githubusercontent.com/108992155/192424810-46b671e8-1aaa-4483-b6d1-9303c8619a2b.png)


#### Project cloned into Azure Cloud Shell
![ss of github clonning](https://user-images.githubusercontent.com/108992155/192417481-8b161de4-43d4-4dae-860f-dbd5b584f74b.PNG)



### Passing tests that are displayed after running the `make all` command from the `Makefile`

![ss of make file passing](https://user-images.githubusercontent.com/108992155/192417515-5f12c1ab-2ff1-4f53-a035-f483f342cff8.PNG)

### Output of a test run<br>
![ssapp](https://user-images.githubusercontent.com/108992155/192422756-35e3833c-e529-4687-a1b9-f216279b8952.JPG)

### Deploying webapp using azure pipeline into azure app service
![deploy webapp pieline](https://user-images.githubusercontent.com/108992155/192425573-b945d6b0-52bc-40e3-9f30-923b47f6f8f2.png)


### successful run in pipeline
![succ run pipeline](https://user-images.githubusercontent.com/108992155/192424878-dac7c6dc-3af8-4d9d-9e0f-ffd4822d2789.png)


### Successful prediction from deployed flask app in Azure Cloud Shell.<br>  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```
<br>

### Successful prediction by webapp<br>
![successful pred](https://user-images.githubusercontent.com/108992155/192425023-9b03d303-7627-487a-b635-48a4bfd3460f.png)

<br>
<br>

### Output of streamed log files from deployed application<br>
![log streem](https://user-images.githubusercontent.com/108992155/192425093-1ec54c9b-f589-494e-949f-3c10601e676f.png)

<br>
<br>

### Conducting load test on the deployed app<br>
![locust run ss](https://user-images.githubusercontent.com/108992155/192152707-0b8d8392-9385-4efb-bb6a-573fe45c2504.JPG)
![locust run ss2](https://user-images.githubusercontent.com/108992155/192152713-6ecc16b3-ced0-4a39-a31d-bdf110b159ac.JPG)
<br>
<br>
## Enhancements

This project can be improved by adding testplans, creating the webapp  more interactive and settingup custom alert.

## Demo 
<br>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=zOwd_eGFmEI
" target="_blank"><img src="http://img.youtube.com/vi/zOwd_eGFmEI/0.jpg" 
alt="Demo" width="240" height="180" border="10" /></a>




##Acknowledgements <br>

The images used in the Architectural diagram and in the video thumbnail are obtained from Google images.


[![Python application test with Github Actions](https://github.com/Muhammed-Firoz/azure-pipeline-Github-Actions/actions/workflows/main.yml/badge.svg)](https://github.com/Muhammed-Firoz/azure-pipeline-Github-Actions/actions/workflows/main.yml)
