
help:
	cat Makefile
run:
	docker-compose up
exec:
	docker-compose exec handson-ml2-vn bash
build: stop .FORCE
	docker-compose build
rebuild: stop .FORCE
	docker-compose build --no-cache
stop:
	docker stop handson-ml2-vn || true; docker rm handson-ml2-vn || true;
.FORCE:
