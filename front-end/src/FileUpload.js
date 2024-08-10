import React, { useState } from 'react';

function FileUpload() {
    const [file, setFile] = useState(null);
    const [docId, setDocId] = useState(null);
    const [summary, setSummary] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();
        setDocId(data.id);
    };

    const handleSummarize = async () => {
        const response = await fetch('http://localhost:5000/summarize', {
            method: 'POST',
            headers: {
                'content-Type': 'application/json',
            },
            body: JSON.stringify({ id: docId }),
        });

        const data = await response.json();
        setSummary(data.summary);
    };

    return (
        <div>
            <h2>Upload Document</h2>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>

            {docId && (
                <>
                    <h3>Document ID: {docId}</h3>
                    <button onClick={handleSummarize}>Summarize</button>
                </>
            )}

            {
                summary && (
                    <div>
                        <h3>summary</h3>
                        <p>{summary}</p>
                    </div>
                )}
        </div>
    );

}
export default FileUpload;