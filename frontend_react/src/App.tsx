import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import FileUploader from './components/FileUploader'
import ResultDisplay from './components/ResultDisplay'

function App() {
  const [result, setResult] = useState<string | null>(null)
  const [taskId, setTaskId] = useState<string | null>(null)
  const [status, setStatus] = useState<string | null>(null)
  const [docFormat, setDocFormat] = useState<string>('pdf')

  let domain = window.location.origin.split(':').slice(0, -1).join(':');

  const handleFileUpload = async (file: File) => {
    setTaskId(null)
    setStatus(null)
    setResult(null)
    const formData = new FormData()
    formData.append('zip_file', file)
    formData.append('doc_format', docFormat)

    setStatus('processing')
    try {
      const response = await fetch(`${domain}:60000/process-zip`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Failed to process ZIP file')
      }

      const data = await response.json()
      setTaskId(data.task_id)
    } catch (error) {
      console.error('Error processing ZIP file:', error)
      setResult(JSON.stringify({ error: 'Failed to process ZIP file' }, null, 2))
    }
  }

  useEffect(() => {
    const pollTaskStatus = async () => {
      if (taskId && status === 'processing') {
        try {
          const response = await fetch(`${domain}:60000/task/${taskId}`)
          const data = await response.json()

          if (data.status === 'completed') {
            setStatus('completed')
            setResult(JSON.stringify(data.result, null, 2))
          } else if (data.status === 'processing') {
            setTimeout(pollTaskStatus, 2000) // Poll every 2 seconds
          } else if (data.status === 'error') {
            setStatus('error')
            setResult(JSON.stringify(data.result, null, 2))
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
        <div className="mb-4">
          <label htmlFor="docFormat" className="mr-2">Formato della documentazione:</label>
          <select
            id="docFormat"
            value={docFormat}
            onChange={(e) => setDocFormat(e.target.value)}
            className="border rounded p-1"
          >
            <option value="pdf">PDF</option>
            <option value="markdown">Markdown</option>
            <option value="html">HTML</option>
          </select>
        </div>
        <FileUploader onFileUpload={handleFileUpload} />
        {status === 'processing' && <p>Elaborazione in corso... Attendere. Il processo può richiedere fino a 5 minuti.</p>}
        <ResultDisplay result={result} />
      </div>
    </div>
  )
}

export default App
