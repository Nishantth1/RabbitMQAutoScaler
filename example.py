import asyncio
from rabbitmq_auto_scaler import AutoScaler

async def message_handler(message):
    print(f"Handling message: {message.body.decode()}")

async def main():
    mq_url = 'amqps://your_username:your_password@your_rabbitmq_url:5671'
    queue = 'your_queue_name'
    min_consumers = 1
    max_consumers = 10
    scale_up_threshold = 10
    scale_down_threshold = 1
    check_interval = 5

    auto_scaler = AutoScaler(mq_url, queue, min_consumers, max_consumers, scale_up_threshold, scale_down_threshold, check_interval)
    await auto_scaler.set_message_handler(message_handler)
    
    await auto_scaler.start()
    while True:
        await asyncio.sleep(3600)
        await auto_scaler.stop()
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")