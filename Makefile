.PHONY: venv preprocess train predict evaluate test
venv:
	python -m venv .venv
preprocess:
	python src/preprocess.py --config config/default.yaml
train:
	python src/train.py --config config/default.yaml
predict:
	python src/predict.py --config config/default.yaml
evaluate:
	python src/evaluate.py --config config/default.yaml
test:
	pytest
