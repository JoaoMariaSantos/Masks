import React from 'react'
import Header from './Header'

function HelpPage() {
  const handleClickScroll = () => {
    const element = document.getElementById('inputPage');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div id='helpPage' className='page'>
      <div>
      <Header/>
      <button className='cell' onClick={handleClickScroll}><h2>Back</h2></button>
      <a href="https://github.com/JoaoMariaSantos" className='cell' target="_blank">repository</a>
      <div className='cell'>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
      </div>
    </div>
  )
}

export default HelpPage