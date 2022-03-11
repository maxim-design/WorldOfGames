FROM python:alpine
WORKDIR /worldofgames
#fetching files for platform
COPY . .
#installing requirements
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r Data/requirements.dat
EXPOSE 5000
CMD python3 Leaderboard.py