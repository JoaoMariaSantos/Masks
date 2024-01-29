import React, {useState, useEffect} from 'react'
import { io } from 'socket.io-client'
import InputPage from './components/InputPage'
import EvolutionPage from './components/EvolutionPage'
import IntroductionPage from './components/IntroductionPage'
import ProxyContext from './ProxyContext'
import Header from './components/Header'

import './style/style.css'

const socket = io.connect("http://localhost:5000")

function App() {
  const proxyUrl = "http://localhost:5000";
  const [isGenerating, setIsGenerating] = useState(false)

  const [socketIsConnected, setSocketIsConnected] = useState(socket.connected);

  useEffect(() => {
    function onConnect() {
      setSocketIsConnected(true);
      console.log("connected to socket")
    }

    function onDisconnect() {
      setSocketIsConnected(false);
      console.log("disconnected from socket")
    }

    function newGeneration(value) {
      console.log("newGeneration")
    }

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);
    socket.on('new_generation', newGeneration);

    return () => {
      socket.off('connect', onConnect);
      socket.off('disconnect', onDisconnect);
      socket.off('new_generation', newGeneration);
    };
  }, []);

  useEffect(() => { //stops generation at startup
    fetch(proxyUrl + "/stopGeneration", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, [])

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
        {isGenerating ? <EvolutionPage stoppedGeneration={stoppedGeneration} socketIsConnected={socketIsConnected} socket={socket}/> : <InputPage startedGeneration={startedGeneration}/>}
      </ProxyContext.Provider>
      <Header/>
    </div>
  )
}

export default App