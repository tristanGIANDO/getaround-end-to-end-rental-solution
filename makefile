local-app:
	@echo "Building local app"
	cd deployment
	streamlit run dashboard.py
	python main.py