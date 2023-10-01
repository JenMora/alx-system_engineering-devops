Infrastructure Design:

Server 1:

Web Server (Nginx): This server will serve as the primary web server responsible for handling HTTP requests from users' browsers. Nginx will also be responsible for terminating SSL and serving encrypted traffic over HTTPS.
Application Server: This server will handle application logic and communicate with the database.
Monitoring Client: This client will collect performance and log data from the server and send it to a monitoring service like Sumo Logic.


Server 2:

Web Server (Nginx): Similar to Server 1, this server will serve as a backup web server, ensuring high availability and redundancy in case Server 1 fails.Application Server: Similar to Server 1, this server will handle application logic and communicate with the database.
Monitoring Client: Similar to Server 1, this client will collect performance and log data.


Server 3:

Database (MySQL): This server will host the MySQL database, ensuring data persistence.
Firewall: Firewalls will be set up to protect each server from unauthorized access.
Specifics:

Firewalls: Firewalls are added to enhance security. They control incoming and outgoing network traffic, allowing only authorized traffic and blocking potential threats.

SSL Certificate (HTTPS): Serving traffic over HTTPS is essential for encrypting data in transit, ensuring data privacy and security for users. It also helps establish trust with visitors.

Monitoring: Monitoring is used to track the health and performance of servers and services in real-time. It helps identify issues proactively and optimize system performance.

Monitoring Data Collection: Monitoring clients (data collectors) on each server are responsible for collecting performance metrics, logs, and other data. This data is sent to a central monitoring service (e.g., Sumo Logic) for analysis.

Monitoring Web Server QPS (Queries Per Second): To monitor web server QPS, you can set up monitoring tools to track the number of incoming requests per second. By analyzing this data, you can identify trends and potential performance bottlenecks.

Issues:

Terminating SSL at the Load Balancer Level:

Terminating SSL at the load balancer is not necessarily an issue, but it can be if sensitive data is transmitted within the internal network after decryption. To mitigate this, you can implement end-to-end encryption by using SSL/TLS between the load balancer and the web servers as well.



Single MySQL Server for Writes:

Having only one MySQL server capable of accepting writes creates a single point of failure. If the database server fails, write operations become impossible, resulting in downtime. Consider implementing a Primary-Replica (Master-Slave) configuration or database clustering for high availability and redundancy.


Identical Server Components:

Having servers with all the same components (database, web server, and application server) might lead to inefficiencies in resource utilization. For optimal performance, consider separating database servers from web/application servers and use load balancing for distribution. This architecture allows for better scalability and resource allocation.


