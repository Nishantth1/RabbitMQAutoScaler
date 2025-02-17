# RabbitMQ AutoScaler Library Documentation

## Introduction

The RabbitMQ AutoScaler library provides an efficient way to automatically scale RabbitMQ consumers based on the message load in the queue. It dynamically adjusts the number of consumers to handle the incoming messages, ensuring optimal performance and resource utilization.

## Installation

To install the library, you need to have Python 3.7 or above installed. You can install the `rabbitmq_auto_scaler` library and its dependencies using pip:

```bash
pip install rabbitmq_auto_scaler
```

## Usage

### Importing the Library

First, you need to import the necessary classes from the library:

```python
import asyncio
from rabbitmq_auto_scaler import AutoScaler
```

### Creating an AutoScaler Instance

Create an instance of the `AutoScaler` class with the required parameters:

- `mq_url`: The RabbitMQ URL.
- `queue`: The name of the queue to consume messages from.
- `min_consumers`: The minimum number of consumers.
- `max_consumers`: The maximum number of consumers.
- `scale_up_threshold`: The message count threshold to scale up consumers.
- `scale_down_threshold`: The message count threshold to scale down consumers.
- `check_interval`: The interval (in seconds) to check the queue length and adjust consumers.
- `**kwargs`: The additional parameters to be passed.

```python
mq_url = 'amqps://your_username:your_password@your_rabbitmq_url:5671'
queue = 'your_queue_name'
min_consumers = 1
max_consumers = 10
scale_up_threshold = 10
scale_down_threshold = 1
check_interval = 5

auto_scaler = AutoScaler(mq_url, queue, min_consumers, max_consumers, scale_up_threshold, scale_down_threshold, check_interval)
```

### Setting a Message Handler

Define a message handler function to process the incoming messages:

```python
async def message_handler(message):
    print(f"Received message: {message.body.decode()}")
```

Set the message handler for the `AutoScaler` instance:

```python
await auto_scaler.set_message_handler(message_handler)
```

### Starting the AutoScaler

Start the AutoScaler to begin consuming messages and dynamically scaling the consumers:

```python
async def main():
    await auto_scaler.set_message_handler(message_handler)
    await auto_scaler.start()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
```

## Example Code

Here is a complete example code to demonstrate how to use the RabbitMQ AutoScaler library:

```python
import asyncio
from rabbitmq_auto_scaler import AutoScaler

mq_url = 'amqps://your_username:your_password@your_rabbitmq_url:5671'
queue = 'your_queue_name'
min_consumers = 1
max_consumers = 10
scale_up_threshold = 10
scale_down_threshold = 1
check_interval = 5

auto_scaler = AutoScaler(mq_url, queue, min_consumers, max_consumers, scale_up_threshold, scale_down_threshold, check_interval)

async def message_handler(message):
    print(f"Received message: {message.body.decode()}")

async def main():
    await auto_scaler.set_message_handler(message_handler)
    await auto_scaler.start()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
```

## Logging

The AutoScaler library provides detailed logging to help you monitor and debug its operations. Logs are written to a rotating file named `rabbitmq_autoscaler.log` and are also output to the console.

### Example Logging Configuration

Here is an example logging configuration you can use:

```python
import logging
from logging.handlers import RotatingFileHandler

log_handler = RotatingFileHandler('rabbitmq_autoscaler.log', maxBytes=5*1024*1024, backupCount=3)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        log_handler,
        logging.StreamHandler()  # Also output to console
    ]
)
logger = logging.getLogger('rabbitmq_autoscaler')
```

## Connection Pooling

The AutoScaler library uses connection pooling to enhance performance by reusing established connections. This reduces the overhead associated with frequently opening and closing connections.

## Conclusion

The RabbitMQ AutoScaler library provides an easy-to-use solution for dynamically scaling RabbitMQ consumers based on the message load. By following the above instructions, you can integrate it into your projects and ensure efficient message processing.

Feel free to reach out for any questions or further assistance. Happy coding!

## Blog
https://medium.com/@nishantthakre9/building-an-auto-scaling-library-for-rabbitmq-a-developers-journey-cad15f22d91c

## Package
https://pypi.org/project/rabbitmq-auto-scaler/

---
