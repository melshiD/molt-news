#!/bin/sh
set -e
cd /home/node/.openclaw/workspace/molt-news
git rm ruminate/reports/hingul-app.html
git add ruminate/reports/hangul-app.html ruminate/reports/index.html
git status
git commit -m "fix: rename Hingul to Hangul throughout Korean learning app"
git push
