import React, {useState} from 'react'
import InputStickers from './InputStickers'
import StickerList from './StickerList'

function Stickers({notifyStickersChange}) {

  const [stickerList, setStickerList] = useState(null)

  const inputCellClasses = () => {
    let classes = "cell inputCell"
    if(stickerList) classes += " inputCell_ready"
    return classes
  }

  const stickersRequested = (text) => {
      requestStickers()
  }

  const requestStickers = async (query) => {
    console.log(query);
    const response = await fetch('/chosenEmojis', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
      },
      body: JSON.stringify({ query }),
    });

    const data = await response.json();
    //setStickerList(data.emojis);
    setStickerList(data.result);
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
      <div className={inputCellClasses()}>
        <div className='inputCell_heading'><h2>Stickers</h2></div>
        <div className='inputCell_description'><p>Tell us your plans</p></div>
        <div className="inputCell_assurance">
          <p>They are only used to choose your stickers</p>
        </div>
        <div className='inputCell_input'>
          <InputStickers notifyStickersRequested = {(text) => requestStickers(text)}/>
        </div>
        <div className='inputCell_result'>
          {stickerList && <StickerList stickers={stickerList}/>}
        </div>
      </div>
      </div>
  )
}

export default Stickers