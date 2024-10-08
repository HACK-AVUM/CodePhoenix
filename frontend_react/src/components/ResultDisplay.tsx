import React from 'react'
import ReactMarkdown from 'react-markdown'
import ResultSection from './ResultSection'

interface ResultDisplayProps {
  result: string | null
}

const ResultDisplay: React.FC<ResultDisplayProps> = ({ result }) => {
  if (!result) return null

  let parsedResult: Record<string, string>
  try {
    parsedResult = JSON.parse(result)
  } catch (error) {
    console.error('Failed to parse result JSON:', error)
    return <div>Error: Invalid result format</div>
  }

  return (
    <div className="w-full max-w-4xl mt-8 space-y-6">
      {Object.entries(parsedResult).map(([key, value]) => (
        <ResultSection key={key} title={key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}>
          <ReactMarkdown>{value}</ReactMarkdown>
        </ResultSection>
      ))}
    </div>
  )
}

export default ResultDisplay
