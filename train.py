import yaml
import random,os

with open("params.yaml") as f:
    params = yaml.safe_load(f)

lr = params["train"]["lr"]
epochs = params["train"]["epochs"]

accuracy = round(random.uniform(0.8, 0.99), 3)
loss = round(1 - accuracy, 3)
#simulate large modal outputs and save
os.makedirs("output", exist_ok=True)
text = "trained modal and this is demo large file content\n" * 100
with open("output/model.txt", "w") as f:
    f.write(text)

with open("output/metrics.json", "w") as f:
    f.write(f'{{"accuracy": {accuracy}, "loss": {loss}}}')
