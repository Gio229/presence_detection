run: 
	@echo "=> Running the application.."
	@python src/main.py

start: prepare-x11
	docker compose up --build

prepare-x11:
	@echo "Autorizing X11 access for Docker containers..."
	xhost +local:docker
	@echo "DISPLAY = $(DISPLAY)"

build:
	docker compose build

up: prepare-x11
	docker compose up 

up-detach: prepare-x11
	docker compose up -d

down:
	docker compose down

rebuild:
	docker compose build --no-cache

logs:
	docker compose logs -f detector

exec:
	docker exec -it detector /bin/bash