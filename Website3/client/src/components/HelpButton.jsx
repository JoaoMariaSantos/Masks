import React from 'react'

function HelpButton() {

  const handleClickScroll = () => {
    const element = document.getElementById('helpPage');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <button id='helpButton' className='cell' onClick={handleClickScroll}><h1>?</h1></button>
  )
}

export default HelpButton