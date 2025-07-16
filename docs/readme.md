\# 🎙️ Neural Voice Dataset Preparation Pipeline



This repository contains a five-step pipeline for preparing high-quality training data for neural voice models (e.g., Microsoft Custom Neural Voice).



The pipeline transforms raw \*\*video files\*\* into a \*\*packaged dataset of labeled audio clips\*\*, ready for upload to a voice training service.



---



\## 🗂️ Notebooks Overview



| Notebook | Description |

|----------|-------------|

| `01-convert-video-to-audio.ipynb` | Extracts audio from video files |

| `02-clean-audio.ipynb`            | Converts audio to 16kHz mono WAV |

| `03-convert-speech-to-text.ipynb` | Transcribes audio with word-level timestamps |

| `04-segment-audio.ipynb`          | Segments audio into labeled clips |

| `05-create-voice-package.ipynb`   | Filters, packages, and prepares training data |



---



\## 🔁 Pipeline Steps



\### 🎞️ 1. Convert Video to Audio

\*\*Notebook:\*\* `01-convert-video-to-audio.ipynb`



\- Downloads video files from Azure Blob Storage.

\- Uses `ffmpeg` to extract the audio stream.

\- Outputs: Raw audio files for each video.



---



\### 🧼 2. Clean and Standardize Audio

\*\*Notebook:\*\* `02-clean-audio.ipynb`



\- Converts audio to 16kHz mono WAV using `ffmpeg`.

\- Ensures compatibility with Azure Speech Services.

\- Outputs: Clean WAV files stored in a designated Azure container.



---



\### 🗣️ 3. Convert Speech to Text

\*\*Notebook:\*\* `03-convert-speech-to-text.ipynb`



\- Submits audio files to Azure’s Custom Speech-to-Text API.

\- Enables word-level timestamps and punctuation.

\- Monitors transcription jobs and downloads the results.

\- Outputs: JSON transcription files per audio file.



---



\### ✂️ 4. Segment Audio into Labeled Clips

\*\*Notebook:\*\* `04-segment-audio.ipynb`



\- Parses transcription JSON to extract phrase-level segments.

\- Uses `ffmpeg` to extract corresponding audio clips.

\- Stores metadata for each segment (start/end/duration/text).

\- Uploads labeled segments to Azure.

\- Outputs: Short WAV clips with metadata for each phrase.



---



\### 📦 5. Create the Voice Package

\*\*Notebook:\*\* `05-create-voice-package.ipynb`



\- Downloads all segments and filters clips longer than 15s.

\- Generates a manifest: `clip\_name<TAB>transcription`.

\- Packages all files into a `.zip` archive.

\- Uploads final package to Azure for use in voice training.

\- Outputs: ZIP archive and manifest file.



---



\## 📁 Output Structure



The final training package contains:





