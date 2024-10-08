import React, { ReactNode } from 'react'

interface ResultSectionProps {
    title: string;
    children: ReactNode;
}

const ResultSection: React.FC<ResultSectionProps> = ({ title, children }) => {
    return (
        <div className="bg-white shadow-md rounded-lg p-4">
            <h2 className="text-xl font-semibold mb-2">{title}</h2>
            <div className="prose max-w-none">{children}</div>
        </div>
    )
}

export default ResultSection
