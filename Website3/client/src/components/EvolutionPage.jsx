import React from 'react'
import Header from './Header'
import CodeButton from './CodeButton'
import EvolutionCell from './EvolutionCell'
import IndividualCell from './IndividualCell'

function EvolutionPage() {
  return (
    <div id='evolutionPage' className='page'>
      <div>
        <Header/>
        <CodeButton/>
        <EvolutionCell/>
        <IndividualCell/>
      </div>
    </div>
  )
}

export default EvolutionPage