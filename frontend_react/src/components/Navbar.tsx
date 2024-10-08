import React from 'react'
import { FileUp } from 'lucide-react'

const Navbar: React.FC = () => {
  return (
    <nav className="bg-blue-600 text-white p-4">
      <div className="container mx-auto flex items-center">
        <FileUp className="mr-2" size={24} />
        <h1 className="text-xl font-bold">CodeMotion Hackathon</h1>
      </div>
    </nav>
  )
}

export default Navbar