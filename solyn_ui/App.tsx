import React, { useState } from 'react'
import ToolPanel from './ToolPanel'

function App() {
  const [input, setInput] = useState('')
  const [response, setResponse] = useState('')

  const askSolyn = async () => {
    const res = await fetch('http://localhost:8000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: input })
    })
    const data = await res.json()
    setResponse(data.answer || 'No response')
  }

  return (
    <div style={{ padding: '2em', fontFamily: 'Arial, sans-serif' }}>
      <h1>🌌 Solyn</h1>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask Solyn..."
        style={{ width: '60%', padding: '0.5em' }}
      />
      <button onClick={askSolyn} style={{ marginLeft: '1em' }}>Send</button>
      <p><strong>Solyn:</strong> {response}</p>
      <ToolPanel />
    </div>
  )
}

export default App