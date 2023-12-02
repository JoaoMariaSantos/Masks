import React from 'react'

function InputStickers() {

  return (
    <form id='stickers_form'>
          <textarea type="text" name="prompt" placeholder="ex: going to a rock concert"></textarea>
          <button type="submit" class="material-symbols-outlined cell">arrow_forward</button>
    </form>
  )
}

export default InputStickers