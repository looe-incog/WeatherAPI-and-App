# WeatherAPI
(Roadmap.sh based project)

This is a project that I chose to follow in order to apply the basics of python I learned from [Crash Course to Python](https://www.coursera.org/learn/python-crash-course/) by Google. It has extensive use of dictionary data type which I had trouble understanding at first. It is an idea from the  Weather API project by [Roadmap.sh](https://roadmap.sh/projects) wherein we create our own API that fetches from a third-party API, [Visual Crossing](https://www.visualcrossing.com/) in this case, and apply caching using [Redis](https://redis.io/).

![Weather API Roadmap.sh Idea](https://assets.roadmap.sh/guest/weather-api-f8i1q.png)

# Steps to run the project

1. Clone the repository
2. In the folder click, install dependencies. This should be only done one time. It set ups a virtual environement so that the dependencies used in this project is isolated. After that, it installs the necessary dependencies which you can view in the depencies.txt generated after its execution.
3. Go to api folder
   - Open weather.py and find the following line:
      ```python
      url = "" #enter your API link here from visual crossing
      ```
      To get the API link, create an account in [Visual Crossing](https://www.visualcrossing.com/), then do the following:
      - Go to Weather API section
      - Enter your location (Example: Philippines)
      - Click "Build your first API query"
      - Under Data and API design, click API.
      - Copy the link in the textbox.
      - Enter the link in the line mentioned above then save.

4. Go back to the WeatherAPI-and-App folder and run the following:
   - run_api
   - run_app

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
