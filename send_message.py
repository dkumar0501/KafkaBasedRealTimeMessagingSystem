from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9008')
   
topic = 'dkumar0501-topic' 
for i in range(10):  
    message = f'Hello Kafka {i}'   
    producer.send(topic, value=message.encode('utf-8'))
    print(f"Sent: {message}")  
  
producer.flush() 
     
   
 
 





















