### Server 1:

Web Server (Nginx): This server will serve as the primary web server responsible for handling HTTP requests from users' browsers. Nginx will serve static content and forward dynamic requests to the application server.
Application Files (Your Code Base): This server will host the application code and logic that generates dynamic web pages.


### Server 2:

Application Server: This server will work alongside the web server to process dynamic requests. It will execute your application code and communicate with the database to fetch and update data.
Database (MySQL): The database stores and manages structured data used by the website, such as user accounts, product listings, etc.


### Server 3:

Load Balancer (HAproxy): The load balancer will distribute incoming user requests across multiple web servers (Server 1). This helps distribute the load evenly and improves fault tolerance.
Specifics:

####### Additional Elements: ######

Load Balancer (HAproxy): Added to distribute traffic and provide high availability.
Server 2 (Application Server): Added to separate application processing from web serving for scalability.
Server 3 (Load Balancer): Added to evenly distribute traffic and provide redundancy.
Load Balancer Algorithm: The load balancer (HAproxy) is configured with a Round Robin distribution algorithm. This algorithm forwards each new request to the next server in line, ensuring a balanced workload distribution.

Active-Active Setup: The load balancer enables an Active-Active setup. In this configuration, all web servers (Server 1) are actively serving requests simultaneously. If one server fails, the load balancer redirects traffic to the remaining healthy servers.

Database Primary-Replica Cluster: The database (MySQL) is set up as a Primary-Replica (Master-Slave) cluster. The Primary node handles write operations (inserts, updates) and replicates data changes to the Replica node. The Replica node is used for read operations, reducing the load on the Primary node.

Difference Between Primary and Replica Nodes: In regard to the application, the Primary node is responsible for handling write operations, ensuring data consistency and integrity. The Replica node is used for read operations, improving read performance. This separation allows for horizontal scalability.

####### Issues: #######

Single Points of Failure (SPOF):

The load balancer (HAproxy) can become a single point of failure. To address this, you could set up a secondary load balancer for redundancy.
Lack of redundancy in the application and database servers could lead to downtime if one of them fails.
Security Issues:

There's no mention of a firewall in the design, leaving the infrastructure vulnerable to unauthorized access. Implementing a firewall is crucial for security.
HTTPS (SSL/TLS) is missing, which exposes user data to potential eavesdropping. Enabling HTTPS is necessary for data encryption in transit.
Monitoring:

There is no monitoring system in place to track the health and performance of servers and services. Implementing monitoring tools is essential for proactive issue detection and resolution.
