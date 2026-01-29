import yaml
import random

with open("params.yaml") as f:
    params = yaml.safe_load(f)

lr = params["train"]["lr"]
epochs = params["train"]["epochs"]

accuracy = round(random.uniform(0.8, 0.99), 3)
loss = round(1 - accuracy, 3)

with open("metrics.json", "w") as f:
    f.write(f'{{"accuracy": {accuracy}, "loss": {loss}}}')
