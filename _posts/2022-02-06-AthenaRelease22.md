---
title: Introduction on how to write an Athena(ATLAS) package for release22
category: tech
classes: wide
---

I am writing this post is because I recently met some problem of writing an Athena Algorithm for my research.
I am using a simple code to get lepton n-tuples from xAODs to feed to my RNN. However, there are not enought  release21 samples and thus,
I need to turn to release22. In release22, the previouse function `TrackParticle.vertex()` function is gone. As a result, I need to use the 
new methods. For some reason, my code is not compatible with the new methods for getting vertex. Consequently, I would need to turn my Root based code
into Athena framework. Below are the steps and some problems I met. I did this under the guidance of Matthew Basso. 


## The Structure of folders


## The jobOptions

## Make jobOptions.py executable 

