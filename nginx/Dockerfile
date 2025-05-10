# i think now it is clear what we have done here
FROM nginx:1.21-alpine

# remove the default nginx server configuration and copy ours
# for that create a file nginx.conf in the same folder as the Dockerfile
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d