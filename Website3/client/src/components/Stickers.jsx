import React, {useState, useContext} from 'react'
import InputStickers from './InputStickers'
import StickerList from './StickerList'
import ProxyContext from '../ProxyContext'

function Stickers({notifyStickersChange}) {
  const proxyUrl = useContext(ProxyContext)
  const [stickerList, setStickerList] = useState(null)
  const [requestFinished, setRequestFinished] = useState(true);

  const inputCellClasses = () => {
    let classes = "cell inputCell"
    if(stickerList) classes += " inputCell_ready"
    return classes
  }

  const stickersRequested = (text) => {
      requestStickers()
  }

  const requestStickers = async (query) => {
    setRequestFinished(false)
    console.log(query);
    const response = await fetch(proxyUrl + '/chosenEmojis', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
      },
      body: JSON.stringify({ query }),
    });

    if (!response) {
      throw new Error('Error fetching emojis')
    }

    const data = await response.json();

    setStickerList(data.result);
    setRequestFinished(true);
    notifyStickersChange(true);
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
        <div className='inputCell_description'><p>Tell us your plans to generate a set of emojis</p></div>
        {/*<div className="inputCell_assurance">
          <p>They are only used to choose your stickers</p>
        </div>*/}
        <div className='inputCell_input'>
          <InputStickers notifyStickersRequested = {(text) => requestStickers(text)} requestDone = {requestFinished}/>
        </div>
        <div className='inputCell_result'>
          {stickerList && <StickerList stickers={stickerList}/>}
        </div>
      </div>
      </div>
  )
}

export default Stickers