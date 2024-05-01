## About the project

This project has consisted on the creation of a web application that given a URL it will retrieve the robots.txt file of the website and display it as an HTML page.

### Built With

* [![Python][Python3]][python-url]
* [![Django][Django]][django-url]
* [![Docker][Docker]][docker-url]


[View demo](https://youtu.be/wLOKXOGNh34)

## Usage

To run this project you have two options, to run it with docker, or run it using python:

### Prerequisites:

1. ```sh
   git clone https://github.com/aamargant/robots.git
   ```
2. ```sh
   cd robots/
   ```

### Run with Docker:

Below is an exmaple of how can you deploy the application using Docker:

1. Build the docker image
   ```sh
   docker build . -t django-robots-v0.0.1
   ```

2. Run the docker image:
   ```sh
   docker run -it -p 8000:8000 django-robots-v0.0.1
   ```

Note: When running with docker the logs will state that the development server started at ```http://0.0.0.0:8000/``` but if you want it to access through your local computer you must access it through ```http://127.0.0.1:8000/```

### Run with Python:

Below is an exmaple of how can you run the application using Python:

1. Install pipenv
   ```sh
   pip3 install pipenv
   ```

2. Install dependencies:
   ```sh
   pipenv install
   ```
3. Activate virtual environment:
   ```sh
   pipenv shell
   ```
4. Run:
   ```sh
   pipenv run python manage.py runserver
   ```
You can view the application at: ```http://127.0.0.1:8000/```

### Run tests:

Below is an exmaple of how can you run tests for this application:

- With python
   ```sh
   pipenv run python manage.py test
   ```

- With Docker:
   ```sh
   docker run -it -p 8000:8000 django-robots-v0.0.1 test
   ```

## Scaling to Millions Of Users

To scale up this porject to millions of users per day we would need different technologies and tools to make this happen.

First of all, I used Django framework for this project because is python-based and has a lot of already built-in tools that make Django quite a complete framework to use when having to deal with a lot of users. For this project use-case I have not used most of the Django features because it was very simple use-case but I chose Django with the mindset so we can built it and improve it overtime with more features coming regularly. (E.g Database, Modeling, Caching, Admin site, etc...)

Key points to take into account to scale up to millions of users per day:
- Client-side rendering: When a client makes the request to our app instead of creating the html in the server side, the server only sends the required data to the client and is the client’s browser the one that’s actually generating the html page, this frees up resources on the server so it can process more requests and it helps scale the application.
- Caching requests: Cache requests that are frequently requested so instead of actually doing the requests to the website to ge the robots.txt file we will answer from the cache, which will be stored in a temporary storage layer. This comes with the challenge on how to invalidate this caching so we would need to set up a system that every x time does a request to the wbesite and checks that the robots.txt file has not been change or getting somehow and event from a website that the robots.txt file has change and we need to ivnalidate the cache. Nonetheless I think robots.txt files do not change frequently.
- Asynchronously process requests: When a thread does a request instead of waitting for it, it will move on to the next task to do. This will allow to handle more requests and improve the responsiveness of the application. For this we would need a message broker between the client and the server so it can handle which tasks need to be done.
- Resiliency/Reliability/Availability: In production environmnets we will need resiliency so if there is any issue with the application we can fall back to another instance of the application instantly, with the use of a loadbalancer.
- Monitoring (metrics, logs): We would need to collect different kinds of metrics to help us gain insights and understand the performance and health status of the application at any given time. Also an alerting system needs to be set up so that we are alerted in case of an incident. (E.g Datadog, Prometheus, Grafana, AlertManager, etc...)

High-level architecture for this application:

![alt text](/arch.drawio.png)

It can be replicated to be in more regions and zones depending on how resilient/available we want the system to be and of course depending on the budget for this project.

To set up the previous architecture I would use terraform and terragrunt to set up infrastructure (VPCs, subnets, DNS, Internet Gateways, NAT, etc...).
To deploy the actual application I would use Kubernetes with Helm charts and ArgoCD. With Kubernetes we have a cluster that is elastic and it will shrink and grow dependning on the CPU usage of the compute VMs.


## Possible Enhancements

- Make this app store the robots.txt file into a Database.
- Analyse and extract insights from multiple robots.txt file from multiple websites.
- Create charts and dashboars with the most banned user-agent in different regions for example.



## Contributing

If you have any suggestion that would make this better, fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/<feature-name>`)
3. Commit your Changes (`git commit -m 'Add some <feature-name>'`)
4. Push to the Branch (`git push origin feature/<feature-name>`)
5. Open a Pull Request to this project

## References

- [Django Intro](https://docs.djangoproject.com/en/5.0/intro/tutorial01)
- [Analyzing one million robots.txt files](https://intoli.com/blog/analyzing-one-million-robots-txt-files/)
- [Instagram using django/python at scale](https://instagram-engineering.com/tagged/python)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python3]: https://img.shields.io/badge/python3-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://nextjs.org/
[django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[django-url]: https://www.djangoproject.com/
[docker]: https://img.shields.io/badge/Docker-1E63ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/