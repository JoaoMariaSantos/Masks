import React from 'react'
import Header from './Header'
import HelpButton from './HelpButton'
import Photos from './Photos'
import Emojis from './Stickers'

function MainPage() {
  return (
    <div className='page'>
      <div>
        <Header/>
        <HelpButton/>
        <Photos/>
        <Emojis/>
      </div>
    </div>
  )
}

export default MainPage