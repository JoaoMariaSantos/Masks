import React, {useState, useEffect} from 'react'

function InputStickers({notifyStickersRequested, requestDone}) {

  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(!requestDone)
    console.log("loading done")
  }, [requestDone]);

  const requestStickers = () => {
    if(prompt.length == 0 || loading) return;
    else {
      notifyStickersRequested(prompt);
      setLoading(true);
    }
  }

  return (
    <div id='stickers_form'>
          <textarea type="text" name="prompt" placeholder="ex: going to a rock concert" onChange={(e) => {setPrompt(e.target.value)}}></textarea>
          <button className="material-symbols-outlined cell" onClick={requestStickers}>{loading ? "hourglass_empty" : "arrow_forward"}</button>
    </div>
  )
}

export default InputStickers