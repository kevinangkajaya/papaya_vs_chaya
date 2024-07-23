# AUTOGENERATED! DO NOT EDIT! File to edit: gradio.ipynb.

# %% auto 0
__all__ = ['exampleImagesList', 'plt', 'learn', 'categories', 'image', 'label', 'intf', 'classify_image']

# %% gradio.ipynb 1
from fastai.vision.all import *
import gradio as gr

# %% gradio.ipynb 2
exampleImagesList = ['images/chaya/chaya leaf.jpg','images/chaya/chaya plants.jpg',
                     'images/papaya/papaya fruit.jpg','images/papaya/papaya leaf.jpg','images/papaya/papaya plant and fruit.jpg']

# %% gradio.ipynb 6
# needed for Hugging Face platform
import pathlib
plt = platform.system()
if plt == 'Windows': pathlib.WindowsPath = pathlib.PosixPath

# %% gradio.ipynb 7
print("posix path:", pathlib.PosixPath)
print("windows path:", pathlib.WindowsPath)
print("plt:", plt)

# %% gradio.ipynb 8
learn = load_learner('training_export/export.pkl')

# %% gradio.ipynb 10
categories = ('Chaya plant', 'Papaya fruit', 'Papaya plant')
def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

# %% gradio.ipynb 12
image = gr.components.Image(width=192,height=192)
label = gr.components.Label()

intf = gr.Interface(fn=classify_image, inputs = image, outputs = label, examples = exampleImagesList)
intf.launch(inline=False)
