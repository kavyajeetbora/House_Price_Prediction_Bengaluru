### Summary of Synchronous vs. Asynchronous Server APIs

<img src="https://miro.medium.com/v2/format:webp/1*V5syja2casc0gCuu9zKV5g.png" height=400/>

#### Intuitive Example: Online Retail Orders

Let's imagine an online retail store like Amazon, and there's only one server processing orders.

**Synchronous (One at a Time)**
In a synchronous system, the server processes one order at a time. So, if there are three customers (Alice, Bob, and Charlie) placing orders:

1. The server processes Alice's order.
2. Once Alice's order is complete, the server processes Bob's order.
3. After Bob's order is complete, the server processes Charlie's order.

Each customer has to wait for the server to finish with the previous order before their order is processed. This is like a synchronous system where tasks are handled one after the other.

**Asynchronous (All at Once)**
In an asynchronous system, the server can start processing multiple orders at the same time. So, if there are three customers (Alice, Bob, and Charlie) placing orders:

1. The server starts processing Alice's order.
2. While Alice's order is being processed, the server starts processing Bob's order.
3. While both Alice's and Bob's orders are being processed, the server starts processing Charlie's order.

Now, all three customers are having their orders processed at the same time, and no one has to wait for the server to finish with the previous order. This is like an asynchronous system where tasks can be handled simultaneously.

In summary:

- **Synchronous**: One task at a time, like processing one order at a time in the online store.
- **Asynchronous**: Multiple tasks at the same time, like processing all orders at once in the online store.

#### Handling More Than Maximum Capacity

- **Queue the Request**: The server can make additional users wait until resources are freed up.
- **Reject the Request**: The server might reject requests if it cannot handle more than the maximum capacity.
- **Graceful Degradation**: Some servers might handle additional requests with reduced performance.

#### FastAPI Example

- **Prediction Endpoint**: We created a FastAPI function that takes in JSON data for making predictions using a trained model.
- **Calling the Endpoint**: We discussed how to call the FastAPI endpoint using `curl`, Postman, and a Python script.

### Difference Between `fastapi` and `fastapi[standard]`

The difference between `fastapi` and `fastapi[standard]` lies in the additional dependencies that come with the standard version. Here's a breakdown:

- **`fastapi`**: This is the core FastAPI package. It includes the essential components needed to create and run a FastAPI application. However, it does not include some optional dependencies that are useful for certain features.
- **`fastapi[standard]`**: This version includes the core FastAPI package along with additional dependencies that are commonly used in FastAPI applications. These dependencies enhance the functionality and ease of development. For example, it includes packages for data validation, serialization, and interactive API documentation.

When you install `fastapi[standard]`, it typically includes:

- `pydantic`: For data validation and settings management.
- `uvicorn`: An ASGI server for running FastAPI applications.
- `jinja2`: For template rendering.
- `python-multipart`: For handling file uploads.
- `email-validator`: For validating email addresses.

To install `fastapi[standard]`, you can use the following command:

```bash
pip install "fastapi[standard]"
```

This ensures you have all the necessary tools and libraries to fully leverage FastAPI's capabilities, including interactive documentation with Swagger UI and ReDoc.

### ASGI Server

An ASGI (Asynchronous Server Gateway Interface) server is a specification that allows for handling asynchronous web applications and frameworks in Python. It is designed to be the successor to WSGI (Web Server Gateway Interface), which is synchronous and used by frameworks like Flask and Django.

Here are some key points about ASGI servers:

- **Asynchronous Support**: ASGI supports asynchronous programming, which allows for handling multiple requests concurrently without blocking. This is particularly useful for applications that require high concurrency and real-time capabilities.
- **Protocol Agnostic**: ASGI is designed to be protocol agnostic, meaning it can handle different types of communication protocols, such as HTTP, WebSockets, and more. This makes it versatile for modern web applications that may need to handle various types of connections.
- **Scalability**: Due to its asynchronous nature, ASGI servers can handle a large number of simultaneous connections efficiently, making them suitable for high-traffic applications.
- **Compatibility with FastAPI**: FastAPI is built on top of ASGI, which allows it to leverage the benefits of asynchronous programming. This makes FastAPI highly performant and capable of handling real-time features like WebSockets.

Some popular ASGI servers include:

- **Uvicorn**: A lightning-fast ASGI server based on `uvloop` and `httptools`. It is commonly used with FastAPI.
- **Daphne**: An ASGI server developed as part of the Django Channels project. It is designed to handle both HTTP and WebSocket protocols.
- **Hypercorn**: An ASGI server that supports HTTP/1, HTTP/2, and WebSockets.

Here's an example of running a FastAPI application with Uvicorn:

```bash
pip install uvicorn
uvicorn main:app --reload
```
