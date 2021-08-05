version: '3.7'
services:
    flask:
        build: .
        ports:
            - "5000:5000"
        environment:
            - REDIS_HOST=redis
        depends_on:
            - redis
    redis:
        image: redis:5.0.7
        ports:
            - "6379:6379"
