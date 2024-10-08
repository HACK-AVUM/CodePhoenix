import React, { useState, useEffect } from 'react'
import { Upload, FileUp } from 'lucide-react'
import Navbar from './components/Navbar'
import FileUploader from './components/FileUploader'
import ResultDisplay from './components/ResultDisplay'
import ResultSection from './components/ResultSection'

// Import a markdown parser library (you'll need to install this)
import ReactMarkdown from 'react-markdown'




function App() {
  const [result, setResult] = useState<string | null>(null)
  const [taskId, setTaskId] = useState<string | null>(null)
  const [status, setStatus] = useState<string | null>(null)

  const handleFileUpload = async (file: File) => {
    const formData = new FormData()
    formData.append('zip_file', file)

    try {
      const response = await fetch('http://localhost:8000/process-zip', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Failed to process ZIP file')
      }

      const data = await response.json()
      setTaskId(data.task_id)
      setStatus('processing')
    } catch (error) {
      console.error('Error processing ZIP file:', error)
      setResult(JSON.stringify({ error: 'Failed to process ZIP file' }, null, 2))
    }
  }

  useEffect(() => {
    const pollTaskStatus = async () => {
      if (taskId && status === 'processing') {
        try {
          const response = await fetch(`http://localhost:8000/task/${taskId}`)
          const data = await response.json()

          if (data.status === 'completed') {
            setStatus('completed')
            setResult(JSON.stringify(data.result, null, 2))
          } else if (data.status === 'processing') {
            setTimeout(pollTaskStatus, 2000) // Poll every 2 seconds
          }
        } catch (error) {
          console.error('Error polling task status:', error)
          setStatus('error')
        }
      }
    }

    pollTaskStatus()
  }, [taskId, status])

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />
      <div className="flex-grow flex flex-col items-center justify-center p-4">
        <FileUploader onFileUpload={handleFileUpload} />
        {status === 'processing' && <p>Processing... Please wait.</p>}
        <ResultDisplay result={result} />
      </div>
    </div>
  )
}

export default App
