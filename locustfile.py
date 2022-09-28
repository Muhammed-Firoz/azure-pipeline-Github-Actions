from locust import HttpUser, task, SequentialTaskSet, constant

class flaskAppTester(SequentialTaskSet):
    #Sequentially execute the task
    @task
    def get_users(self):
        res = self.client.get("/")
        print("Landing page status is ", res.status_code)
    
        
    @task
    def post_prediction(self):
        res=self.client.post("/predict")
        print("Predict end status is ",res.status_code)
        
        
class MyAppTester(HttpUser):
    wait_time = constant(1)
    host = "https://firozflaskmlapp.azurewebsites.net"
    
    
    tasks = [flaskAppTester]
