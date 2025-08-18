# WeatherAPI
(Roadmap.sh based project)

This is a project that I chose to follow in order to apply the basics of python I learned from [Crash Course to Python](https://www.coursera.org/learn/python-crash-course/) by Google. It has extensive use of dictionary data type which I had trouble understanding at first. It is an idea from the  Weather API project by [Roadmap.sh](https://roadmap.sh/projects) wherein we create our own API that fetches from a third-party API, [Visual Crossing](https://www.visualcrossing.com/) in this case, and apply caching using [Redis](https://redis.io/).

![Weather API Roadmap.sh Idea](https://assets.roadmap.sh/guest/weather-api-f8i1q.png)

# Steps to run the project

1. Clone the repository
2. I recommend setting up a virtual environment first (skip if you already know these steps):
    
    a. In the cloned folder run
    ```sh
    python3 -m venv .dev
    ```
3. After setting up a virtual environment, install the following dependencies:
    
    a. Flask
    ```sh
    pip3 install flask
    ```
    b. Redis
      - Install Redis (Make sure to start it using the guide). Use [Redis Installation Guide](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/) as a reference
      - Install redis dependecy in python
         ```sh
         pip3 install redis
         ```
    c. Requests
    ```sh
    pip3 install requests
    ```
    d. PyQt6
    ```sh
    pip3 install PyQt6
    ```

4. Go to api folder and run flask
    ```sh
    cd api
    chmod +x ./flask
    ./flask
    ```
   Note: You only have to do chmod +x ./flask once. Otherwise if you want to test your app just run the flask as a first step.
4. Go application folder and run weather_app.py

    ```sh
    python3 weather_app.py
    ```

# References

1. Roadmap.sh
   - [Weather API](https://roadmap.sh/projects/weather-api-wrapper-service)

2. Visual Crossing
   - [Weather API](https://www.visualcrossing.com/weather-api/)

3. Redis
   - [redis-py guide](https://redis.io/docs/latest/clients/redis-py/)
   - [Redis Crash Course](https://www.youtube.com/watch?v=jgpVdJB2sKQ)

4. Flask
   - [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
   - [REST API Crash Course - Introduction + Full Python API Tutorial](https://www.youtube.com/watch?v=qbLc5a9jdXo)

5. PyQt6
   - [Creating your first app with PyQt6 by Martin Fitzpatrick](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-start)
