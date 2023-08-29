###
# Makefile
# Instalção do ambiente de Desenvolvimento,
# ferramentas de qualidade de código e testes.
###
#| awk '{if ($$1 == "Fixing") print "$(SUCCESS)" $$0 "$(RESET)"; else print "$(ERROR)" $$0 "$(RESET)"}'
### Colors:
# Reset
RESET='\033[0m'
# Regular Colors
ERROR='\033[0;31m'
SUCCESS='\033[0;32m'
WARNING='\033[0;33m'
BOLD = '\033[1m'

lint:## Roda o format, antes roda o lint.
	@echo -e ${BOLD}Start coding formatting with black...${RESET};
	@poetry run black --pyi --color . > /dev/null
	@if [ "$$?" -eq 0 ]; then \
		echo -e $?; \
	else \
		echo -e ${ERROR}Error: Black not format.${RESET}; \
		echo -e $?; \
	fi
	@echo -e ${BOLD}Start coding lint with ruff...${RESET};
	@poetry run ruff --fix . > /dev/null
	@if [ "$$?" -eq 0 ]; then \
		echo -e ${SUCCESS}Fixing lint with ruff...${RESET}; \
	else \
		echo -e ${ERROR}Error: Ruff not format.${RESET}; \
		echo -e $?; \
	fi

test:
	@echo -e ${BOLD}Start testing with pytest...${RESET};
	#@poetry run pytest -v --cov=app --cov-report=term-missing --cov-report=html tests/ > /dev/null	

######################################## GIT HOOKS ######################################
hooks:
	@echo "Configurando o Git Hooks."
# Verifica o VCS e adiciona os hooks
	@ if [ -d .git ]; then \
		echo "$$git_pre_commit" > .git/hooks/pre-commit; \
		echo "$$git_pre_push" > .git/hooks/pre-push; \
		chmod +x .git/hooks/pre-*; \
	fi

	@ if [ -d .hg ]; then \
		echo "$$hg_hooks" > .hg/hgrc; \
	fi

# Pre-commit
define git_pre_commit
#!/bin/bash
cd $$(git rev-parse --show-toplevel)
poetry run make lint
endef
export git_pre_commit

## Pre-push
define git_pre_push
#!/bin/bash
cd $$(git rev-parse --show-toplevel)
poetry run make test
endef
export git_pre_push

# Git Hooks
define hg_hooks
[hooks]
precommit.lint = (cd `hg root`; poetry run make lint)
pre-push.test = (cd `hg root`; poetry run make test)
endef
export hg_hooks
######################################## ./GIT HOOKS #####################################
create_module: ## Cria um novo módulo.
	@echo "============ Criando um novo módulo ============"
	@echo "Digite o nome do módulo: "
	@read module_name; \
	echo "Criando o módulo: $$module_name"; \
	mkdir -p app/$$module_name; \
	touch app/$$module_name/__init__.py; \
	mkdir -p app/$$module_name/controllers; \
	touch app/$$module_name/controllers/__init__.py; \
	touch app/$$module_name/controllers/$$module_name"_controller.py"; \
	mkdir -p app/$$module_name/models; \
	touch app/$$module_name/models/__init__.py; \
	mkdir -p app/$$module_name/repositories; \
	touch app/$$module_name/repositories/__init__.py; \
	touch app/$$module_name/repositories/$$module_name"_repository.py"; \
	mkdir -p app/$$module_name/routes; \
	touch app/$$module_name/routes/__init__.py; \
	touch app/$$module_name/routes/$$module_name"_routes.py"; \
	mkdir -p views/$$module_name; \
	mkdir -p tests/$$module_name; \
	touch tests/$$module_name/conftest.py; \
	touch tests/$$module_name/"test_"$$module_name"routes.py"; \
	touch tests/$$module_name/"test_"$$module_name"controllers.py"; \
	touch tests/$$module_name/"test_"$$module_name"repositories.py"; \
	touch tests/$$module_name/"test_"$$module_name"models.py"; \
	echo "Módulo criado com sucesso!"