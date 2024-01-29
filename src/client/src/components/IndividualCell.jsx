import React, {useEffect, useState, useContext } from 'react'
import EvolutionBar from './EvolutionBar'
import StickersDownload from './StickersDownload'

function IndividualCell({individualSrc, bestFitness}) {

    return (
        <div id='individualCell' className='cell'>
            {individualSrc && (
              <img src={individualSrc} alt="best result so far" />
            )}

            
        <EvolutionBar bestFitness={bestFitness}/>
        <StickersDownload/>
        </div>
    )
}

export default IndividualCell