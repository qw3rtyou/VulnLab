FROM node:14

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY ./deploy .

EXPOSE 10008
CMD ["npm", "start"]
