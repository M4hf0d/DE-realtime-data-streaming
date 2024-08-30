import uuid
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "mhfd",
    'start_date': datetime(2024, 8, 26, 21, 12),
}

#fetch random user data from the API
def get_data():
    import json
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    # first user's information 
    res = res['results'][0]
    return res 

# format the fetched user data into a structured dictionary
def format_data(res):
    data = {}
    location = res['location']
    data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    # Convert UUID objects to strings to ensure they are JSON serializable
    for key, value in data.items():
        if isinstance(value, uuid.UUID):
            data[key] = str(value)   
    return data

# Function to stream formatted user data to a Kafka topic
def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    # Setting up a Kafka producer to send data to Kafka, 
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)  # broker:29092 : advertised listener ip
    curr_time = time.time()

    # Streaming loop to send data to Kafka for 1 minute
    while True:
        if time.time() > curr_time + 60: 
            break
        try:
            # Fetch and format data
            res = get_data()
            res = format_data(res)
            # Send the formatted data to the 'users_created' Kafka topic
            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue

# Define the Airflow DAG for automating the data streaming process
with DAG("user_automation", 
        default_args=default_args,
        schedule="@daily",  
        catchup=False) as dag:
    # PythonOperator to run the stream_data function within the DAG
    streaming_task = PythonOperator(
        task_id="stream_data_from_api",
        python_callable=stream_data,
    )

    
    # submit a job : spark-submit --master spark://localhost:7077 spark_stream.py
