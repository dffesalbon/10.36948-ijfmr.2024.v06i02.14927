#!/bin/bash
#exec > ./console.txt 2>&1
echo "Scraping data.."
py ./scrape.py 100
echo "Consolidating.."
py ./consolidate.py
echo "Filtering english detected chats.."
py ./filter.py
