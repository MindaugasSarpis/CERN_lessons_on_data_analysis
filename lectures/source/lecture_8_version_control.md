---
marp: true
paginate: true

background: ./resources/global/background.jpg
# apply unocss classes to the current slide
class: text-left

drawings:
  persist: false

transition: fade

---

# Dr. Mindaugas Šarpis
# Lessons on **Data Analysis** from **CERN**

## Lecture 8

### **Version** Control using Git

---
layout: image-right
image: ./resources/git/comic_version.jfif
backgroundSize: contain
---

# The Importance of Version Control

- ### Even if working alone, many different version of the same file will exist. 
- ### Some overwritten changes might be needed later.
- ### A "versioned" file might be needed when implementing comments from supervisor / reviewers. 
- ### This hold true for written work, code and other files. 

---

# Tracking Changes (differences)  

- ## Rather than saving multiple copies of the same file, we can track changes.
- ## `git` is an open-source version control system that is used to track changes in files.

![](./resources/git/play-changes.svg)

---

![](./resources/git/conflict.svg)

---

![](./resources/git/git_staging.svg)

---

![](./resources/git/git-committing.svg)

---

![](./resources/git/git-freshly-made-github-repo.svg)

---

![](./resources/git/git-restore.svg)

---

![](./resources/git/git-staging-area.svg)

---

![](./resources/git/github-collaboration.svg)

---

![](./resources/git/github-repo-after-first-push.svg)

---

![](./resources/git/merge.svg)

---

![](./resources/git/versions.svg)

--- 3

```bash
git init
```

---