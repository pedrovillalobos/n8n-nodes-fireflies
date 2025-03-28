// Helper: Convert seconds (as a number or string) to SRT timestamp "HH:MM:SS,mmm"
function secondsToTimestamp(seconds) {
    seconds = parseFloat(seconds);
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = Math.floor(seconds % 60);
    const millis = Math.floor((seconds - Math.floor(seconds)) * 1000);
    return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')},${String(millis).padStart(3, '0')}`;
}

// Get the transcript data from the first input item
const transcript = items[0].json;

if (!transcript || !Array.isArray(transcript.sentences)) {
    throw new Error("Transcript data or sentences not found.");
}

const sentences = transcript.sentences;
let content = "";

// Build the content (SRT format)
sentences.forEach((sentence, index) => {
    const blockNumber = index + 1;
    const startTimestamp = secondsToTimestamp(sentence.start_time);
    const endTimestamp = secondsToTimestamp(sentence.end_time);
    const speaker = sentence.speaker_name ? sentence.speaker_name + ": " : "";
    const text = sentence.text || "";
    
    content += `${blockNumber}\n${startTimestamp} --> ${endTimestamp}\n${speaker}${text}\n\n`;
});

// Build the base file name using the transcript's dateString and title.
const baseFileName = new Date(transcript.dateString).toISOString().split('T')[0] + " - " + transcript.title;

// Return a single item with a folderName and an array of file objects
return [
    {
        json: {
            folderName: baseFileName, // This will be used for your folder name
            files: [
                {
                    fileName: baseFileName + ".srt",
                    content: content,
                },
                {
                    fileName: baseFileName + ".txt",
                    content: content,
                },
            ],
        },
    },
];