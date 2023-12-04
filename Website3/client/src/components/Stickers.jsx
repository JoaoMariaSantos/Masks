import React, {useState} from 'react'
import InputStickers from './InputStickers'
import StickerList from './StickerList'

function Stickers({notifyStickersChange}) {

  //const [stickerList, setStickerList] = useState([])

  const stickersRequested = (text) => {
      requestStickers()
  }

  const requestStickers = async (prompt) => {
    console.log(prompt);
    const response = await fetch('/chosenEmojis', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt }),
    });

    const data = await response.json();
    //setStickerList(data.emojis);
    console.log(data);
  }

  const stickerListDiv = (list) => {
    <div>
      {list.map((sticker) => (
        sticker
      ))}
    </div>
  }

  return (
    <div id='stickers'>
      <div className='cell inputCell'>
        <div className='inputCell_heading'><h2>Stickers</h2></div>
        <div className='inputCell_description'><p>Tell us your plans</p></div>
        <div className="inputCell_assurance">
          <p>They are only used to choose your stickers</p>
        </div>
        <div className='inputCell_input'>
          <InputStickers notifyStickersRequested = {(text) => requestStickers(text)}/>
        </div>
        <div className='inputCell_result'>
          <StickerList/>
        </div>
      </div>
      </div>
  )
}

export default Stickers