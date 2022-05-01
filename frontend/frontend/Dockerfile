FROM node:lts-alpine

#Install serve package
RUN npm i -g serve

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

# Executables
CMD [ "serve", "-s", "dist" ]