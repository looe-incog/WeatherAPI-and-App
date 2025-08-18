# WeatherAPI
(Roadmap.sh based project)

This is a project that I chose to follow in order to apply the basics of python I learned from [Crash Course to Python](https://www.coursera.org/learn/python-crash-course/) by Google. It has extensive use of dictionary data type which I had trouble understanding at first. It is an idea from the  Weather API project by [Roadmap.sh](https://roadmap.sh/projects) wherein we create our own API that fetches from a third-party API, [Visual Crossing](https://www.visualcrossing.com/) in this case, and apply caching using [Redis](https://redis.io/).

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
