import React, {useState, useEffect, useContext} from 'react'
import Banner from './Banner'
import Header from './Header'
import Photos from './Photos'
import Stickers from './Stickers'
import GenerateButton from './GenerateButton'
import CodeButton from './CodeButton'
import ProxyContext from '../ProxyContext'

function InputPage() {
  const proxyUrl = useContext(ProxyContext)

  const [photoReady, setPhotoReady] = useState(false);
  const [stickersReady, setStickersReady] = useState(false);

  const handlePhotoChange = (state) =>{
    console.log("photo ready:" + state)
    setPhotoReady(state);
  }

  const handleStickersChange = (state) =>{
    console.log("stickers:" + state)
    setStickersReady(state);
  }

  const handleGeneratePressed = () =>{
    console.log("generate button was pressed \nPhoto: " + photoReady + "\nStickers: " + stickersReady);
    if(photoReady && stickersReady){
      console.log("generation ready");
      startGeneration();
    }
  }

  const startGeneration = () => {
    fetch(proxyUrl + "/startgeneration", {
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
  };

  return (
    <div id='inputPage' className='page'>
      <div>
        <Banner/>
        <Header/>
        <CodeButton/>
        <Photos notifyPhotoChange = {handlePhotoChange}/>
        <Stickers notifyStickersChange = {handleStickersChange}/>
        {photoReady && stickersReady && <GenerateButton notifyGeneratePressed = {handleGeneratePressed}/>}
      </div>
    </div>
  )
}

export default InputPage