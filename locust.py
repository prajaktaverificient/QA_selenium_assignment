from locust import HttpUser, TaskSet

class MyTasks(TaskSet):
    #when locust file start executing on_start() will be called first
    def on_start(self):
        self.MyWebsiteUser.get("/")

class MyWebsiteUser(HttpUser):
    min_wait = 100  # miliseconds
    max_wait = 5000  # miliseconds
    host ="https://www.bestundertaking.net/NewConnection.aspx"
    # same as wait_time = between(0.100, 5)


