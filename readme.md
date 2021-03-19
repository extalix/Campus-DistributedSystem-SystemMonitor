# **COMPUTER RESOURCE MONITOR**

This app could be used for monitoring computers' resources in network. It consist of server side script and client side script. Server side script handles data from clients and print to screen using *tabulate dependency*. Client side script handles sending data from client's machine to server. As for now, clients only send CPU usage (%) and RAM usage (%) from *psutil dependencies*. It is possible to send other resources value in the future.

# Dependencies
- **psutil** - Fetch CPU & RAM usage value
- **tabulate** - Pretty print array into table

# prerequisite
- Python 3.9
- virtualenv / conda / other

# how to
1. Create virtual environment using virtualenv or conda
```
virtualenv CRM
```
2. Install dependencies using pip from requirement.txt
```
pip install -r requirement.txt
```
3. run Server.py on server's machine
4. run Client.py on clients' machines
