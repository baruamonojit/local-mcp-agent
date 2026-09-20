APP_NAME = wedding-agent
PORT = 8501

.PHONY: build run stop logs

build:
	docker build -t $(APP_NAME) .

run:
	docker run -d \
		--name $(APP_NAME) \
		--network=host \
		-e OLLAMA_BASE_URL="http://127.0.0.1:11434" \
		--env-file .env \
		$(APP_NAME)
	@echo "Wedding Planner running at http://localhost:$(PORT)"

stop:
	-docker stop $(APP_NAME)
	-docker rm $(APP_NAME)

logs:
	docker logs -f $(APP_NAME)