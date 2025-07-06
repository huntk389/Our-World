import React, { useState } from 'react'
import axios from 'axios'

const API = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export default function ToolPanel() {
  const [status, setStatus] = useState('')

  const callTool = async (endpoint, method = 'POST') => {
    setStatus('⏳ Running...')
    try {
      const url = `${API}/tool/${endpoint}`
      const response = await axios({ url, method })
      setStatus(`✅ ${endpoint} complete`)
    } catch (err) {
      setStatus(`❌ ${endpoint} failed`)
    }
  }

  return (
    <div style={{ marginTop: '1em', padding: '1em', border: '1px solid #ccc' }}>
      <h3>🛠 Solyn Tools</h3>
      <button onClick={() => callTool('create')}>📝 Create File</button>
      <button onClick={() => callTool('search?q=latest+news', 'GET')}>🔍 Web Search</button>
      <button onClick={() => callTool('files', 'GET')}>📂 List Files</button>
      <button onClick={() => callTool('index')}>🧠 Reload Memory</button>
      <p>{status}</p>
    </div>
  )
}