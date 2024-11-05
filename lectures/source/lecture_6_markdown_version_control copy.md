---
marp: true
paginate: true

# You can also start simply with 'default'
theme: Seriph

background: ./resources/global/background.jpg
# apply unocss classes to the current slide
class: text-left

drawings:
  persist: false

transition: slide-left
---

# Dr. Mindaugas Šarpis
# Lessons on **Data Analysis** from **CERN**

## Lecture 6

### **Version** Control

---

## Git 

### Commits 
- git commit
    - git commit -m "Initial Commit" 

---

### Branches
- git branch Development 
    - git checkout -b Development
    - git merge branch
    - git rebase branch

---

### HEAD 
- git checkout {commit} (detaches head)

---

### Relative refs
- git checkout main^ (parent)
- git checkout main~x (parent x)

---

### Branch forcing 
- git branch -f main {commit} (or relative ref)

---

### Resetting changes

- git reset {commit} (works locally)
- git revert {commit} {works on remotes / creates a new commit}

---

### Moving work around 

- git cherry-pick {commit1} {commit2} ...

---

### Interactive rebase

- git rebase -i {branch}

---