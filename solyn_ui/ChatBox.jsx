
import React, { useState } from 'react'
import axios from 'axios'

const ChatBox = () => {
  const [message, setMessage] = useState('')
  const [response, setResponse] = useState('')

  const sendMessage = async () => {
    try {
      const res = await axios.post(import.meta.env.VITE_API_BASE_URL + "/ask", {
        question: message,
      })
      setResponse(res.data.answer)
    } catch (err) {
      setResponse("Error: " + err.message)
    }
  }

  return (
    <div className="w-full max-w-xl">
      <textarea
        className="w-full p-2 bg-gray-800 border border-purple-500 rounded"
        rows={4}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask Solyn..."
      />
      <button
        onClick={sendMessage}
        className="mt-2 px-4 py-2 bg-purple-600 rounded text-white"
      >
        Send
      </button>
      {response && (
        <div className="mt-4 p-3 bg-gray-700 rounded">
          <strong>Solyn:</strong> {response}
        </div>
      )}
    </div>
  )
}

export default ChatBox
