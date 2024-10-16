# build container from existing docker python 3.11 image
FROM python:3.11

# port to expose docker to
EXPOSE 5000

# set working directory in docker
WORKDIR /app

# copy current local directory to docker
COPY . .

# install packages in container
RUN pip install -r requirements.txt

# pass the command to run flask app and ask it to listen on host 0.0.0.0
CMD ["flask", "run", "--host", "0.0.0.0"]


# Docker Commands

# Command to build the image
# docker build -t rest-apis .

# Command to run the docker container. {local port} : {docker port}
# docker run -p 5005:5000 rest-apis

# Running the container but in detached mode
# docker run -dp 5005:5000 rest-apis

# Running the container but in detached mode with volume mounting the local dir
# docker run -p 5005:5000 -w /app -v "C:\Users\91991\Documents\My Git Repository\misc-projects\restful-api-python\3-rest-api-with-uuid\:/app" rest-apis 



