.PHONY: clean

NAME 	   	:= Aliens Attack
VERSION		:= 1.0
DEVELOPERS	:= Reinaldo Barrera Travieso
COPYRIGHT  	:= Copyright © 2022: $(DEVELOPERS)


run: ## Run the app desktop
	python3 main.py

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

clean: ## Remove temporary files
	rm -rf __pycache__/
	rm -rf modules/__pycache__/
	rm -rf tools/__pycache__/
	rm -rf visual/__pycache__/

install: ## Install the project dependencies
	pip3 install numpy
	pip3 install scipy
	pip3 install PyQt5
	pip3 install opencv
	pip3 install Pillow
	pip3 install pydicom
	pip3 install imageio
	pip3 install skimage

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
