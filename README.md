# Singularity Registry Containers

Hi there! This is a feed of "registered" Singularity registries. You can submit a pull request (PR) to this repo if you have deployed a <a href="https://singularityhub.github.io/sregistry">Singularity Registry</a> with containers to share! We will provide more documentation soon, however here is how to get started:

1. You will first want to fork the repo, clone it to your local computer.
2. Next, copy one of the current registry pages under [_registries](_registries). Fill in your appropriate information, and be sure to look at our [assets/img/registry](assets/img/registry) folder to choose a robot image that you like. Feel free to add your institution image, or another robot! Here is an example registry:

```
---
layout: registry
title:  "Stanford University"
base: https://containers.stanford.edu
date:   2017-08-29 16:54:46
author: Vanessa Sochat
categories:
- registry
img: robot1.png
thumb: robot1.png
tagged: public, academic, hpc
institution: Stanford University
---

Stanford Containers is a registry of containers for Stanford University that doesn't exist yet!
```

Note that it's important that you specify http or https, so the site is directed to correctly. You should generally choose the same image for your `thumbnail` and `img` but we've provided both so you can customize.

3. When you are ready to test, run `jekyll serve`.

We will be adding more search and browsability, along with tests that will be run regularly to ensure the health of your registry. For now, enjoy! And please contribute to both projects via feedback and help.
