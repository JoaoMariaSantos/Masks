import React, {useState, useEffect, useContext} from 'react'
import io from 'socket.io-client';
import Header from './Header'
import CodeButton from './CodeButton'
import HelpButton from './HelpButton';
import EvolutionCell from './EvolutionCell'
import IndividualCell from './IndividualCell'
import Banner from './Banner'
import ProxyContext from '../ProxyContext';

function EvolutionPage() {
  const proxyUrl = useContext(ProxyContext)

  useEffect(() => {
    const socket = io(proxyUrl);

    socket.on('connect', () => {
      console.log('Connected to Flask server');
    });

    socket.on('new_generation', (message) => {
      console.log('Received message from Flask:', message);
      // Handle the message in your React component
    });

    return () => {
      socket.disconnect();
    };
  }, []);


  return (
    <div id='evolutionPage' className='page'>
      <div>
        <Banner/>
        <Header/>
        <HelpButton/>
        <EvolutionCell/>
        <IndividualCell/>
      </div>
    </div>
  )
}

export default EvolutionPage