venv-windows:
	python -m venv ..\.venv
	@echo 
	@echo VirtualENV Setup Complete. Now run: ..\.venv\Scripts\Activate
	@echo 

install:
	pip install --upgrade pip
	pip install -r requirements.txt