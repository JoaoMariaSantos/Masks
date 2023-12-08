import React from 'react'

function StickerList({stickers}) {
  console.log(stickers);
  const stickerList = stickers.map((sticker) => {
    <div><img src={sticker.svg} alt={sticker.message} /></div>
  }) 

  

  return (
    <div id='sticker_list'>
        {stickers.map((sticker) => {
          return(
            <div>
              <img src={sticker.svg} alt={sticker.message} />
            </div>
          );
        })}
     </div>
  )
}

export default StickerList