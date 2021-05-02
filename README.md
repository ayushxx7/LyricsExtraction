# Lyrics Extraction

## A simple web scaper which extract lyrics for any given song

| Library  | Use Case                                                                         |
| -------- | -------------------------------------------------------------------------------- |
| bs4      | Parse the webpage to generate HTML Tree. Extract required information from tree. |
| requests | Request Web Page from musixmatch that will be parsed.                            |

### Prerequisites

- Python3
- Libraries: requests and bs4

### How To Run

- Clone the repository

  ```
  git clone https://github.com/ayushxx7/LyricsExtraction
  ```

- Open command prompt and switch to this folder
- Install requirements

  ```
  py -m pip install -r requirements.txt
  ```

- Run the script
  ```
  py lyrics_extractor.py
  ```
- Enter song name
- Press Enter and wait for result

### Process

- Take input song name
- Generate MusixMatch search URL
- Make a get request to the URL
- Parse the webpage via BeautifulSoup
- Extract the `best match` element to find the song that matched with the input search term
- Extract URL from the `best match`
- Request the above URL
- Parse it via BeautifulSoup
- Extract the Paragraphs which have the lyrics via class: `mxm-lyrics__content`
- Iterate over the paragraphs and print them to the console

## Credits

Special thanks to [MusixMatch](https://www.musixmatch.com/) for providing such an awesome service.
