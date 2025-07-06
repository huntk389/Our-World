
import React, { useState } from 'react'
import ChatBox from './components/ChatBox'
import ToolPanel from './components/ToolPanel'
import MemoryView from './components/MemoryView'

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center p-4 space-y-4">
      <h1 className="text-3xl font-bold text-purple-400">Solyn</h1>
      <ChatBox />
      <ToolPanel />
      <MemoryView />
    </div>
  )
}

export default App
