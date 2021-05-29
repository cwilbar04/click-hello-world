venv-windows:
	python -m venv ..\.venv
	@echo VirtualENV Setup Complete. Now run: ..\.venv\Scripts\Activate

install:
	pip install --upgrade pip
	pip install -r requirements.txt