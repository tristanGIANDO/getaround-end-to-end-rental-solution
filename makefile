local-app:
	@echo "Building local app"
	streamlit run deployment/dashboard.py
	python api.py