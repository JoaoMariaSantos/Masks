import React from 'react'

function GenerateButton({notifyGeneratePressed}) {
  return (
    <button className='cell' id='GenerateButton' onClick={notifyGeneratePressed}>
        <h2>Generate</h2>
    </button>
  )
}

export default GenerateButton