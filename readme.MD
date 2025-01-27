## Prediction of house price for Bengaluru city, India using machine learning model

Creating an application that can predict the house price in the bangalore.

### Outline

1. Creating a machine learning model from the [dataset]() available on kaggle. [[Outline for modelling](model)]
2. Writing an server-side application which will be able to predict the house prices based on the given input from the user.
3. Developing an friendly user-interface through which client can communicate.

The final application looks like this -

![presentation](https://user-images.githubusercontent.com/38955297/192730317-06987a3b-3b0a-4710-845d-24ded7ab5228.gif)

## FastAPI

<img src='https://upload.wikimedia.org/wikipedia/commons/1/1a/FastAPI_logo.svg' height=100/>

### FastAPI Overview

**What is FastAPI?**
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

**Why FastAPI?**
FastAPI is known for its speed, ease of use, and automatic interactive API documentation. It supports [asynchronous programming](app\readme.md), making it suitable for high-performance applications.

**How to Deploy?**

1. Install FastAPI and Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```

### Serving the application as FastAPI

Run this command:

```
fastapi run app/main.py --port=7751
```

or

```
uvicorn app.main:app --port 7751 --reload
```

### References

1. [Running FastAPI with Docker Image](https://fastapi.tiangolo.com/deployment/docker/#create-the-fastapi-code)
2. [Running a Server Manually](https://fastapi.tiangolo.com/deployment/manually/#install-the-server-program)

## Unit Testing with Pytest

In this project, I learned about unit testing using `pytest`. I wrote several test cases, including:

- Testing for file existence
- Loading the model
- Testing the root page endpoint
- Testing the API endpoint that predicts the price of a house in Bangalore from given inputs

Using `pytest`, we can define functions for each test and verify whether they are running correctly. To run the tests, use the following command in the terminal:

```bash
pytest test/
```

This command will execute all the `test_*.py` files in the `test` folder and provide a detailed report on how many tests passed while running and testing the application. This is essential to ensure that our application runs correctly when deployed on a remote server or cloud environment.

### Why automated testing and integration test?

Automated testing is crucial because it helps us verify that all tests are running and our application functions as designed. This automated testing pipeline can also be integrated into CI (Continuous Integration) pipelines, which is explained in the next section. In the CI pipeline, we will build, test, and deploy our application on every git push command made to a specific branch. This automation streamlines the deployment and testing process, eliminating the need for manual intervention

## Continuous Integration and Continous Deployment

Here is a step by step video how you can deploy your applicaiton to Docker hub using automated CI/CD pipelines:

<a href="https://www.youtube.com/watch?v=R8_veQiYBjI"><img src="https://img.youtube.com/vi/R8_veQiYBjI/0.jpg" height=400/></a>

### Build and Push Docker Images

To create a workflow for CI/CD pipeline for deploying ML models on Docker Hub:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v3
      - name: Build
        run: |
          pip install -r requirements.txt

  test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v3
      - name: Run tests
        run: pytest test/

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Check out code
        uses: actions/checkout@v3

      - name: Deploy
        uses: mr-smithers-excellent/docker-build-push@v6
        with:
        image: docker-hub-repo/image-name
        registry: docker.io
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
```

To build and push docker images: [link](https://github.com/mr-smithers-excellent/docker-build-push)

Follow this example for pushing the docker to docker hub: [link](https://github.com/mr-smithers-excellent/docker-build-push?tab=readme-ov-file#examples)
