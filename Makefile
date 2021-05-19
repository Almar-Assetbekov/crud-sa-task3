init: down-clear pull build yarn-i up
restart: down up

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

yarn-i:
	docker-compose run --rm node-cli yarn install

down-clear:
	docker-compose down -v --remove-orphans

build:
	docker-compose build

pull:
	docker-compose pull