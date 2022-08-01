# This is a basic workflow to help you get started with Actions

name: twitch_m3ugrabber

# Controls when the workflow will run
on:
  schedule:
    - cron: '*/10 * * * *'
  
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2

      # 
      - name: config
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "GitHub Action"
      
      
      - name: Main
        run: |
          pwd
          chmod +x autorun_github.sh
          ./autorun_github.sh
          #cd scripts
          #python3 twitch_m3ugrabber.py > ../twitch.m3u
          echo "m3u grabbed"
        
      - name: git add
        run: |
          git add -A
          ls -la 
          
      - name: commit & push
        run: |
          git commit -m "links are updated"
          git push
