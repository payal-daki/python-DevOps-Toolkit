student_info = {
    "name": "anshal",
    "age" : "22",
    "class" : "10"
}

#modifies value
student_info ["age"] = 25
print (student_info)

#delete a value 
del student_info ["class"]
print(student_info)

#check existing
if "age" in student_info:
    print("its present in dictionaries")

#iterating through keys and values
for key, value in student_info.items():
    print(key, value)

#print name 
print(student_info["name"])




#another example
ec2_instance_info = [
    {
        "id":"instance_001",
        "type": "t2.micro"
    },
    { 
        "id":"instance_002",
        "type": "t2.meadium"     
    },
    {
        "id":"instance_003",
        "type": "t2.xlarge"
    }
]
print(ec2_instance_info [1]["id"])




#In this example, the function get_server_status optimizes the retrieval of the server status by using the get method and providing a default value 
# if the server name is not found.

# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")

