import React, {useState, useEffect} from 'react'
import Header from './Header'
import HelpButton from './HelpButton'
import Photos from './Photos'
import Stickers from './Stickers'
import GenerateButton from './GenerateButton'

function InputPage() {

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
    if(photoReady){ //&& stickersReady
      console.log("generation ready");
      startGeneration();
    }
  }

  const startGeneration = () => {
    fetch("/startgeneration", {
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
    <div className='page'>
      <div>
        <Header/>
        <HelpButton/>
        <Photos notifyPhotoChange = {handlePhotoChange}/>
        <Stickers notifyStickersChange = {handleStickersChange}/>
        {photoReady && <GenerateButton notifyGeneratePressed = {handleGeneratePressed}/>}
      </div>
    </div>
  )
}

export default InputPage