import React, { useCallback } from 'react'
import { useDropzone } from 'react-dropzone'
import { Upload } from 'lucide-react'

interface FileUploaderProps {
  onFileUpload: (file: File) => void
}

const FileUploader: React.FC<FileUploaderProps> = ({ onFileUpload }) => {
  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      onFileUpload(acceptedFiles[0])
    }
  }, [onFileUpload])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'application/zip': ['.zip'] },
    multiple: false,
  })

  return (
    <div
      {...getRootProps()}
      className={`w-full max-w-md p-6 mb-4 border-2 border-dashed rounded-lg text-center cursor-pointer transition-colors ${
        isDragActive ? 'border-blue-500 bg-blue-50' : 'border-gray-300 hover:border-blue-500'
      }`}
    >
      <input {...getInputProps()} />
      <Upload className="mx-auto mb-2" size={48} />
      <p className="text-lg font-semibold">
        {isDragActive ? 'Drop the ZIP file here' : 'Drag & drop a ZIP file here, or click to select'}
      </p>
    </div>
  )
}

export default FileUploader