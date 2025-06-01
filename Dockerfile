FROM node:18  # Or python/java image based on your backend
WORKDIR /app
COPY . .
RUN npm install  # Or pip install requirements.txt
CMD ["node", "server.js"]  # Or python app.py

