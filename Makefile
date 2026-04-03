.PHONY: preprocess train predict evaluate

preprocess:
	python src/preprocess.py

train:
	python src/train.py

predict:
	python src/predict.py

evaluate:
	python src/evaluate.py
