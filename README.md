# svdiff-api

First, install Docker Desktop and login.
Second, download the Dockerfile, main.py and requirements.txt and put these three in a "svdiff-api" folder.
Third, run the given below command in the command line of the respective folder.
  docker build -t svdiff-api .
  docker run -p 8000:8000 svdiff-api

Then, go to Docker Desktop and run the http://localhost:8000/.
