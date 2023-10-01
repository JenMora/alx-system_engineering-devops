Infrastructure Design:

Server 1:

Web Server (Nginx): This server is dedicated to serving static content and handling incoming HTTP requests from users' browsers. Nginx will forward dynamic requests to the application server.


Server 2:

Application Server: This server is responsible for executing the application code and generating dynamic web pages. It communicates with the database server to fetch and update data.


Server 3:

Database (MySQL): This server stores and manages structured data used by the website, such as user accounts, product listings, etc.


Server 4:

Load Balancer Cluster (HAproxy): This server is part of a load balancer cluster with the other load balancer. It distributes incoming user requests to the web servers (Server 1) for load balancing and high availability.


Server 5:

Load Balancer Cluster (HAproxy): This is the second load balancer server in the cluster, working in conjunction with Server 4. It ensures redundancy and fault tolerance for load balancing.
Specifics:

Additional Server 4 (Load Balancer): We've added a second load balancer server (Server 5) to create a high-availability and fault-tolerant cluster. In case one load balancer fails, the other can seamlessly take over, ensuring uninterrupted service.

Component Splitting (Web, Application, Database): Each component (web server, application server, and database) is on its dedicated server to achieve better resource isolation, scalability, and maintainability. Splitting components allows you to scale each part independently based on its specific requirements.

Load Balancer Cluster: We've configured two load balancer servers (Server 4 and Server 5) as a cluster for redundancy and load distribution. If one load balancer becomes unavailable or overloaded, the other can handle the traffic.

Reasons for Additions:

Second Load Balancer (Server 5):

Added for high availability: If one load balancer fails, the other can continue to distribute traffic.
Provides fault tolerance: In case of hardware or software issues, the cluster can still operate.
Ensures load balancing: Helps evenly distribute incoming user requests, preventing overload on a single load balancer.
Component Splitting:

Web Server (Server 1): Separated to efficiently serve static content and handle web requests.
Application Server (Server 2): Dedicated to running application logic for dynamic content.
Database Server (Server 3): Isolated for data storage and management, enhancing security and scalability.
Load Balancer Cluster:

Ensures high availability: Load balancer clustering enhances system availability and minimizes downtime.
Facilitates scalability: Distributes incoming traffic across multiple web servers for better performance.
Provides redundancy: In case of a load balancer failure, the other can take over, preventing service interruptions.
