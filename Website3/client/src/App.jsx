import React, {useState} from 'react'
import InputPage from './components/InputPage'
import EvolutionPage from './components/EvolutionPage'

import './style/style.css'


function App() {
  const [isGenerating, setIsGenerating] = useState(false)

  return (
    <div>
      {isGenerating ? <EvolutionPage/> : <InputPage/>}
    </div>
  )
}

export default App