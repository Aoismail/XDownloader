FROM nginx:alpine

COPY index.html /usr/share/nginx/html/
COPY server.js /app/

RUN apk add --no-cache nodejs npm
RUN npm install express

EXPOSE 80

CMD ["sh", "-c", "nginx && node /app/server.js"]
