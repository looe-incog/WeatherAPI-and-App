# WeatherAPI
(Roadmap.sh based project)

This project was inspired by the [Weather API Project](https://roadmap.sh/projects/weather-api-wrapper-service) from [Roadmap.sh](https://roadmap.sh/). I worked on it to help me understand the basics of REST API development. Using flask, I developed a local weather API that fetches data from a third-party API and used Redis for caching to avoid reduntant requests and enhance response time. The API and frontend communicate locally or through the machine's loopback addres. It is not a production-ready service and was just a mini project for me to learn how APIs are structured, how caching improves performance, and how applications can get data from API endpoints. It served as my first step in getting familiar with REST API design and allowing me to practice JSON handling and Python programming. I included instructions how to run it, just in case.

This project consists of two components:
1. A Flask API which receives and caches data locally (using Redis) and exposes endpoints.
2. A weather app which is a very simple frontend that consumes the Flask API.

**Note:** The entire project is meant to run locally on a single machine.
   - The Flask API is bound to 127.0.0.1, and should only be accessed by applications on the same device running it.
   - No part of the system is exposed to the internet or local network.

![Weather API Roadmap.sh Idea](https://assets.roadmap.sh/guest/weather-api-f8i1q.png)

# Steps to run the project

1. Install Redis
   - Go to [**Redis Installation Guide**](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/) and follow which is applicable on your operating system.
   - Don't forget to start redis and close it after you run this project. (Instructions are also included in the link above)

2. Clone the repository
   ```sh
   git clone https://github.com/looe-incog/WeatherAPI-and-App.git
   cd WeatherAPI-and-App
   ```  
3. Install dependencies(one-time-setup)
   - Inside the project folder, run the script:
      ```sh
      ./install_dependencies
      ```
   - This will:
      - Create a virtual environment (`.dev\`) so that the dependecies are only installed inside the project.
      - Install all required dependencies.
      - Generate a `dependencies.txt` that lists dependencies installed

4. Configure the API key
   - Go to the `api/` folder and open `weather.py` using any text editor.
   - Find this line:
      ```python
      url = "" #Enter your API link here from visual crossing
      ```
   - To get the API link:
      - Create an account at [Visual Crossing](https://www.visualcrossing.com/)
      - Go to **Weather API** section
      - Enter your location (Example: Philippines)
      - Click **Build your first API Query**
      - Under **Data and API design**, click **API**
      - Copy the link shown in that textbox
   - Enter that link between the **url** line above and save the file.

5. Run the project
   From the root folder (`WeatherAPI-and-APP/`), run both scripts in separate terminals
   ```sh
   ./run_api
   ./run_app
   ```
   - `run_api` starts the Weaather API (backend)
   - `run_app` starts the Weather App (frontend)

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
