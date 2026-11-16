FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY public /usr/share/nginx/html
HEALTHCHECK CMD wget -qO- http://127.0.0.1/ >/dev/null || exit 1
