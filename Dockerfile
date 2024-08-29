FROM node:14-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --only=production && npm cache clean --force

EXPOSE 3000

CMD ["node", "server.js"]
