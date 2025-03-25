FROM python:3.12 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN reflex export --frontend-only --no-zip

FROM nginx

COPY --from=builder /app/.web/_static /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
