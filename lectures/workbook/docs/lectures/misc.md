# How to use

## Need Node.js >=18
`sudo apt-get install -y nodejs`

## Install Slidev globally with pnpm
`npm i -g pnpm`

`pnpm i -g @slidev/cli`

## For hosting
Regenerate `package-lock.json`

    - `npm install --package-lock-only`

# Rename part of file 

```bash
for f in *viz*; do
  mv -- "$f" "${f//viz/vis}"
done
```