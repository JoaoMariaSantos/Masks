import React, {useState} from 'react'
import InputPage from './components/InputPage'
import EvolutionPage from './components/EvolutionPage'
import IntroductionPage from './components/IntroductionPage'
import ProxyContext from './ProxyContext'
import Header from './components/Header'

import './style/style.css'


function App() {
  const proxyUrl = "http://localhost:5000";
  const [isGenerating, setIsGenerating] = useState(false)

  const startedGeneration = () => {
    setIsGenerating(true)
  }

  const stoppedGeneration = () => {
    setIsGenerating(false)
  }

  const generationChange = (state) => {
    setIsGenerating(state)
  }

  return (
    <div>
      <ProxyContext.Provider value = {proxyUrl}>
      <IntroductionPage/>
        {isGenerating ? <EvolutionPage stoppedGeneration={stoppedGeneration}/> : <InputPage startedGeneration={startedGeneration}/>}
      </ProxyContext.Provider>
      <Header/>
    </div>
  )
}

export default App