---
title: Papaya Vs Chaya
emoji: 📉
colorFrom: purple
colorTo: gray
sdk: gradio
sdk_version: 4.39.0
app_file: app.py
pinned: false
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

### Papaya vs Chaya Plants
- Upload your image and check if it is papaya plants or chaya plants!
- Both plants look very similar at first glance.
- [NOT WORKING] Go here to check the Jupyter notebook: https://mybinder.org/v2/gh/kevinangkajaya/papaya_vs_chaya/main?urlpath=%2Fvoila%2Frender%2Fprod.ipynb
- According to Wikipedia, The papaya (/pəˈpaɪə/, US: /pəˈpɑːjə/), papaw, (/pəˈpɔː/) or pawpaw (/ˈpɔːpɔː/) is the plant species Carica papaya, one of the 21 accepted species in the genus Carica of the family Caricaceae, and also the name of its fruit.
    - It was first domesticated in Mesoamerica, within modern-day southern Mexico and Central America. It is grown in several countries in regions with a tropical climate. In 2022, India produced 38% of the world's supply of papayas.
    - ![Papaya plant and fruit](./images/papaya/papaya%20plant%20and%20fruit.jpg)
    - ![Papaya leaf](./images/papaya/papaya%20leaf.jpg)
    - ![Papaya fruit](./images/papaya/papaya%20fruit.jpg)
- According to Wikipedia, Cnidoscolus aconitifolius, commonly known as chaya, tree spinach, or spinach tree, is a large, fast-growing and leafy perennial shrub that is believed to have originated in the Yucatán Peninsula of southeastern México.
    - As with most euphorbias, the entire plant contains a caustic, viscous and potentially dangerous white sap which flows readily when any part of the plant is broken, cut or damaged. 
    - The leaves should always be cooked before being eaten, as the raw leaves contain a high amount of toxic hydrocyanic acid, in addition to the irritating sap typical of Euphorbiaceae family members. Care should be taken to avoid getting any raw plant material into one’s mucous membranes; i.e., the sap, juice and hydrocyanic acids should, ideally, never contact one’s mouth, eyes, genitals, nose, inner ears or any otherwise open wound or injury.
    - ![Chaya leaf](./images/chaya/chaya%20leaf.jpg)
    - ![Chaya plants](./images/chaya/chaya%20plants.jpg)
- Note that this project is very simple, it cannot accurately judge pictures that are not papaya or chaya. Open the website: https://kevinangkajaya.github.io/papaya_vs_chaya

### Git Miscellaneous
- This project has two remote URLs:
    - github: git@github.com:kevinangkajaya/papaya_vs_chaya.git
    - huggingface: git@hf.co:spaces/kevinangkajaya/papaya_vs_chaya
- How to push to multiple remote URLs is explained here: https://stackoverflow.com/questions/849308/how-can-i-pull-push-from-multiple-remote-locations
    - `git remote set-url origin --push --add <a remote>`
    - `git remote set-url origin --push --add <another remote>`
    - `git remote -v`
- Note that, normally, HuggingFace wouldn't accept a file greater than 10 MB. To allow this, we need to use Git LFS.
    - You will need to enter the following the first time you are initializing your repository. Put these in the command line on the repository path:
    - `git lfs install`
    - `git lfs track "*.pkl"`
    - Check this website for more information: https://www.tanishq.ai/blog/posts/2021-11-16-gradio-huggingface.html
- When we are using Git LFS, it is normal to be asked for login or SSH passphrase multiple times, usually we are asked 3 or 4 times. 
    - We can check more details here https://github.com/git-lfs/git-lfs/issues/3318. Here is the quote from the page: 
    > During the normal lifetime of a request such as a push, git-lfs will generally need to get credentials a few times - once to actually push content to the remote, as well as some additional API requests to do LFS-specific operations. As such, it's normal for git-lfs to need credentials three times as you're seeing here.
    - Note that for this project, because we have two remote URLs (github and hugging face), in total we need to enter credentials 6-8 times.
    - We can add `git config lfs.cachecredentials true` or `git config --global credential.helper cache` to cause Git LFS to cache credentials for the lifetime of an operation, so we only need to enter the credential once. However, the credential will still be prompted every time we do a `push`.

### How to Copy to Another Project (This Project As a Template)
- Go to https://huggingface.co/, login into your account.
- Select `+New` -> `Space`.
- On the `Create a New Space`:
    - Choose a suitable Space name.
    - Choose `apache-2.0` license.
    - `Select the Space SDK`: `Gradio` -> `Blank`.
    - Let `Space hardware` be default.
    - Choose `Public` visibility.
    - Click `Create Space`.
- Clone the new repository to your working local PC by either HTTPS or SSH.
- Make sure you already have this repository access on your working local PC or from Hugging Face user interface.
- On your working local PC, copy the following from this repository to the new repository:
    - .gitignore
    - requirements.txt
    - dev.ipynb
    - gradio.ipynb
- Adjust dev.ipynb as necessary. This dev.ipynb is used for setting up images folder, training the model by the image data, and make sure everything worked perfectly.
- Adjust gradio.ipynb as necessary. This gradio.ipynb is used for configuring settings for Hugging Face (with Gradio) interface. This uses file data of `training_export/export.pkl` to set up the model.
- Copy the content of README.md from this repository to the new repository. DO NOT delete existing section on the new repository, instead, skip copying that section (the part with `title`, `emoji`, `colorfrom`). Copy other sections, and edit as necessary.
- Now you can save and commit your changes to Hugging Face's remote git.