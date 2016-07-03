# Scraping

This section scrapes poemhunter.com for poems written by RF. The strategy for doing this is as following:

1) Identify which poems on poemhunter.com is by RF. Create a csv file with links.

2) Call on those links, identify the block of html source where the poem is. Save into temp .txt files.

3) Process the temp .txt files and clean out the poem.