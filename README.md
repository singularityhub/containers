# Singularity Registry Containers

[![CircleCI](https://circleci.com/gh/singularityhub/containers.svg?style=svg)](https://circleci.com/gh/singularityhub/containers)

Hi there! This is a feed of "registered" Singularity registries. You can submit a pull request (PR) to this repo if you have deployed a <a href="https://singularityhub.github.io/sregistry">Singularity Registry</a> with containers to share! 

## How to Register
You have two options:

### Automatic Generation
You can have your registry generate the metadata for you, fork and clone this repository, add the file to the [_registries](_registries) folder, and submit a PR.  Complete instructions are [provided here.](https://singularityhub.github.io/sregistry/setup.html#registration)

### Manual Generation
You can also produce this file manually, although it's more error prone you can fix with results of our testing. Here are specific instructions:

1. Fork the repo, clone it to your local computer.
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
img: robots/robot1.png
thumb: robots/robot1.png
tagged: public, academic, hpc
institution: Stanford University
---

Stanford Containers is a registry of containers for Stanford University that doesn't exist yet!
```

The name of the markdown file MUST coincide with the [REGISTRY_URI](https://singularityhub.github.io/sregistry/deployment.html#registry-contact) you have chosen for your endpoint. Thus, if my registry identifier is `taco` then the file would need to be called `taco-registry.md`. Note that the images `robots/robot1.png` are found in the `assets/img/registry` folder. If you want your registry to be private, meaning no listing of a base or containers, then simply change the layout to `registry-private`.


Note that it's important that you specify http or https, so the site is directed to correctly. You should generally choose the same image for your `thumbnail` and `img` but we've provided both so you can customize.

3. When you are ready to test, run `jekyll serve`.

## How does it work?
We run basic tests to ensure that the following matches up. For matching, we use the identifier endpoint served by your registry, which typically looks like `{{domain}}/api/registry/identity`. Specifically:

 - the file you add in [_registries](_registries) is named according to your registry uri (eg `taco`--> `taco-registry.md`)
 - the `base` field must return 200 response, along with the identifier endpoint
 - the uri we parse from the file (eg, `taco`) must match to the `id` served by the endpoint

We will be adding more search and browsability, along with tests that will be run regularly to ensure the health of your registry. For now, enjoy! And please contribute to both projects via feedback and help.
