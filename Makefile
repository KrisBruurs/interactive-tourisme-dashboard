.PHONY: download_data transform_data dashboard

requirements: requirements.txt
	pip install -r requirements.txt

download_data: download_data.py
	python download_data.py

transform_data: transform.py data/tourism_data.csv
	python transform.py

dashboard: app.py data/transformed_tourism_data.csv
	streamlit run app.py

remove_data:
	rm -f data/*.csv