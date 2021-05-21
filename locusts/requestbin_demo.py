#!/usr/bin/env python
# -*- coding: utf-8 -*-
from locust import HttpUser, between, task


# http://httpbin.org/
# base url: http://httpbin.org

class RequestBinDemo(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_url(self):
        self.client.get("/get")

    def on_start(self):
        self.client.post("/post", json={"username": "foo", "password": "bar"})

# locust -f <locust_file_name>
# Concurrency, parallelism, threading, multiprocessing. That’s a lot to grasp already. Where does async IO fit in?