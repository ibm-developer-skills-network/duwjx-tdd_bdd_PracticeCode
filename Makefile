# Builds an environment for Behave and Selenium

.PHONY: all help bdd app

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-\\.]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

all: help

bdd: ## Install pre-requisite software for BDD
	$(info Install BDD prerequisite software...)
	sudo apt-get update
	sudo apt-get install -y sqlite3 chromium-driver python3-selenium
 
app: ## Run the BDD application
	$(info Running BDD Application...)
	docker run -d --name bdd \
		-p 8080:8080 \
		-e DATABASE_URI=sqlite:///test.db \
		rofrano/lab-flask-bdd:1.0
