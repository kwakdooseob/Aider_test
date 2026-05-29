import React, { useState } from 'react';

const FileUpload: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [uploadProgress, setUploadProgress] = useState<number>(0);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            const selectedFile = event.target.files[0];
            const allowedTypes = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/pdf', 'application/vnd.openxmlformats-officedocument.presentationml.presentation'];
            if (allowedTypes.includes(selectedFile.type)) {
                setFile(selectedFile);
                setErrorMessage(null);
            } else {
                alert('Invalid file type. Please upload a .docx, .pdf, or .pptx file.');
                setErrorMessage('Invalid file type');
            }
        }
    };

    const handleUpload = async () => {
        if (file) {
            setIsLoading(true);
            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await fetch('/api/upload', {
                    method: 'POST',
                    body: formData,
                    onUploadProgress: (progressEvent) => {
                        setUploadProgress(Math.round((progressEvent.loaded * 100) / progressEvent.total));
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    alert('File uploaded successfully!');
                    console.log('Extracted text:', data.text);
                    setFile(null);
                    setErrorMessage(null);
                    setIsLoading(false);
                } else {
                    const errorData = await response.json();
                    alert(`File upload failed: ${errorData.message}`);
                    setErrorMessage(errorData.message);
                    setIsLoading(false);
                }
            } catch (error: any) {
                console.error('Error uploading file:', error);
                alert('An error occurred while uploading the file.');
                setErrorMessage(error.message);
                setIsLoading(false);
            }
        }
    };

    return (
        <div>
            <h2>Upload File</h2>
            <input type="file" onChange={handleFileChange} />
            {file && (
                <div>
                    <p>Selected file: {file.name}</p>
                    <button onClick={handleUpload} disabled={isLoading}>
                        {isLoading ? 'Uploading...' : 'Upload'}
                    </button>
                    {uploadProgress > 0 && uploadProgress < 100 && (
                        <progress value={uploadProgress} max="100"></progress>
                    )}
                    {errorMessage && <p style={{ color: 'red' }}>Error: {errorMessage}</p>}
                </div>
            )}
        </div>
    );
};

export default FileUpload;
