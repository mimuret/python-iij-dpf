all: setup.py

setup.py: swagger.json
	docker run --rm -u `id -u`:`id -g` -v ${PWD}:/local openapitools/openapi-generator-cli \
	generate \
	--input-spec /local/swagger.json \
	--generator-name python \
	--output /local/
