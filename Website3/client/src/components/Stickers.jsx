import React from 'react'
import InputStickers from './InputStickers'

function Stickers() {
  return (
    <div id='stickers' className='cell inputCell'>
      <div className='inputCell_heading'><h2>Stickers</h2></div>
      <div className='inputCell_description'><p>Tell us your plans</p></div>
      <div className='inputCell_body'>
        <InputStickers/>
      </div>
    </div>
  )
}

export default Stickers