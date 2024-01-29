import React from 'react'
import Banner from './Banner';
import HelpButton from './HelpButton';

function Header() {
  return (
    <div id='header'>
      <HelpButton/>
      <div id='siteName' className='cell'>
          <h1>Incognito Stickers</h1>
      </div>
    </div>
  )
}

export default Header;