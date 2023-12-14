import React from 'react'
import Header from './Header'
import CodeButton from './CodeButton'
import EvolutionCell from './EvolutionCell'
import IndividualCell from './IndividualCell'
import Banner from './Banner'

function EvolutionPage() {
  return (
    <div id='evolutionPage' className='page'>
      <div>
        <Banner/>
        <Header/>
        <CodeButton/>
        <EvolutionCell/>
        <IndividualCell/>
      </div>
    </div>
  )
}

export default EvolutionPage