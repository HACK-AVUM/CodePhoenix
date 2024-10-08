import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import FileUploader from './components/FileUploader'
import ResultDisplay from './components/ResultDisplay'



function App() {
  const [result, setResult] = useState<string | null>(null)
  const [taskId, setTaskId] = useState<string | null>(null)
  const [status, setStatus] = useState<string | null>(null)
  const [sonarQubeToken, setSonarQubeToken] = useState<string>('')
  const [showSonarQubeToken, setShowSonarQubeToken] = useState<boolean>(false)

  const handleFileUpload = async (file: File) => {
    setTaskId(null)
    setStatus(null)
    setResult(null)
    const formData = new FormData()
    formData.append('zip_file', file)
    formData.append('sonarqube_token', sonarQubeToken)

    setStatus('processing')
    try {
      const response = await fetch('http://localhost:60000/process-zip', {
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
      setResult(JSON.stringify({ error: 'Failed to process the code. Try checking the SonarQube token.' }, null, 2))
    }
  }

  useEffect(() => {
    const pollTaskStatus = async () => {
      if (taskId && status === 'processing') {
        try {
          const response = await fetch(`http://localhost:60000/task/${taskId}`)
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

  setShowSonarQubeToken(false);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />
      <div className="flex-grow flex flex-col items-center justify-center p-4">
        <div className="mb-4">
          {showSonarQubeToken && (
            <>
              <label htmlFor="sonarqube-token" className="block text-sm font-medium text-gray-700">
                SonarQube Token:
              </label>
              <input
                type="text"
                id="sonarqube-token"
                value={sonarQubeToken}
                onChange={(e) => setSonarQubeToken(e.target.value)}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                placeholder="Enter your SonarQube token"
              />
            </>
          )}
        </div>
        <FileUploader onFileUpload={handleFileUpload} />
        {status === 'processing' && <p>Elaborazione in corso... Attendere. Il processo può richiedere fino a 5 minuti.</p>}
        <ResultDisplay result={result} />
      </div>
    </div>
  )
}

export default App
