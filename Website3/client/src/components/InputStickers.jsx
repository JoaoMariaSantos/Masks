import React, {useState} from 'react'

function InputStickers({notifyStickersRequested}) {

  const [prompt, setPrompt] = useState('');

  const requestStickers = () => {
    if(prompt.length < 2) return;
    else notifyStickersRequested(prompt);
  }

  return (
    <div id='stickers_form'>
          <textarea type="text" name="prompt" placeholder="ex: going to a rock concert" onChange={(e) => {setPrompt(e.target.value)}}></textarea>
          <button className="material-symbols-outlined cell" onClick={requestStickers}>arrow_forward</button>
    </div>
  )
}

export default InputStickers