# How to use

Regenerate `package-lock.json`

    - `npm install --package-lock-only`

# Rename part of file 

```bash
for f in *viz*; do
  mv -- "$f" "${f//viz/vis}"
done
```