# File handling and directory structure

⏺ For a script in scripts/input/, I'd recommend download_data.py because:

  1. Action-oriented: Script names typically use verb-noun format (e.g., download_data,
  process_files, run_analysis) since they perform actions when executed
  2. More intuitive: When running python scripts/input/download_data.py, the command
  reads naturally as "download data"
  3. Consistency: Most Python scripts follow this pattern - the name describes what the
  script does

  Use data_downloader.py if it primarily contains a DataDownloader class or is a module
  to be imported elsewhere (noun = thing/component). Use download_data.py if it's an
  executable script (verb = action/command).

  Since it's in a scripts/ directory, download_data.py is the better choice.
