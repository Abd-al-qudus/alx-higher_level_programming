#!/bin/bash
git add .
echo "*****************************************************"
echo "*****************************************************"
echo "********** WELCOME BACK, ENGINEER PHOENIX ***********"
echo "*****************************************************"
echo "*****************************************************"
echo "[*] -- Enter commit message: "
read -r commitMessage
git commit -m "$commitMessage"
echo "[*] -- Branch(main/master): "
read -r branch
git push origin "$branch"

