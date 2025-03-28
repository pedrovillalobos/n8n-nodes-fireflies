# n8n-nodes-fireflies

Custom n8n node module for Fireflies.ai.
This node provides transcription information based on the Meeting ID that you can collect from their webhook call to you n8n installation.
It also provides the full transcription and a script to convert the transcription to SRT and TXT. Right now, just copy and paste the content of [convert-sentence-to-srt-txt](convert-sentence-to-srt-txt.py) in a script node in n8n

This was fully built using ChatGPT, and no guarantee is given, although it was tested and worked before being published.

## Installation

1. Copy or clone this folder to your local machine.
2. Package the module (if needed) or simply copy the folder into your n8n custom nodes directory. For example, if you use the default n8n setup, place the folder in `~/.n8n/nodes/node_modules/`.
3. Restart n8n.
4. In the n8n UI, you should now see a new credential type called **"Fireflies API"** and a node called **"Fireflies Transcript Query (by Meeting ID)"**.

## Usage

1. Create a credential using your Fireflies API
2. Use the node to query the Fireflies API by providing a meeting ID. The node will return the complete transcript data including audio URL, transcript text, and meeting metadata.
